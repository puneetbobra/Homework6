import os

#Read the file book.txt and write the output in summary.txt
FILENAME = 'book.txt'
OUTPUT_FILE = 'summary2.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'

#define file variables to open multiple files
try:
    out = open(OUTPUT_FILE, WRITE_MODE)
    book_file = open(FILENAME, READ_MODE, encoding='utf-8')
    with out, book_file:
        text = book_file.read()
        
        #make all alphabets lower case to make it case insensitive
        text = text.lower()

        word_counts = {}
        new = {}
        all_alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        for word in text:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                       
        for word, count in sorted(word_counts.items()):
            if word in all_alphabets:
                out.write(f'{word.upper():<3} {count}\n')
            else: pass

        if all_alphabets.issubset(word_counts) == True:
            out.write('\nIt has all letters')
        else: out.write("\nIt doesn't have all letters")

except OSError:
    print(f'Unable to open {FILENAME}')
    
#End