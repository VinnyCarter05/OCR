import os
import datetime

path = "faxes"
PDFlist = []
for file in os.listdir(path):
    if file.lower().endswith(".pdf"):
        PDFlist.append([file, os.path.getmtime(os.path.join(path,file))])
    # if file.endswith(".txt"):
    #     print(os.path.join("/mydir", file))
for file, date in PDFlist:
    print (file,datetime.datetime.fromtimestamp(date))