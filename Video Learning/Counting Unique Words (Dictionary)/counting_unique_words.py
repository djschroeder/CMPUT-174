in_file = open('2701.txt','r')
number_of_words = 0
word_counts = {}
for line in in_file:
    for word in line.split():
        #if word not in word_counts:
            #word_counts[word] = 1
        #else:
            #word_counts[word] = word_counts[word] + 1
        word_counts[word] = word_counts.get(word,0) + 1
        number_of_words = number_of_words +1
in_file.close()
print('Number of unique words counted: ',len(word_counts))
print('Number of words in the file: ',number_of_words)
out_file = open('unique_words_counts.txt', 'w')
for key in word_counts:
    out_file.write(key + ': ' + str(word_counts.get(key)) + '\n')

out_file.close()