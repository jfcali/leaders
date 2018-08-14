import PyPDF2
import os


os.chdir('/home/jgomez/Documents/personal/Datatas Bravas/leaders')
# PDFfilename = "data/PDF/2016-2018.pdf" #filename of your PDF/directory where your PDF is stored
PDFfilename = "data/PDF/todos_los_nombres_2018.pdf" #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

tableStart1 = 8
tablestart2 = 20

tb21 = 45
tb22 = 55

tb31 = 55
tb32 = 60

tb41 = 60
tb42 = 63

tb51 = 63
tb52 = 70


def extractTablesFrom(start, end, name):
    print("writing " + name)
    writer = PyPDF2.PdfFileWriter()
    for x in range(start, end):
        writer.addPage(pfr.getPage(x))
        print("page " + str(x))

    with open(name, "wb") as outputStream: #create new PDF
        writer.write(outputStream) #write pages to new PDF

extractTablesFrom(tableStart1, tablestart2, "data/PDF/output/2018-lideres-actualizado-TABLE.pdf")
#extractTablesFrom(tb21, tb22, "data/PDF/output/2017-lideres-TABLE.pdf")
#extractTablesFrom(tb31, tb32, "data/PDF/output/2018-lideres-TABLE.pdf")
#extractTablesFrom(tb41, tb42, "data/PDF/output/2016-2018-exfarc-familiares-TABLE.pdf")
#extractTablesFrom(tb51, tb52, "data/PDF/output/2011-2018-marcha-patriotica-TABLE.pdf")
