# Converts the output of Selen's NLP code to structured fields that can be used for prediction.
# The following categories will be extracted:
#   BreastDensity:  ???
#   MassesMargins:  Circumscribed, Illdefined, CannotDiscern, Spiculated, Microlobulated
#   MassesShape:    Oval, Round, Irregular, Lobular, CannotDiscern
#   MassesDensity:  Equal, CannotDiscern, High, Low, Fatdensity
#   MassesSize:     Small, Large
#   BIRADS_category: 0-5

from mammo_utils.utils import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

total_types = { 'BreastDensity' : set(), 'MassesMargins' : set(), 'MassesShape' : set(), 'MassesDensity' : set() }

breast_density_map = { 'Almost_Entirely_Fat' : 'Class1', 
                       'Scattered_Fibroglandular_Densities' : 'Class2',
                       'Heterogeneously_Dense' : 'Class3',
                       'Extremely_Dense' : 'Class4',
                       'Not_Specified' : '*' }
mass_margin_map = { 'Circumscribed' : 'Circumscribed', 
                     'Ill_Defined' : 'Illdefined',
                     'Spiculated' : 'Spiculated',
                     'Microlobulated' : 'Microlobulated', 
                     'Obscured' : 'CannotDiscern',
                     'Indistinct' : 'CannotDiscern' }
mass_shape_map = { 'Oval' : 'Oval', 'Lobular' : 'Lobular', 'Irregular' : 'Irregular' }
mass_density_map = { 'High' : 'High', 'Equal' : 'Equal', 'Fat_Containing' : 'Fatdensity', 'Low' : 'Low' }


class EntryData:
    def __init__(self):
        self.breast_density = '*'
        self.mass_margins = { '*' : 1 }
        self.mass_shape = { '*' : 1 }
        self.mass_density = { '*' : 1 }
        self.mass_size = []
        self.birads_cat = '*'

    def _add(self, collection, value):
        if '*' in collection:
            del collection['*']
        
        if value in collection:
            collection[value] += 1
        else:
            collection[value] = 1

    def _get(self, collection):
        item = None
        count = 0
        for k, v in collection.iteritems():
            if v > count:
                item = k
                count = v
        return item

    def add_breast_density(self, value):
        self.breast_density = breast_density_map[value]

    def add_mass_margin(self, value):
        v = mass_margin_map[value]
        self._add(self.mass_margins, v)

    def add_mass_shape(self, value):
        v = mass_shape_map[value]
        self._add(self.mass_shape, v)

    def add_mass_density(self, value):
        v = mass_density_map[value]
        self._add(self.mass_density, v)

    def add_mass_size(self, value):
        self.mass_size.append(value)

    def get_breast_density(self):
        return self.breast_density

    def get_mass_margin(self):
        return self._get(self.mass_margins)

    def get_mass_shape(self):
        return self._get(self.mass_shape)

    def get_mass_density(self):
        return self._get(self.mass_density)

    def get_mass_size(self):
        return self.mass_size

# Gets 
def extract_birads(text):
	text = text[:60].lower()
	if 'incomplete' in text:
		return '0'
	elif 'highly suggestive of malignancy' in text:
		return '5'
	elif 'suspicious of malignancy' in text:
		return '4'
	elif 'probably benign mammogram' in text:
		return '3'
	elif 'benign mammogram' in text:
		return '2'
	elif 'negative mammogram' in text:
		return '1'
	else:
		return '*'

# Currently just gets latest entry if fields repeat
def extract_fields(types, name):
#    xml = get_nlp_result_arjun('../mcw_nlp/', name)
    xml = get_nlp_result_arjun('../mcw_nlp/', 1)
    if xml is None:
        print "No file found"
        return None
    print "file found"
    # Get breast density
    entry = EntryData()
    if xml.attrib['breastDensity'] is not None:
        entry.add_breast_density(xml.attrib['breastDensity'])

    # Get BIRADS value
    text = xml.find('Text')
    if text is not None:
    	entry.birads_cat = extract_birads(text.attrib['value'])

    abnormalities = xml.findall('Abnormalities/Abnormality')
    for abnormality in abnormalities:
        if abnormality.attrib['type'] == 'Mass':
            for child in abnormality:
                if child.attrib['type'] == 'Shape':
                    entry.add_mass_shape(child.attrib['value'])
                if child.attrib['type'] == 'Margin':
                    entry.add_mass_margin(child.attrib['value'])
                if child.attrib['type'] == 'Density':
                    entry.add_mass_density(child.attrib['value'])
                if child.tag == 'Size':
                    try:
                        size = float(child.attrib['value'])
                    except:
                        continue

                    if child.attrib['type'] == 'cm' or child.attrib['type'] == 'CM':
                        size *= 10
                    elif child.attrib['type'] != 'mm' and child.attrib['type'] != 'MM':
                        print "Size not 'cm' or 'mm', but " + child.attrib['type']
                    entry.add_mass_size(size)
    return entry

def check_match(extracted_val, correct_val, counters):  
    if extracted_val == correct_val:
        counters[0] += 1
    elif extracted_val == '*':
        counters[1] += 1
    else:
        counters[2] += 1

stats = { 'BreastDensity' : [0, 0, 0],
          'MassesMargins' : [0, 0, 0],
          'MassesShape'   : [0, 0, 0],
          'MassesDensity' : [0, 0, 0],
          'BIRADS_category' : [0, 0, 0] }
mass_smalls = []
mass_large = []
counter = 0

def process_entry(entry):
    global counter, stats, mass_smalls, mass_large
    counter += 1
    if counter % 100 == 0:
        print counter
    print entry[counter] 
    extracted = extract_fields(total_types, entry[0])
    if extracted is not None:
        breast_density = entry[2]
        mass_margins = entry[6]
        mass_shape = entry[5]
        mass_density = entry[7]
        mass_size = entry[8]
        birads_cat = entry[40]

        # check_match(extracted.get_breast_density(), breast_density, stats['BreastDensity'])
        # check_match(extracted.get_mass_margin(), mass_margins, stats['MassesMargins'])
        # check_match(extracted.get_mass_shape(), mass_shape, stats['MassesShape'])
        # check_match(extracted.get_mass_density(), mass_density, stats['MassesDensity'])
        #check_match(extracted.birads_cat, birads_cat, stats['BIRADS_category'])

        #if mass_size == 'Small':
        #    mass_smalls += extracted.get_mass_size()
        #elif mass_size == 'Large':
        #    mass_large += extracted.get_mass_size()

def generate_output(entry):
    global counter
    counter += 1
    if counter % 100 == 0:
        print counter
    out = extract_fields(total_types, entry[0])
    if out is None:
        return None
    else:
        result = entry[39]
        return (out.get_breast_density(), out.get_mass_margin(), out.get_mass_shape(), out.get_mass_density(), out.birads_cat, result)


input_name =('/home/arjun/mammo_reports/mcw_nlp/1_selen.txt')
results = read_file(input_name)
map(process_entry, results)
outputs = filter(lambda x: x is not None, map(generate_output, results))
write_file('../env/practicedata/train_0_parsed.csv', outputs)

# plt.hist(mass_smalls, bins=np.arange(min(mass_smalls), max(mass_smalls) + 1, 1), facecolor='red', alpha=0.5)
# plt.hist(mass_large, bins=np.arange(min(mass_large), max(mass_large) + 1, 1), facecolor='blue', alpha=0.5)
# plt.show()

#print stats
