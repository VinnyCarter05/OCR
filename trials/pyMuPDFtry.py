import fitz

pdf_document = 'Faxes\FANI_GHASEM_MRISPINC_20201208.PDF'
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")
print(page1text)