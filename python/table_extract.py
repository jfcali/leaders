import PyPDF2
import os

os.chdir('/home/jgomez/Documents/personal/Datatas Bravas/leaders')
PDFfilename = "data/PDF/2016-2018.pdf" #filename of your PDF/directory where your PDF is stored
writer = PyPDF2.PdfFileWriter()

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

tableStart1 = 40
tablestart2 = 45

tb1 = 46

def extractTablesFrom(start, end, name):
    for x in range(start, end):
        writer.addPage(pfr.getPage(x))

    with open(name, "wb") as outputStream: #create new PDF
        writer.write(outputStream) #write pages to new PDF

extractTablesFrom(tableStart1, tablestart2, "data/PDF/2016-TABLE.pdf")