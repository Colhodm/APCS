# Define categorizer functions here, which will be used by categorize_utils.py
# Each categorizer function takes an accession id and raw text

from mammo_utils.utils import *
import string
import xml.etree.ElementTree as ET

#-----------------------------
# Exam type categories:
#-----------------------------

def is_mammo((acc_id, text)):
	words = text.split(' ')
	first_2 = ' '.join(words[:2])		# Check first two words to to see if this note contains a report or not

	default_cutoff = 25					# By default, check the first 25 words to see if it contains the phrase 'mammo'
	try:
		cutoff = words.index('date:')
		if cutoff > 2:					# Edge case: if date is the first field, use the default
			cutoff = min(cutoff, default_cutoff)
		else:
			cutoff = default_cutoff
	except:
		cutoff = default_cutoff
	first_part = ' '.join(words[:cutoff])

	if 'i have' in first_2 or 'please' in first_2 or 'dear doctor' in first_2 or 'addendum' in first_2:
		return False
	elif 'mammo' in first_part:
		return True
	else:
		try:
			idx = words.index('impression:')
			impression_str = ' '.join(words[idx + 1 : idx + 6])
			return 'mammo' in impresson_str
		except:
			return False

#-----------------------------
# Abnormality categories:
#-----------------------------

# Rough heuristic to determine whether a file contains masses or not
def is_mass((acc_id, text)):
	return 'mass' in text

# Uses existing NLP results to determine whether a mass has been detected
def nlp_is_mass((acc_id, text)):
	root = get_nlp_result(acc_id)
	abnormalities = root.find('Abnormalities')
	for abnormality in abnormalities:
		if abnormality.get('type') == 'Mass':
			return True
	return False

#-----------------------------
# BI-RADS categories:
#-----------------------------

def birads_0((acc_id, text)):
	return ('birads 0' in text or 'bi-rads 0' in text or 'birads zero' in text or 'bi-rads zero' in text)

def birads_1((acc_id, text)):
	return ('birads 1' in text or 'bi-rads 1' in text or 'birads i' in text 
		or 'bi-rads i' in text or 'birads one' in text or 'bi-rads one' in text
		or 'birads category 1' in text or 'bi-rads category 1' in text or 'birads category i' in text 
		or 'bi-rads category i' in text or 'birads category one' in text or 'bi-rads category one' in text)

def birads_2((acc_id, text)):
	return ('birads 2' in text or 'bi-rads 2' in text or 'birads ii' in text 
		or 'bi-rads ii' in text or 'birads two' in text or 'bi-rads two' in text
		or 'birads category 2' in text or 'bi-rads category 2' in text or 'birads category ii' in text 
		or 'bi-rads category ii' in text or 'birads category two' in text or 'bi-rads category two' in text)

def birads_3((acc_id, text)):
	return ('birads 3' in text or 'bi-rads 3' in text or 'birads iii' in text 
		or 'bi-rads iii' in text or 'birads three' in text or 'bi-rads three' in text
		or 'birads category 3' in text or 'bi-rads category 3' in text or 'birads category iii' in text 
		or 'bi-rads category iii' in text or 'birads category three' in text or 'bi-rads category three' in text)

def birads_4((acc_id, text)):
	return ('birads 4' in text or 'bi-rads 4' in text or 'birads iv' in text 
		or 'bi-rads iv' in text or 'birads four' in text or 'bi-rads four' in text
		or 'birads category 4' in text or 'bi-rads category 4' in text or 'birads category iv' in text 
		or 'bi-rads category iv' in text or 'birads category four' in text or 'bi-rads category four' in text)

def birads_5((acc_id, text)):
	return ('birads 5' in text or 'bi-rads 5' in text or 'birads v' in text 
		or 'bi-rads v' in text or 'birads five' in text or 'bi-rads five' in text
		or 'birads category 5' in text or 'bi-rads category 5' in text or 'birads category v' in text 
		or 'bi-rads category v' in text or 'birads category five' in text or 'bi-rads category five' in text)

def birads_6((acc_id, text)):
	return ('birads 6' in text or 'bi-rads 6' in text or 'birads vi' in text 
		or 'bi-rads vi' in text or 'birads six' in text or 'bi-rads six' in text
		or 'birads category 6' in text or 'bi-rads category 6' in text or 'birads category vi' in text 
		or 'bi-rads category vi' in text or 'birads category six' in text or 'bi-rads category six' in text)

def birads_cat((acc_id, text)):
	return ('birads cat' in text or 'bi-rads cat' in text)

def birads_multi((acc_id, text)):
	counter = 0
	counter += 1 if birads_1(text) else 0
	counter += 1 if birads_2(text) else 0
	counter += 1 if birads_3(text) else 0
	counter += 1 if birads_4(text) else 0
	counter += 1 if birads_5(text) else 0
	counter += 1 if birads_6(text) else 0
	return counter > 1

##########################################################################
#	Run the script:

exam_categories = [('mammo', is_mammo)]

mass_categories = [('mass', is_mass)]

birad_categories = [#('multi', birads_multi),
					('birads_5', birads_5),
					('birads_4', birads_4),
					('birads_6', birads_6),
					('birads_0', birads_0),
					('birads_3', birads_3),
					('birads_2', birads_2),
					('birads_1', birads_1)]

def categorize_stanford(filename, categories, out_path=None, other_name='other', dry_run=False):
	if out_path is None and not dry_run:
		print "Error: output path was not specified. Aborting."
		return
	entries = read_file(filename)
	entries = map(lambda x : (x[0], x[1].lower()), entries)
	entries = map(make_categorizer(mass_categories, other_name), entries)
	groups = group_by_key(entries)
	if dry_run:
		count_categories(groups, mass_categories, other_name)
	else:
		write_groups(out_path, groups)
	return

categorize_stanford('../data/mammo_split_by_birads/with_multi/data_birads_5.csv', mass_categories, dry_run=True)