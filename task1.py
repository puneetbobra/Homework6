import numpy as np

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
    
    #count the number of words in the file - remove '.' and ',' at the end of the string
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
    out.write(f'The average word length is: {int(avg)}\n')
    
    # Average sentence length 
    # Can be calculated by dividing total character count by total number of sentences
    count_of_sentences = lines.split('.')
    out.write(f'The average sentence length is: {int(total / len(count_of_sentences))}\n')
    
    # Word distribution of all words ending in "ly"
    ending_ly = []
    freq = 0
    values = 0
    out.write('\nA word distribution of all words ending in "ly"\n')
    for word in count_of_words:
        if word.endswith('ly') == True:
            ending_ly.append(word)            
        else: pass    
    ending_ly = sorted(ending_ly)
    values, freq = np.unique(ending_ly, return_counts = True)
    for i, j in zip(values, freq):        
        out.write(f'{i} - {j}\n')
    
        
    # List of top 10 longest words in descending order
    out.write('\nA list of top 10 longest words in descending order\n')
    temp1 = [s.strip('.') for s in count_of_words]
    temp2 = [s.strip(',') for s in temp1]
    words = (sorted(np.unique(temp2), key= len))
    top_10 = words[-10:]
    top_10 = reversed(top_10)
    for word in top_10:
        out.write(f'{word}, ')
            

#End