# from fpdf import FPDF
# print(pprint.pformat(res.text))
# print(len(res.text))
# pdf = FPDF('L')
# pdf.add_page()
# pdf.set_font('helvetica', "B", 16)
# pdf.cell(40, 10, 'HELLO WORLD')
# pdf.output('hw.pdf')


from packages.api_data import definations


defination, link = definations('fight')
print(defination)