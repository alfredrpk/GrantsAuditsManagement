import sys

try:
	zip_file_url = 'https://www2.census.gov/pub/outgoing/govs/singleaudit//allfac'+sys.argv[1]+'.zip'
except IndexError as error:
	zip_file_url = 'https://www2.census.gov/pub/outgoing/govs/singleaudit//allfac18.zip'

import os
import requests, zipfile, io, time
start = time.time()
r = requests.get(zip_file_url)
print(time.time()-start)
z = zipfile.ZipFile(io.BytesIO(r.content))
print(time.time()-start)
os.chdir('../Download Files/')
z.extractall(os.getcwd())
print(time.time()-start)

try:
	print('Extracted data from year ' + sys.argv[1])
except IndexError as error:
	print('Extracted data from year 18 as default')