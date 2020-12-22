import PyPDF2
pdf_file = open('Faxes\OU_WAIHAR_HOLTSU14D_20201104.PDF', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content.encode('utf-8'))