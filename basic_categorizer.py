# Script to perform basic filtering on a CSV of (Accession #, Text) entries.

import csv
import sys
import string

# Performs file categorization.
# categories: a list of (<category name>, <categorizer function>) tuples
# dry_run: if set to true, displays how many entries would fall into each category,
#	but does not actually perform categorization
def categorize_file(input_file, out_path, categories, dry_run=False):
	if dry_run:
		counts = [0] * (len(categories) + 1)
	else:
		out_files = []
		for cat in categories:
			out_files.append(open('{}/data_{}.csv'.format(out_path, cat[0]), 'w+'))
		out_files.append(open('{}/data_other.csv'.format(out_path), 'w+'))

	with open(input_file, 'r') as csvfile:
		counter = 0
		reader = csv.reader(csvfile)

		for row in reader:
			if not row:
				break
			counter += 1
			# if counter % 1000 == 0:
			# 	sys.stdout.write("\rEntry {}".format(counter))
			# 	sys.stdout.flush()

			# Performs categorization
			has_cat = False
			for i in range(len(categories)):
				if categories[i][1](row[1].lower()):
					if dry_run:
						counts[i] += 1
					else:
						out_files[i].write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))
					has_cat = True
					break

			# Entry falls into the "other" category
			if not has_cat:
				if dry_run:
					counts[-1] += 1
				else:
					out_files[-1].write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))

	if dry_run:
		for i in range(len(categories)):
			print "{}: {}".format(categories[i][0], counts[i])
		print "Other: {}".format(counts[-1])
	else:
		for f in out_files:
			f.close()
		print "\nDone."

##########################################################################
#	Define categories here:

#-----------------------------
# Exam type categories:
#-----------------------------

def is_mammo(text):
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

def is_mass(text):
	# words = text.split(' ')
	# indices = [i for i, x in enumerate(words) if x == 'mass']
	# if len(indices) == 0:
	# 	return False
	# for i in indices:
	# 	if 'no' in words[max(0, i - 4) : i - 1]:
	# 		return False
	# return True
	return 'mass' in text

#-----------------------------
# BI-RADS categories:
#-----------------------------

def birads_0(text):
	return ('birads 0' in text or 'bi-rads 0' in text or 'birads zero' in text or 'bi-rads zero' in text)

def birads_1(text):
	return ('birads 1' in text or 'bi-rads 1' in text or 'birads i' in text 
		or 'bi-rads i' in text or 'birads one' in text or 'bi-rads one' in text
		or 'birads category 1' in text or 'bi-rads category 1' in text or 'birads category i' in text 
		or 'bi-rads category i' in text or 'birads category one' in text or 'bi-rads category one' in text)

def birads_2(text):
	return ('birads 2' in text or 'bi-rads 2' in text or 'birads ii' in text 
		or 'bi-rads ii' in text or 'birads two' in text or 'bi-rads two' in text
		or 'birads category 2' in text or 'bi-rads category 2' in text or 'birads category ii' in text 
		or 'bi-rads category ii' in text or 'birads category two' in text or 'bi-rads category two' in text)

def birads_3(text):
	return ('birads 3' in text or 'bi-rads 3' in text or 'birads iii' in text 
		or 'bi-rads iii' in text or 'birads three' in text or 'bi-rads three' in text
		or 'birads category 3' in text or 'bi-rads category 3' in text or 'birads category iii' in text 
		or 'bi-rads category iii' in text or 'birads category three' in text or 'bi-rads category three' in text)

def birads_4(text):
	return ('birads 4' in text or 'bi-rads 4' in text or 'birads iv' in text 
		or 'bi-rads iv' in text or 'birads four' in text or 'bi-rads four' in text
		or 'birads category 4' in text or 'bi-rads category 4' in text or 'birads category iv' in text 
		or 'bi-rads category iv' in text or 'birads category four' in text or 'bi-rads category four' in text)

def birads_5(text):
	return ('birads 5' in text or 'bi-rads 5' in text or 'birads v' in text 
		or 'bi-rads v' in text or 'birads five' in text or 'bi-rads five' in text
		or 'birads category 5' in text or 'bi-rads category 5' in text or 'birads category v' in text 
		or 'bi-rads category v' in text or 'birads category five' in text or 'bi-rads category five' in text)

def birads_6(text):
	return ('birads 6' in text or 'bi-rads 6' in text or 'birads vi' in text 
		or 'bi-rads vi' in text or 'birads six' in text or 'bi-rads six' in text
		or 'birads category 6' in text or 'bi-rads category 6' in text or 'birads category vi' in text 
		or 'bi-rads category vi' in text or 'birads category six' in text or 'bi-rads category six' in text)

def birads_cat(text):
	return ('birads cat' in text or 'bi-rads cat' in text)

def birads_multi(text):
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

input_file = '../data/categorized/data_mammo.csv'
output_path = '../data/categorized/birads'

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

#categorize_file('../data/categorized/data_mammo.csv', output_path, birad_categories)

#categorize_file('../data/birads_nm_split_by_mass/has_mass/birads_4.csv', None, mass_categories, dry_run=True)

categorize_file('../data/mammo_split_by_birads/no_multi/data_birads_0.csv', 
	'../data/mammo_split_by_birads/tentative_mass_split', mass_categories)