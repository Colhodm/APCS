# Script to perform basic filtering on a CSV of (Accession #, Text) entries.

import csv
import sys
import string

def process_file(input_file, out_path, categories):
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
			if counter % 1000 == 0:
				sys.stdout.write("\rEntry {}".format(counter))
				sys.stdout.flush()

			has_cat = False
			for i in range(len(categories)):
				if categories[i][1](row[1]):
					out_files[i].write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))
					has_cat = True
					break
			if not has_cat:
				out_files[-1].write('\"{}\",\"{}\"\n'.format(row[0], row[1].replace('\"', '\"\"')))

	for f in out_files:
		f.close()
	print "\nDone."

##########################################################################
#	Define categories here:

def is_mammo(text):
	text = text.lower()
	words = text.split(' ')
	first_2 = ' '.join(words[:2])
	first_25 = ' '.join(words[:25])
	if 'i have' in first_2 or 'please see' in first_2 or 'dear doctor' in first_2 or 'addendum' in first_2:
		return False
	elif 'mammo' in first_25:
		return True
	else:
		try:
			idx = words.index('impression:')
			impression_str = ' '.join(words[idx + 1 : idx + 6])
			return 'mammo' in impresson_str
		except:
			return False

categories = [('mammo', is_mammo)]

##########################################################################
#	Run the script:

input_file = '../data/raw/stanford_mammo.csv'
output_path = '../data/categorized'

process_file(input_file, output_path, categories)