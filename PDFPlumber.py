from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys, os
import pdfplumber

pdf_file = "zivkovic, stana.pdf"
pdf = pdfplumber.open(pdf_file)

pages = pdf.pages
print(pages)
page = pdf.pages[0]
text = page.images
print(text)

