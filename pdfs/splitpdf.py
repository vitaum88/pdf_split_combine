from PyPDF2 import PdfFileReader, PdfFileWriter

arquivo = 'arquivo.pdf'

entrada = PdfFileReader(open(arquivo, 'rb'))


for i in range(entrada.numPages):
    saida = PdfFileWriter()
    saida.addPage(entrada.getPage(i))

    with open('Página_'+str(i)+'.pdf', 'wb') as f:
        saida.write(f)

