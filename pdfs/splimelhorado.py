import re
from PyPDF2 import PdfFileReader, PdfFileWriter

arquivo = 'combinado2.pdf'

entrada = PdfFileReader(open(arquivo,'rb'))

paginas = entrada.numPages

for i in range(paginas):
    m = re.search('\nUNIVERSIDADE FEDERAL DO PARANÁ', entrada.getPage(i).extractText())

    if m: print('{} - achou'.format(i))
    else: print(i)
