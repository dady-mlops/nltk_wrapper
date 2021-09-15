"""
The main file of the natural language processing program.
"""
import argparse
import os
import sys
import time
#
import api


def parser_args():
    """
    This function is a parser of data input through the Terminal.

    :return parser.parse_args()(namespace):parced path to the file with text.
    """
    parser = argparse.ArgumentParser(
        description='This program handles and analyzes natural text and '
                    'performs linguistic operations.'
                    'Put your text file into the "text_files" folder, '
                    'run the program and select required operations.'
    )
    parser.add_argument('--folder', type=str,
                        default="../text_files/",
                        help='The folder with your text file to process.')
    parser.add_argument('--operation', type=int,
                        choices=[1, 2, 3, 4],
                        default=1,
                        help='Select the operation you want to apply to your text:\n'
                             '"1" - tokenizing, deleting stopwords\n'
                             '"2" - lemmatizing, stemming and tagging\n'
                             '"3" - classification of tokens; frequency distribution\n'
                             '"4" - lexical analysis: definitions, synonyms, antonyms\n')
    return parser.parse_args()


def text_file():
    """
    This function creates a path to a text file
    inside the "text_files" folder
    and gets its full name.

    Introduced variables:
    args(namespace): parced path to the folder,
                     parced type of operation
    files(list): names of text files inside the folder

    :return:
    path(str): complete path to the text file
    file(str): complete name of the text file
    """
    args = parser_args()
    files = os.listdir(args.folder)
    path = file = ""
    for file in files:
        path = os.path.join(args.folder, file)
    return path, file


def run():
    """
    The main function of the program.
    Runs the front-end file ('api.py').

    Introduced variables:
    args(namespace): parced path to the folder,
                     parced type of operation
    t_file(list): complete name of/path to the text file
    process, morphology, semantics, systematics(class objects):
    instances of relevant classes from the 'api.py' module
    text(str): 'string' object of text inside the text file

    """
    args = parser_args()
    t_file = text_file()
    try:
        process = api.Interface(t_file[0])
        morphology = api.MorphInterface(t_file[0])
        semantics = api.SemanticInterface(t_file[0])
        systematics = api.SystemInterface(t_file[0])
        text = process.file_open()
        morphology.file_open()
        semantics.file_open()
        systematics.file_open()
    except (UnboundLocalError, FileNotFoundError):
        print("THE FOLDER IS EMPTY. "
              "PLACE A TEXT FILE INTO THE 'text_files' FOLDER.")
        sys.exit()
    print(f"\nTEXT FILE '{t_file[1]}':\n{text:^10}")
    while True:
        try:
            args.operation = int(input("\n" + "*" * 30 +
                                       "\nPlease, select an operation:\n"
                                       "'1' - tokenizing, deleting stopwords\n"
                                       "'2' - lemmatizing, stemming and tagging\n"
                                       "'3 - classification of tokens; "
                                       "frequency distribution\n"
                                       "'4' - lexical analysis: "
                                       "definitions, synonyms, antonyms\n"
                                       "'0' - EXIT the program"
                                       "\n" + "*" * 30 +
                                       "\nThe number of operation: "))
            if args.operation < 0 or args.operation > 4:
                print("You can only input values: {1}, {2}, {3}, {4} or {0}")
                continue
        except ValueError:
            print("Inadmissible characters. Try again")
            continue
        time.sleep(1)
        if args.operation == 1:
            print("\nWORD TOKENIZING:")
            morphology.get_w_tokens()
            time.sleep(1)
            print("\nSENTENCE TOKENIZING:")
            morphology.get_s_tokens()
            time.sleep(1)
            print("\nTHE TEXT WITHOUT STOPWORDS:")
            morphology.get_stop_words()
            time.sleep(1)
        elif args.operation == 2:
            print("\nLEMMATIZING:")
            semantics.get_lemmatizing()
            time.sleep(1)
            print("\nSTEMMING:")
            semantics.get_stemming()
            time.sleep(1)
            print("\nTAGGING:")
            semantics.get_tags()
            time.sleep(1)
        elif args.operation == 3:
            print("\nCLASSIFICATION:")
            systematics.get_classifying()
            time.sleep(1)
        elif args.operation == 4:
            print("\nANALYSIS:")
            systematics.get_analysis()
            time.sleep(1)
        elif args.operation == 0:
            print("\nTHANK YOU FOR USING THE SERVICE")
            sys.exit()


def not_main_entry_point():
    print('0000')
    pass


if __name__ == "__main__":
    run()
else:
    not_main_entry_point()
