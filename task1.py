#Read the file book.txt and write the output in summary.txt
FILENAME = 'speech.txt'
OUTPUT_FILE = 'summary.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'

#define file variables to open multiple files
out = open(OUTPUT_FILE, WRITE_MODE)
book_file = open(FILENAME, READ_MODE,encoding='utf-8')

#Read input file and open output file
with out, book_file:
    lines = book_file.read()    
    
    #count the number of words in the file
    count_of_words = lines.split()
    out.write(f'Total word count: {len(count_of_words)}\n')

    #count the number of characters in the file excluding spaces and special characers
    t = []    
    for i in lines:   
        #append the characters in list t, length of t will determine the total character count
        t.append(i)     
    out.write(f'Total character count: {len(t)}\n')

    #Average length of the words in the file
    total = 0
    for word in count_of_words:
        ch = len(word)
        total += ch
    avg = total / len(count_of_words)
    out.write(f'Average word length is: {round(avg,2)}\n')
  
    
#End