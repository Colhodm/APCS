import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import os, shutil, zipfile

# Webservice URL
base_url = 'http://isis-public.stanford.edu:8085'
path = '/storage/BladderBulk'
dir_url = base_url + path

# Login credentials
username = 'user'
password = 'user'

# Local storage directory
storage_dir = "../images/"

def process_row(tr):
	accession_id = tr.contents[2].string
	dl_link = tr.contents[7].contents[0]['href']
	assert 'delete=yes' not in dl_link
	return (accession_id, dl_link)

def download_all():
	# Perform login
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.open(dir_url, urllib.urlencode({'username' : username, 'password' : password}))

	# Fetch directory listings
	soup = BeautifulSoup(opener.open(dir_url))
	table_rows = soup.find_all(lambda tag: tag.name == 'tr' and tag.parent.name != 'thead')
	image_links = map(process_row, table_rows)

	# Download and extract
	for image_link in image_links:
		if os.path.exists(storage_dir + image_link[0]):
			print "Images with accession id " + image_link[0] + " already exists."
			continue
		else:
			print "Downloading images for accession id " + image_link[0] + "."
			dir_name = storage_dir + image_link[0]
			os.makedirs(dir_name)
			try:
				# Download file
				filestream = opener.open(base_url + image_link[1])
				with open(dir_name + "/images.zip", "wb") as local_file:
					local_file.write(filestream.read())

			except HTTPError, e:
				print "HTTP Error:", e.code, url
			except URLError, e:
				print "URL Error:", e.reason, url

def extract_images(dir_name):
	# Extract file
	zf = zipfile.ZipFile(dir_name + "/images.zip")
	zf.extractall(dir_name)
	zf.close()
	os.remove(dir_name + "/images.zip")

	# Move files to parent directory
	child_folder_name = dir_name + "/" + next(os.walk(dir_name))[1][0]
	files_to_move = os.listdir(child_folder_name)
	for f in files_to_move:
		if os.path.isfile(child_folder_name + "/" + f):
			shutil.move(child_folder_name + "/" + f, dir_name + "/" + f)
	os.rmdir(child_folder_name)

def extract_all():
	for folder in os.listdir(storage_dir):
		if os.path.exists(storage_dir + folder + "/images.zip"):
			print "Extracting images for accession id " + folder + "."
			extract_images(storage_dir + folder)
		print "Finished extracting images."

# Run script
download_all()
#extract_all()
