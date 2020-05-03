import os

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4,portrait
import PyPDF2

from reportlab.platypus import Table,TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors


in1path = "C:\\Users\\隼也\\OneDrive\\基本情報午後PDF"
in2path = "C:\\Users\\隼也\\OneDrive\\基本情報午後PDF2"
outpath = "C:\\Users\\隼也\\OneDrive\\基本情報午後PDF3"


for file in os.listdir( in1path ):

    if file in os.listdir( in2path ):
        continue
    in1file = os.path.join( in1path , file )
    in2file = os.path.join( in2path , file )

    pdf_canvas = canvas.Canvas( in2file , pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
    font_size = 16
    pdf_canvas.setFont('HeiseiKakuGo-W5',font_size)
    pdf_canvas.drawString(60,60, file )

    pdf_canvas.showPage()
    pdf_canvas.save()


for file in os.listdir( in1path ):
    if file in os.listdir( outpath ):
        continue
    in1file = os.path.join( in1path , file )
    in2file = os.path.join( in2path , file )

    file2 = open(in2file,'rb')
    pdf2 = PyPDF2.PdfFileReader( file2 )

    pdfWriter = PyPDF2.PdfFileWriter()

    file1 = open(in1file, 'rb')
    pdf1 = PyPDF2.PdfFileReader(file1)

    for page in range( 0, pdf1.getNumPages() ):
        pdf1page1 = pdf1.getPage(page)
        pdf1page1.mergePage(pdf2.getPage(0))
        pdfWriter.addPage( pdf1page1 )

    result = open(os.path.join(outpath , file),'wb')
    pdfWriter.write( result )

#os.startfile(os.path.join(outpath,filename) )