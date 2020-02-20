import re
import os

from src.util import get_project_root

root_path = str(get_project_root())

summariser_input_dir = root_path + '/data/sample_judgement_text_cleaned/'

summariser_output_dir = root_path + '/tests/summariser_tests/output/'


for case in os.listdir(summariser_input_dir):

    if not case.endswith('.txt'):
        continue
    output_dict = {}
    case_no = re.search('case_\d+', case).group()
    with open(os.path.join(summariser_input_dir, case), 'r') as f:
        case_text = f.readlines()

    # locate the relevant files in output folder
    output_files = os.listdir(summariser_output_dir)
    output_files = [file for file in os.listdir(summariser_output_dir) if case_no in file]

    removed_text_dict = {}
    for outfile in output_files:
        with open(os.path.join(summariser_output_dir, outfile), 'r') as f:
            output_text = f.readlines()

            removed_text = [text for text in case_text if text not in output_text]

        if 'casesummariser' in outfile:
            removed_text_dict['casesummariser'] = removed_text
        elif 'letsum' in outfile:
            removed_text_dict['letsum'] = removed_text

        output_dict[case] = removed_text_dict

print(output_dict)

    # with open(os.path.join(summariser_input_dir, case), 'r') as in_f:
    #     input_case_text = in_f.readlines()
