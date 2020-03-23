from tika import parser
import re
import os

list_of_pdfs = [file for file in os.listdir("pdfs/") if file.endswith(".pdf")]


# extracting data from pdf file
def extract_pdf_text(file_path):
    text = parser.from_file(file_path)["content"]
    return text


# cleaning the string
def remove_numbers_and_lines(text):
    # remove all non-armenian letters
    text = re.sub(u"[^\u0530-\u058f0-9\s]", "", text)
    text = "".join([x for x in text if not x.isdigit()])
    text = text.replace("\n", "")
    text = re.sub("  +", " ", text)
    text = text.split(":")
    return text


# writing data to the txt file
def write_in_file(my_list, current_txt_heading):
    # check if text is more than 100 bytes
    if len(max(my_list, key=len)) > 100:
        with open(current_txt_heading, "w", encoding="utf-8") as f1:
            for list_item in my_list:
                f1.write(list_item + "\n")


for current_name in list_of_pdfs:
    current_pdf = "pdfs/" + current_name[0:-4] + ".pdf"
    current_txt = "cors/" + current_name[0:-4] + ".cor"

    current_text = extract_pdf_text(current_pdf)
    # check if the text is not empty
    if current_text:
        write_in_file(remove_numbers_and_lines(current_text), current_txt)
