import csv
import random

#inputs = list of files
def random_concatenate(inputs, out_fname, n):
	entries = []

	# Generate list of all accession_ids
	for i in range(len(inputs)):
		fname = inputs[i]
		idx = fname.rfind('/')
		if not idx == -1:
			fname = fname[idx + 1 : ]

		with open(inputs[i], 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if not row:
					break
				entries.append((row[0], row[1], i))

	out_file = open(out_fname, 'w+')

	# Shuffle accession IDs
	random.shuffle(entries)
	count = 0

	# Write results
	for acc_id, text, src_idx in entries:
		if count >= n:
			break
		count += 1
		out_file.write('\"{}\",\"{}\"\n'.format(acc_id, text.replace('\"', '\"\"')))

	out_file.close()

	print "Done."

out_prefix = '../rnn_test/rnn_input/'

random_concatenate(['../data/split_by_method/data_mammo.csv'], out_prefix + 'mammo_5k/input.txt', 5000)
