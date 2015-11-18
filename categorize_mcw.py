#!/usr/env/python

from mammo_utils.utils import *

birad_categories = [('birads_5', lambda entry : entry[40] == '5'),
                    ('birads_4', lambda entry : entry[40] == '4'),
                    ('birads_0', lambda entry : entry[40] == '0'),
                    ('birads_3', lambda entry : entry[40] == '3'),
                    ('birads_2', lambda entry : entry[40] == '2'),
                    ('birads_1', lambda entry : entry[40] == '1')]

def has_cat_fn(entry):
    birad = entry[40]
    return birad == '5' or birad == '4' or birad == '3' or birad == '2' or birad == '1' or birad == '0'

has_cat = [('has_cat', has_cat_fn)]

def categorize(filename, categories, out_path=None, other_name='other', dry_run=False):
    if out_path is None and not dry_run:
        print "Error: output path was not specified. Aborting."
        return
    entries = read_file(filename)
    entries = map(make_categorizer(categories, other_name), entries)
    groups = group_by_key(entries)
    if dry_run:
        count_categories(groups, categories, other_name)
    else:
        write_groups(out_path, groups)

categorize('../mcw_data/MCW_Radiology09_Reports.csv', has_cat, out_path='../mcw_data/birads')

