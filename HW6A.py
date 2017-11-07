#Write a code that prints out 15 most frequent words from the file words.txt.
import collections

#The re module provides regular expression matching operations
import re

words = re.findall(r'\w+', open('text.txt').read().lower())
most_common = collections.Counter(words).most_common(15)
print(most_common)
