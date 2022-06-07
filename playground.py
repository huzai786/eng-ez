# from fpdf import FPDF
import requests
import pprint

res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/vague')

with open('ret.txt', 'w+', encoding='utf-8') as f:
    f.write(pprint.pformat((res.json())))
# print(pprint.pformat(res.text))
# print(len(res.text))
# pdf = FPDF('L')
# pdf.add_page()
# pdf.set_font('helvetica', "B", 16)
# pdf.cell(40, 10, 'HELLO WORLD')
# pdf.output('hw.pdf')
