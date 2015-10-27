from suds.client import Client
import csv
import os
import sys
import xml.dom.minidom

url = 'http://isis-collaborator.stanford.edu:8085/NLP/WebServices/Stanford_IBIIS_NLP.asmx?WSDL'

client = Client(url, timeout=300)

def format_xml(xml_text):
	return xml.dom.minidom.parseString(xml_text).toprettyxml()

# mode = 0 for Selen, mode = 1 for Hakan
def process_entry(row_num, row_contents, mode, output_dir):
	suffix = '_hakan.txt' if mode == 1 else '_selen.txt'

	sys.stdout.flush()
	sys.stdout.write("\rEntry {} ({})".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
	if os.path.exists(output_dir + '/' + row_contents[0] + suffix):
		sys.stdout.write(" skipped")
		return

	try:
		text = row_contents[1].decode('ascii', errors='ignore')
		if mode == 1:
			output = client.service.performHakanBulu(text)
		else:
			output = client.service.performSelenBozkurt(text)
		formatted_out = format_xml(output)

		out_file = open(output_dir + '/' + row_contents[0] + suffix, 'w+')
		out_file.write(formatted_out)
		out_file.close()
		return True
	except:
		print "Entry #{} ({}) failed.".format(row_num, 'Hakan' if mode == 1 else 'Selen')
		err_file = open(output_dir + '/failed.txt', 'a+')
		err_file.write("{} ({})\n".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
		err_file.close()
		return False

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

			process_entry(counter, row, 0, save_dir)
			# process_entry(counter, row, 1, output_dir)

	print "\nFile processing done."

#########################################################################

# process_file("../data/mammo_split_by_birads/no_multi/data_birads_0.csv", "../nlp")


#########################################################################

# txt = ""

# output = client.service.performSelenBozkurt(txt)

# f = open('output.txt', 'w+')
# f.write(format_xml(output))
# f.close()
