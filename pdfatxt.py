import pyPdf 
from pdf import PdfFileReader, PdfFileWriter

pdf = pyPdf.PdfFileReader(open(filename, "rb")) 
for page in pdf.pages: 
    print(page.extractText()) 

filename = open('C:/Users/54112/Downloads/Bueno_para_comer.pdf')