# Contains utility functions for manipulating records

import csv
import os
import sys
import xml.etree.ElementTree as ET

# Returns the
def get_nlp_result(id):
	filename = '../nlp/' + id + '_selen.txt'
	if os.path.isfile(filename):
		return ET.parse(filename).getroot()
	else:
		return None

# Reads the input file
def read_file(input_file):
	results = []

	with open(input_file, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if not row:
				break
			results.append(tuple(row))
	return results

def group_by_key(entries, keyfunc=lambda x : x[0]):
	groups = dict()
	for entry in entries:
		k = keyfunc(entry)
		entry = tuple(filter(lambda x : x != k, entry))
		if k not in groups:
			groups[k] = [entry]
		else:
			groups[k].append(entry)
	return groups

def write_file(filename, entries, quotemode=csv.QUOTE_MINIMAL):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=quotemode)
		for entry in entries:
			writer.writerow(entry)
	print "File written to " + filename

def write_groups(out_path, groups, quotemode=csv.QUOTE_MINIMAL):
	for k, v in groups.iteritems():
		filename = out_path + '/' + k + '.csv'
		write_file(filename, v, quotemode)

def make_categorizer(categories, other_name="other"):
	def categorize(entry):
		for (name, cat_func) in categories:
			if cat_func(entry):
				return (name, ) + entry
		return (other_name, ) + entry
	return categorize

def count_categories(groups, categories, other_name="other"):
	for name, cat_func in (categories + [(other_name, None)]):
		if name in groups:
			print "{}: {}".format(name, len(groups[name]))
		else:
			print name + ": 0"