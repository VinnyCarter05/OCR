import os
import datetime



def listdir_with_ext (path="", ext = ".*"):
    PDFlist = []
    for file in os.listdir(path):
        if file.lower().endswith(ext):
            PDFlist.append([file, os.path.getmtime(os.path.join(path,file))])
    return sorted_list_by_col (PDFlist, 0)

def sorted_list_by_col (lst, col, reverse = False):
    sorted_list = sorted(lst, key = lambda x: x[col], reverse = reverse)
    return (sorted_list)

if __name__=="__main__":
    path = "faxes"
    PDFlist = listdir_with_ext(path, ".pdf")
    # 
    for file, date in PDFlist:
        print (file,datetime.datetime.fromtimestamp(date))