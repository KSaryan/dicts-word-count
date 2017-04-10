import sys
import string

def count_words(my_file):
    poem = open(my_file)
    word_count = {}
    for line in poem:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            word = word.lower()
            word = word.strip(string.punctuation)
            word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print word, count

print sys.argv
count_words(my_file = sys.argv[-1])
