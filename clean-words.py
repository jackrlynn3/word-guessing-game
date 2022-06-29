# Use this file to only get words of lengths 7 to 15
import os

def clean_words():

    # Change directory to the directory the file is in
    os.chdir(os.path.dirname(__file__))
    print(f'In directory file is in: {os.getcwd()}\n')

    # Open necessary files
    f = open('words.txt', 'r')
    fn = open('words-cleaned.txt', 'w')
    print('File opened!\n')

    # Check word lengths and for all alphabetic characters
    lines = f.readlines()
    f.close()
    for line in lines:
        usable = True
        line = line.strip()
        if (len(line) < 7 or len(line) > 15):
            usable = False
        for i in range(len(line)):
            if (not line.isalpha()):
                usable = False
        if (usable):
            print(line, file=fn)
    fn.close()
    print('New cleaned words file created!\n')

clean_words()