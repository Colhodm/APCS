# Given a CSV of (Accession #, Text) and NLP outputs determines which entries have masses.
from ibiis_nlp_webservice import process_entry
import csv
import random
import xml.etree.ElementTree as ET

def nlp_result_has_mass(file_path):
	root = ET.parse(file_path).getroot()
	abnormalities = root.find('Abnormalities')
	for abnormality in abnormalities:
		if abnormality.get('type') == 'Mass':
			return True
	return False

def select_all_masses(input_file, nlp_path, mass_file_path, no_mass_file_path):
	with open(input_file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		mass_file = open(mass_file_path, 'a+')
		no_mass_file = open(no_mass_file_path, 'a+')

		for row in reader:
			if not row:
				break

			if nlp_result_has_mass(nlp_path + '/' + row[0] + '_selen.txt'):
				mass_file.write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))
			else:
				no_mass_file.write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))

		mass_file.close()
		no_mass_file.close()

def random_select_n(inputs, nlp_path, mass_file_dir, no_mass_file_dir, n):
	entries = []
	mass_files, no_mass_files = [], []

	# Generate list of all accession_ids
	for i in range(len(inputs)):
		fname = inputs[i]
		idx = fname.rfind('/')
		if not idx == -1:
			fname = fname[idx + 1 : ]
		mass_files.append(open(mass_file_dir + '/' + fname, 'a+'))
		no_mass_files.append(open(no_mass_file_dir + '/' + fname, 'a+'))

		with open(inputs[i], 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if not row:
					break
				entries.append((row[0], row[1], i))

	# Shuffle accession IDs
	random.shuffle(entries)
	mass_count = 0
	tot_count = 0

	print "Extracting {} masses from a total of {} entries".format(n, len(entries))

	# Write results
	for acc_id, text, src_idx in entries:
		if mass_count >= n:
			break
		tot_count += 1

		if process_entry(tot_count, acc_id, text, 0, nlp_path):
			if nlp_result_has_mass(nlp_path + '/' + acc_id + '_selen.txt'):
				mass_count += 1
				mass_files[src_idx].write('\"{}\",\"{}\"\n'.format(acc_id, text.replace('\"', '\"\"')))
			else:
				no_mass_files[src_idx].write('\"{}\",\"{}\"\n'.format(acc_id, text.replace('\"', '\"\"')))
		else:
			pass

	for f in mass_files:
		f.close()
	for f in no_mass_files:
		f.close()

	print "Masses: {} / {} entries".format(mass_count, tot_count)


#################################################################################

# select_all_masses('../data/mammo_split_by_birads/no_multi/data_birads_4_notdone.csv', 
# 	'../nlp', 
# 	'G:/data/birads_nm_split_by_mass/has_mass/birads_4.csv',
# 	'G:/data/birads_nm_split_by_mass/no_mass/birads_4.csv')

masses = ['G:/data/mammo_split_by_birads/tentative_mass_split/has_mass/birads1_mass.csv',
          'G:/data/mammo_split_by_birads/tentative_mass_split/has_mass/birads2_mass.csv',
          'G:/data/mammo_split_by_birads/tentative_mass_split/has_mass/birads3_mass.csv']

random_select_n(masses, 'G:/nlp', 'G:/data/birads_nm_split_by_mass/has_mass', 'G:/data/birads_nm_split_by_mass/no_mass', 1250)
