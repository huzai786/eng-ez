from pdf_class import PDF
from api_data import get_definations



def print_pdf(list_of_words):
    pdf = PDF(orientation='L')
    pdf.add_page()
    pdf.set_font('Times', size=13)
    h = 20
    definations = [get_definations(word) for word in list_of_words]
    words = [word for word in list_of_words]
    
    for data, word in zip(definations, words):
        defination_list, link, part_of_speech = data
        defination_string = ''
        for i in defination_list:
            single_defination = i.get('Defination')
            example = i.get('Examples') or None
            if example is None: 
                defination_string += f'DEFINATION: {single_defination} \n'
            else:
                defination_string += f'DEFINATION: {single_defination} \nExample: {example}\n'
            
        string = f'WORD: {word} \n\nLINK: {link} \n\nPART OF SPEECH: {part_of_speech}\n\n'
        pdf.cell(0, 10, string, border=1, new_x='LMARGIN', new_y='NEXT')
        pdf.multi_cell(0, pdf.font_size + 5, defination_string, border=1, new_x='LMARGIN', new_y='NEXT')
        pdf.ln(10)

    x = pdf.output('definations.pdf')
    return None


def get_words(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines