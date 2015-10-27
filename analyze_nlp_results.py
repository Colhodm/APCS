import xml.dom.minidom
import os
import string
import xml.etree.ElementTree as ET

in_path = '../data/nlp_formatted'
out_path = '../data/nlp_formatted'

has_mass = 0
total = 0
# mass_file = open('has_mass.txt', 'w+')

abnormal_types = {	'AssociatedFinding' : 1,
					'Calcification' : 2,
					'Mass' : 4,
					'SpecialCase' : 8
				}

def process_file(fname):	
	tree = ET.parse(fname)
	root = tree.getroot()
	abnormalities = root.find('Abnormalities')
	if len(abnormalities) == 0:
		return
	else:
		for abnormality in abnormalities:
			abnormal_types.add(abnormality.get('type'))

# Has masses:
process_file(in_path + '/92153_selen.txt')

# Has nothing:
#process_file(in_path + '/3854_selen.txt')

###############################################################

for f in os.listdir(in_path):
	fname = os.path.join(in_path, f)
	if os.path.isfile(fname):
		total += 1
		process_file(fname)

print abnormal_types

# print "{}/{} has mass".format(has_mass, total)

