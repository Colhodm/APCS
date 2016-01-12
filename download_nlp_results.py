# Sends the entries of an entire file to the IBIIS NLP service. The code will skip files that already have
# been processed.

import csv
import os
from mammo_utils.ibiis_nlp import process_entry

# The following four functions extract the accession ID and data from the Stanford and MCW datasets.
def get_stanford_name(row):
    return row[0]

def get_stanford_data(row):
    return row[1]

def get_mcw_name(row):
    return row[0]

def get_mcw_data(row):
    return row[41] + " " + row[42]

# Reads portions of an entire CSV file from start_row to end_row, inclusive.
def process_file(filename, save_dir, start_row=None, end_row=None, name_func=get_stanford_name, data_func=get_stanford_data):
    print "Processing entries {} to {}".format(start_row if start_row else 'start', 
        end_row if end_row else 'end')

    if os.path.exists(save_dir + '/failed.txt'):
        os.remove(save_dir + '/failed.txt')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(filename, 'r') as csvfile:
        counter = 0
        reader = csv.reader(csvfile)

        for row in reader:
            counter += 1

            if row == []:
                break
            elif end_row and counter > end_row:
                break
            elif start_row and counter < start_row:
                continue

            process_entry(counter, name_func(row), data_func(row), 0, save_dir)

    print "\nFile processing done."


#########################################################################

process_file("../mcw_data/splits/train_0.csv", "../mcw_nlp", name_func=get_mcw_name, data_func=get_mcw_data)

