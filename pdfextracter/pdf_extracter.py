from tika import parser
import re

from tika import parser

list_of_pdfs = ['armenian_dictionary', 'rights']


# extracting data from pdf file
def extract_pdf_text(file_path):
    text = parser.from_file(file_path)['content']
    return text


# cleaning the string
def remove_numbers_and_lines(text):
    text = ''.join([x for x in text if not x.isdigit()])
    text = text.replace('\n', '')
    text = re.sub(' +', ' ', text)
    text = text.split(":")
    return text


# writing data to the txt file
def write_in_file(my_list, current_txt_heading):
    with open(current_txt_heading, 'w', encoding="utf-8") as f1:
        for list_item in my_list:
            content = list_item
            f1.write(content + '\n')


for current_name in list_of_pdfs:
    current_pdf = 'pdfs/' + current_name + '.pdf'
    current_txt = 'txts/' + current_name + '.txt'

    my_text = extract_pdf_text(current_pdf)
    final_list = remove_numbers_and_lines(my_text)
    write_in_file(final_list, current_txt)