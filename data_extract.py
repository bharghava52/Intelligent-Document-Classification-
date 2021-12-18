import PyPDF2
import os

directory = 'agreement_document'
output = 'agreement'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        pdffileobj = open(f, 'rb')
        pdfreader = PyPDF2.PdfFileReader(pdffileobj)
        x = pdfreader.numPages
        for i in range(x):
            pageobj = pdfreader.getPage(i)
            text = pageobj.extractText()
            file1 = open(os.path.join(
                output, "invoice.txt"), "a")
            file1.writelines(text)
            file1.close
        pdffileobj.close
