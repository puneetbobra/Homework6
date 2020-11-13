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

    #Average length of the words in the file
    total = 0
    for word in count_of_words:
        ch = len(word)
        total += ch
    avg = total / len(count_of_words)
    out.write(f'Average word length is: {round(avg,2)}\n')
  
    t = []
    
    # populate all lower case characters of alphabets to check if all letters exist in the book or not
    for j in range(97, 123):        
        count = 0
        # read the lines 
        for i in lines:   
            #if it is an alphabet then increase the count
            if i == chr(j): count += 1

            #append the characters in list t which would be used for checking if all alphabets exist or not
            t.append(i) 
 
    #count the number of characters in the file excluding spaces
    out.write(f'\nTotal character count: {len(t)}')

#End