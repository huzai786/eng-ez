from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(110)
        self.cell(50, 10, 'Definations', border=1, align='C')
        self.ln(20)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")



pdf = PDF(orientation='L')
pdf.add_page()
pdf.set_font('Times', size=12)
h = 20
for i in range(1, 41):
    pdf.cell(0, 10, f'Printing line number {i}', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(10)
    page_break = pdf.will_page_break(10)
    print(page_break)
    if page_break:
        h = 20
    pdf.line(1, 30 + h, 300, 30 + h)
    h += 20
    print(h)



pdf.output('TUT.pdf')
