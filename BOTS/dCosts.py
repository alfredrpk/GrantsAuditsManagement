import sys
import os
from tika import parser
from decimal import Decimal #use for conversion from monetary string to float
import tkinter
os.chdir('..')
os.chdir('pdfs')
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
        location = string.lower().find(substring.lower(), start)
        if location != -1:
            return recurse(locations_found + [location], location+substring_length)
        else:
            return locations_found

    return recurse([], 0)

try:
	inds = locations_of_substring(text, 'Disallowed Cost')
	print(inds[0])
except IndexError as error:
	sys.exit('NO DISALLOWED COST FOUND');


print('POSSIBLE DISALLOWED COST FOUND')
sub = []
num=0

for ind in inds:
	sub.append(text[ind:ind + 140])
	try:
		moneyind = sub[num].index('$')
		temp = sub[num][moneyind:len(text)].split(" ", 1)[0]
		print('HIT: ' + str(temp))
	except ValueError as error:
		print('NO HIT')
	num+=1

tomp = text[inds[0]-500:inds[0]+500]