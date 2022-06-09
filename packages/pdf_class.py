from fpdf import FPDF, HTMLMixin


class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(110)
        self.cell(50, 10, 'Definations', border=1, align='C')
        self.ln(20)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
