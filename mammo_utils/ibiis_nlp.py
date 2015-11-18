from suds.client import Client
import os
import sys
import xml.dom.minidom

url = 'http://isis-collaborator.stanford.edu:8085/NLP/WebServices/Stanford_IBIIS_NLP.asmx?WSDL'

client = Client(url, timeout=300)

def format_xml(xml_text):
	return xml.dom.minidom.parseString(xml_text).toprettyxml()

# mode = 0 for Selen, mode = 1 for Hakan
def process_entry(row_num, acc_id, text, mode, output_dir):
	suffix = '_hakan.txt' if mode == 1 else '_selen.txt'

	sys.stdout.flush()
	if os.path.exists(output_dir + '/' + acc_id + suffix):
		sys.stdout.write("\rEntry {} ({}) SK".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
		return
	else:
		sys.stdout.write("\rEntry {} ({}) IP".format(row_num, 'Hakan' if mode == 1 else 'Selen'))

	try:
		text = text.decode('ascii', errors='ignore')
		if mode == 1:
			output = client.service.performHakanBulu(text)
		else:
			output = client.service.performSelenBozkurt(text)
		formatted_out = format_xml(output)

		out_file = open(output_dir + '/' + acc_id + suffix, 'w+')
		out_file.write(formatted_out)
		out_file.close()
		return True
	except:
		print "Entry #{} ({}) failed.".format(row_num, 'Hakan' if mode == 1 else 'Selen')
		err_file = open(output_dir + '/failed.txt', 'a+')
		err_file.write("{} ({})\n".format(row_num, 'Hakan' if mode == 1 else 'Selen'))
		err_file.close()
		return False
		