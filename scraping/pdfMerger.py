import os
from PyPDF2 import PdfWriter
# from pypdf import  PdfMerger
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith('.pdf')]

for file in files:
    merger.append(file)

merger.write('final.pdf')
merger.close()


# import os
# files = os.listdir('PDF')
# i = 1
# for file in files:
#     file = os.rename(f'PDF/{file}',f'PDF/level{i}.pdf')
#     print(file)
#     i = i+1