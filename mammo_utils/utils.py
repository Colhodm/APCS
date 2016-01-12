# Contains utility functions for manipulating mammo entries in bulk.

import csv
import os
import sys
import random
import xml.etree.ElementTree as ET

# Returns the result of the IBIIS webservice as .
def get_nlp_result(id):
    filename = '../nlp/' + id + '_selen.txt'
    if os.path.isfile(filename):
        return ET.parse(filename).getroot()
    else:
        return None

# Reads the input file and returns a list of entries. Each entry is a tuple, with 
# each field of the tuple corresponding to a column in the original CSV file.
def read_file(input_file):
    results = []

    with open(input_file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                break
            results.append(tuple(row))
    return results

# Transforms a list of entries into a dictionary of lists. The keyfunc specifies
# which keys the dictionary uses.
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

# Writes a list of entries to CSV format.
def write_file(filename, entries, quotemode=csv.QUOTE_MINIMAL):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=quotemode)
        for entry in entries:
            writer.writerow(entry)
    print "File written to " + filename

# Writes a dictionary of lists into CSV format. Each list is written into a separate
# CSV file.
def write_groups(out_path, groups, quotemode=csv.QUOTE_MINIMAL):
    for k, v in groups.iteritems():
        filename = "{}/{}.csv".format(out_path, k)
        write_file(filename, v, quotemode)

# Shuffles a list of entries randomly and splits the list based on the fractions
# specified by the splits array.
def random_split(entries, splits):
    num_entries = len(entries)
    norm = float(reduce(lambda x, y: x + y, splits))
    random.shuffle(entries)
    start, end = 0, 0
    groups = dict()
    for i in range(len(splits)):
        end += int(round(splits[i] * num_entries / norm, 0))
        groups[i] = entries[start : end]
        start = end
    groups[i] += entries[end : ]
    return groups

# Creates a function to categorize each entry in a list of entries. categories should
# be a list of typles of the format (name, cat_func), where name is a string containing
# the name of the category and cat_func is a function that takes in an entry and returns
# True or False depending on whether the the entry belongs in the category. Each entry
# is sorted into the first category that returns true. other_name is the name of the category
# an entry is sorted to if none of the categorizer functions return true.
def make_categorizer(categories, other_name="other"):
    def categorize(entry):
        for (name, cat_func) in categories:
            if cat_func(entry):
                return (name, ) + entry
        return (other_name, ) + entry
    return categorize

# Given a dictionary of categories, prints out the count of each list of entries.
def count_categories(groups, categories, other_name="other"):
    for name, cat_func in (categories + [(other_name, None)]):
        if name in groups:
            print "{}: {}".format(name, len(groups[name]))
        else:
            print name + ": 0"
