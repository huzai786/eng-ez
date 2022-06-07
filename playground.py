from fpdf import FPDF


pdf = FPDF('L')
pdf.add_page()
pdf.set_font('helvetica', "B", 16)
pdf.cell(40, 10, 'HELLO WORLD')
pdf.output('hw.pdf')
