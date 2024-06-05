import PyPDF2 as pdf
import time

# print(pdf.__version__)

# records = dir(pdf)
# for record in records:
#     print(record)


file = open('Introduction-To-Python.pdf', 'rb')

reader = pdf.PdfReader(file)

info = reader.metadata

# print(info.creator)

# print(len(reader.pages))

# print(reader.pages[3].extract_text)

# print(reader.pages[0].extract_text)

print('No. of pages: ', len(reader.pages))

pages = reader.pages
txt = []
for page in pages:
    
    pass
    # txt.append(page.extract_text())
    # print(page.extract_text())
    # time.sleep(5)

# print(" ".join(txt))
    

def split_pages(file):
    with open(file, 'rb') as f:
        reader = pdf.PdfReader(f)
        pages = reader.pages
        for page , i in zip (pages, range(1, len(pages)+1)):
            writer = pdf.PdfWriter()
            writer.add_page(page)
            with open(f'sample{i}.pdf', 'wb') as out:
                writer.write(out)
                print(f'file {i} created')    

# split_pages('Introduction-To-Python.pdf')
                
def file_upto(file,start = 0,end = 3):
    with open(file, 'rb') as f:
        reader = pdf.PdfReader(f)
        writer = pdf.PdfWriter()
        for page_no in range(start,end):
            page = reader.pages[page_no]
            writer.add_page(page)
        with open(f'sample_{start}_to_{end}.pdf', 'wb' ) as f:
            writer.write(f)  

file_upto('Introduction-To-Python.pdf' ,4, 10)           