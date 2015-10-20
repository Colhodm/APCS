from suds.client import Client
import csv
import os
import sys

url = 'http://isis-collaborator.stanford.edu:8085/NLP/WebServices/Stanford_IBIIS_NLP.asmx?WSDL'

client = Client(url)

# mode = 0 for Selen, mode = 1 for Hakan
def process_entry(row_num, row_contents, mode, output_dir):
	sys.stdout.write("\rEntry {} ({})".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
	sys.stdout.flush()

	try:
		if mode == 1:
			output = client.service.performHakanBulu(row_contents[1])
		else:
			output = client.service.performSelenBozkurt(row_contents[1])

		suffix = '_hakan.txt' if mode == 1 else '_selen.txt'
		out_file = open(output_dir + '/' + row_contents[0] + suffix, 'w+')
		out_file.write(output)
		out_file.close()
	except:
		print "Entry #{} ({}) failed.".format(row_num, 'Hakan' if mode == 1 else 'Selen')
		err_file = open(ouput_dir + '/failed.txt', 'a+')
		err_file.write("{} ({})".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
		err_file.close()

# Reads portions of an entire CSV file from start_row to end_row, inclusive.
def process_file(filename, save_dir, start_row=None, end_row=None):
	print "Processing entries {} to {}".format(start_row if start_row else 'start', 
		end_row if end_row else 'end')

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

			# output_dir = save_dir + '/' + row[0]
			# if not os.path.exists(output_dir):
			# 	os.mkdir(output_dir)
			
			process_entry(counter, row, 0, save_dir)
			# process_entry(counter, row, 1, output_dir)

	print "\nFile processing done."

#########################################################################

process_file("../data/categorized/data_mammo.csv", "../data/nlp", start_row=2, end_row=10000)

