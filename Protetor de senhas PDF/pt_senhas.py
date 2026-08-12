from PyPDF2 import PdfWriter, PdfReader
import getpass
pdfwriter=PdfWriter()
pdf=PdfReader("1.pdf")
for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])
passw=getpass.getpass(prompt='Digite a senha: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)