import os
from tika import parser
os.chdir('C:/Users/Alfred/Downloads/pdfs')
num = 1

for filename in os.listdir('C:/Users/Alfred/Downloads/pdfs'):
	if filename.endswith('.pdf'):
		raw = parser.from_file(filename)
		page_content = raw['content']
		f = open('combinedPDF.txt', 'a', encoding='utf-8')
		f.write(page_content)
		f.write("PDF " + str(num))
		print(num)
		num += 1

f.close()
