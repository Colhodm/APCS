from mammo_utils.utils import *
import xml.etree.ElementTree as ET
import csv
import re
import datetime

def get_date(text):
	def parse_numeric(date_string):
		fields = re.split('[-|\/]', date_string)
		month = fields[0]
		date = fields[1]
		year = fields[2]
		if (len(year)) == 2:
			year = '19' + year if year[0] == '9' else '20' + year
		return datetime.datetime.strptime("{} {} {}".format(month, date, year), "%m %d %Y")

	def parse_month(date_string):
		date_string = date_string.replace(',', ' ')
		date_start = re.search("\d", date_string).start()
		month = date_string[ : date_start].strip()[:3]
		year_start = re.search(" \d", date_string[date_start:]).start() + date_start
		date = date_string[date_start : year_start].strip()
		year = date_string[year_start : ].strip()
		if (len(year)) == 2:
			year = '19' + year if year[0] == '9' else '20' + year
		return datetime.datetime.strptime("{} {} {}".format(month, date, year), "%b %d %Y")

	# Found on the Internet...hope it works well
	date_regex = "((0?[13578]|10|12)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[01]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1}))|(0?[2469]|11)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[0]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1})))"
	date_regex2 = "(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|(nov|dec)(?:ember)?) ?(([1-9])|(0[1-9])|([12])([0-9]?)|(3[01]?))[,| ] ?((19[7-9]\d|20\d{2})|\d{2})"
	m1 = re.search(date_regex, text)
	m2 = re.search(date_regex2, text)

	if m1 is not None and m2 is not None:
		if m2.start() < m1.start():
			return parse_month(m2.group())
		else:
			return parse_numeric(m1.group())
	elif m1 is not None:
		return parse_numeric(m1.group())
	elif m2 is not None:
		return parse_month(m2.group())
	else:
		return datetime.datetime.min

def extract_date((acc_id, text)):
	lowertext = text.lower()
	date = get_date(lowertext)
	return (date, acc_id, text)

entries = read_file("../data/birads.csv")
entries = map(extract_date, entries)
entries.sort(key=lambda x : x[0])
write_file("../data/birads_sorted.csv", map(lambda x: (x[1], x[2]), entries))