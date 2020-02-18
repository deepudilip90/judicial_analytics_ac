"""
This script can be used as the high level main code for the text pre-processing pipeline. The various text
pre-processing operations are defined as separate functions in the module src.preprocess.preprocess_functions.
It is recommending to add any new text pre-processing operations that might be required in the said module above and
change this script only if required to modify the pipeline
"""
# system packages
import os

# user defined modules
from src.util import get_project_root
from src.preprocess.preprocess_functions import preprocess_data


def main(input_path, output_path_base):
    """
    Main function that implements the text processing pipeline.

    :param input_path: path to the input folder containing the raw .txt data files prior to any pre-processing. If the
    given path is to a folder, this function will loop over all available .txt files inside the same. If the given path
    is instead to a .txt file, only the same will be processed
    :type input_path: str
    :param output_path_base:
    :return: path to the folder where to keep the pre-processed file. Should be directory. The output file will have the
    same name as the input file
    :rtype str
    """

    if os.path.isdir(input_path):
        for file in os.listdir(input_path):
            if file.endswith('.txt'):
                filepath = os.path.join(input_path, file)
                print('now reading ', filepath)
                cleaned_text = preprocess_data(filepath)
                output_file_path = os.path.join(output_path_base, file)
                with open(output_file_path, 'w') as f:
                    print('writing output to ', output_file_path)
                    f.write(cleaned_text)

    else:
        filename = input_path
        assert(filename.endswith('.txt'))
        print('now reading ', filename)
        cleaned_text = preprocess_data(input_path)
        output_filename = input_path.split(os.sep)[-1]
        output_file_path = os.path.join(output_path_base, output_filename)
        with open(output_file_path, 'w') as file:
            print('writing output to ', output_file_path)
            file.write(cleaned_text)


if __name__ == '__main__':
    root_dir = get_project_root()
    in_path = str(root_dir) + os.sep + 'data' + os.sep + 'sample_judgement_text_raw' + os.sep
    out_path = str(root_dir) + os.sep + 'data' + os.sep + 'sample_judgement_text_cleaned' + os.sep

    main(in_path, out_path)
