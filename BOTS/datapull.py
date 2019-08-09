# import urllib.request

# print('finna download this bih')

# url = 'https://www2.census.gov/pub/outgoing/govs/singleaudit//allfac.zip';
# urllib.request.urlretrieve(url)

zip_file_url = 'https://www2.census.gov/pub/outgoing/govs/singleaudit//allfac18.zip'
import os
import requests, zipfile, io, time
start = time.time()
r = requests.get(zip_file_url)
print(time.time()-start)
z = zipfile.ZipFile(io.BytesIO(r.content))
print(time.time()-start)
#z.extractall(os.path.join(os.getcwd(), '/data'))
z.extractall()
print(time.time()-start)