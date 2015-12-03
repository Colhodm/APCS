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
    return groups

def make_splits(in_fname, out_dir, splits):
    print "Categorizing raw data:"
    birad_groups = categorize(in_fname, birad_categories, dry_run=True)
    output = dict()
    for birad, birad_entries in birad_groups.items():
        split_groups = random_split(birad_entries, splits)
        for s, split_entries in split_groups.items():
            if s in output:
                output[s] += split_entries
            else:
                output[s] = split_entries
    for k, v in output.items():
        random.shuffle(v)
       
    write_groups(out_dir, output)
    for i in range(len(output)):
        print "Categorizing split {}:".format(i)
        categorize('{}/{}.csv'.format(out_dir, i), birad_categories, dry_run=True)

categorize('../../mammo_report_rnn/rnn_output/mcw_20k_3x1000_lr0.0001/sample_t0.5.txt', birad_categories, dry_run=True)

