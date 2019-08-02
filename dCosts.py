import sys
import os
from tika import parser
os.chdir('C:/Users/Alfred/Downloads/pdfs')
try:
	filename = sys.argv[1]
except IndexError as error:
	#sys.exit('ENTER A PDF NAME');
	filename = input('ENTER A PDF NAME: ')
raw = parser.from_file(filename + '.pdf')
text = raw['content']

def locations_of_substring(string, substring):
    """Return a list of locations of a substring."""

    substring_length = len(substring)    
    def recurse(locations_found, start):
        location = string.find(substring, start)
        if location != -1:
            return recurse(locations_found + [location], location+substring_length)
        else:
            return locations_found

    return recurse([], 0)

try:
	inds = locations_of_substring(text, 'Disallowed Cost')
except ValueError as error:
	sys.exit('NO DISALLOWED COST FOUND');


print('POSSIBLE DISALLOWED COST FOUND')

for ind in inds:
	sub = text[ind:ind + 90]
	try:
		moneyind = sub.index('$')
		print('HIT')
	except ValueError as error:
		print('NO HIT')