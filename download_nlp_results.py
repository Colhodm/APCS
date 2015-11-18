
import csv
import os
from mammo_utils.ibiis_nlp import process_entry

# Reads portions of an entire CSV file from start_row to end_row, inclusive.
def process_file(filename, save_dir, start_row=None, end_row=None):
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

			process_entry(counter, row[0], row[1], 0, save_dir)
			# process_entry(counter, row, 1, output_dir)

	print "\nFile processing done."


#########################################################################

process_file("../data/mammo_split_by_birads/tentative_mass_split/has_mass/birads1_mass.csv", "../nlp")

# process_file("../rnn_test/rnn_out/mammo_small_default_params/temp_1.csv", 
# 	"../rnn_test/rnn_out_nlp/mammo_small_default_params/temp_1")

#########################################################################

# txt = ""

# output = client.service.performSelenBozkurt(txt)

# f = open('output.txt', 'w+')
# f.write(format_xml(output))
# f.close()
