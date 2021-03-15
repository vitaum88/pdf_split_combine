from PyPDF2 import PdfFileMerger
import os

saida = PdfFileMerger()

for filename in os.listdir():
    if '.pdf' in filename:
        saida.append(filename)

with open('combinado2.pdf', 'wb') as f:
    saida.write(f)
    
