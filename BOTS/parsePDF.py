import os
from tika import parser
os.chdir('C:/Users/Alfred/Downloads/pdfs')
save_path = 'C:/Users/Alfred/Downloads/pdfs/pdftxtfiles'
num = 1
for filename in os.listdir('C:/Users/Alfred/Downloads/pdfs'):
	if filename.endswith('.pdf'):
		complete_name = os.path.join(save_path, 'pdftxt' + str(num) + '.txt')
		raw = parser.from_file(filename)
		page_content = raw['content']
		f = open(complete_name, 'w', encoding='utf-8')
		f.write(page_content)
		print(num)
		num += 1
f.close()
