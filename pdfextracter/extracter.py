from tika import parser


#extracting data from pdf file
def extract_pdf_text(file_path):
    text = parser.from_file(file_path)['content']
    return text

#cleaning the string
def remove_numbers_and_lines(text):
    text = ''.join([x for x in text if not x.isdigit()])
    text = text.replace('\n','')
    text = " ".join(text.split())
    text = text.split(":")

    return text

#writing data to the txt file
def write_in_file(my_list):
    with open('test.txt', 'w', encoding="utf-8") as f1:
        for i in range(len(my_list)):
            content = my_list[i]
            f1.write(content+'\n')

my_text = extract_pdf_text('nor_barer.pdf')
final_list = remove_numbers_and_lines(my_text)
write_in_file(final_list)