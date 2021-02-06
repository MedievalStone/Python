import sys
import PyPDF2

input= sys.argv[1:]

def combinePdf(pdfList):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        merger.append(pdf)
    merger.write('super.pdf');

combinePdf(input)