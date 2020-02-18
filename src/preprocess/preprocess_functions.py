"""
This file will have definitions of all relevant text pre-processing functions such as text extraction, text cleaning or
any other relevant operations. It is recommended to keep each text pre-processing operation as separate functions, and
define any new operation that may be required as a new function. The high level main function that will call the
individual pre-processing functions is defined as 'preprocess_data'. It is recommended to modify this function to adapt
the code to changing requirements.
"""

# system packages
import re


def rm_paragraph_numbers(text):
    """
    Currently taken from the source <> for testing judgement summarises. Please modify this function to adapt to our
    requirements
    :param text: input text string containing paragraph numbers
    :type text: str
    :return: text with the paragraph numbers removed
    :rtype: str
    """
    return re.sub(r'^.?\d+\.\s', '', text)


def rm_special_characters(text):
    """
    Currently taken from the source <> for testing judgement summarises. Please modify this function to adapt to our
    requirements
    :param text: input text string containing special characters
    :type text: str
    :return: text with the special characters removed
    :rtype: str
    """

    text = re.sub(r'(?<=[a-zA-Z])\.(?=\d)', '', text)  # removes dot(.) i.e File No.1063
    text = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s[\da-z])', ' ', text)  # to remove the ending dot of abbr
    text = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s?[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~])',
                  '', text)  # to remove the ending dot of abbr
    text = re.sub(r'(?<!\.)[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]', ' ',
                  text)  # removes the other punctuations

    return text


def extract_text_sections_file(filepath):
    """
    This function is used to extract relevant text sections from the input data (.txt) file. This function has been
     written keeping in mind the specific data found in the portal:
    Hence, this function might need modifications if we intend to use it on a different data

    :param filepath: Path to the data file. Should be a .txt file
    :type filepath: str
    :return: a list of individual sentences in the text file, that are relevant for the analysis
    :rtype: str

    """

    with open(filepath, 'r') as file:
        lines = file.readlines()
        extract_start = False

        for idx, line in enumerate(lines):

            if 'Dated' in line:
                extract_start = True

            if extract_start & line.startswith('2.'):
                extract_start_idx = idx
                break

        lines = lines[extract_start_idx:]
        lines = [line for line in lines if not re.search('-\d+-', line)]

        return lines


def preprocess_data(input_file_path):
    """
    This function is used to apply all text cleaning operations to a given input data file. The function first
    extracts the text sections from the input file relevant for the analysis, and then performs necessary text cleaning
    operations. Currently only two text cleaning operations are implemented as can be seen. This shall be expanded later
    on as and when more specific text cleaning operations might be required analysis

    :param input_file_path: Path to the data file. Should be a .txt file
    :type input_file_path: str
    :return: a single string of all the relevant text in the file, obtained after applying the necessary text cleaning
    :rtype: str
    """

    lines = extract_text_sections_file(input_file_path)
    cleaned_text = ""

    for line in lines:
        line = rm_special_characters(line)
        line = rm_paragraph_numbers(line)  # removes the paragraph lables 1. or 2. etc.
        cleaned_text = cleaned_text + "" + line

    return cleaned_text


# def rm_paragraph_numbers(text):
#     return re.sub(r'(\d\d\d|\d\d|\d)\.\s', ' ', text)
#
# def rm_special_characters(text):
#
#     text = re.sub(r'(?<=[a-zA-Z])\.(?=\d)', '', text)  # removes dot(.) i.e File No.1063
#     text = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s[\da-z])', ' ', text)  # to remove the ending dot of abbr
#     text = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s?[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~])',
#                   '', text)  # to remove the ending dot of abbr
#     text = re.sub(r'(?<!\.)[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]', ' ',
#                   text)  # removes the other punctuations
#rge
#     return text

