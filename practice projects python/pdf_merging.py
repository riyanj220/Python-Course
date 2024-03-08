import PyPDF2

pdf1 = open("sample1.pdf", "rb")
pdf2 = open("sample2.pdf", "rb")


reader1 = PyPDF2.PdfReader(pdf1)
reader2 = PyPDF2.PdfReader(pdf2)

writer = PyPDF2.PdfWriter()

for page_num in range(len(reader1.pages)):
    page = reader1.pages[page_num]
    writer.add_page(page)

for page_num in range(len(reader2.pages)):
    page = reader2.pages[page_num]
    writer.add_page(page)

merged_pdf = open("merged.pdf", "wb")

writer.write(merged_pdf)

pdf1.close()
pdf2.close()
merged_pdf.close()
