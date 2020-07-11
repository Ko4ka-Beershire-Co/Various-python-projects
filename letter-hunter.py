# Fishing file CYKA input - letters to catch, no space, no integers, careful with encoding 

from __future__ import print_function
import string

bookfile = '406.txt' # file name (it has to share ROOT location)
hunted = 'cyka' # Basically the letters you are hunting, I was looking for Ё for example (no space)

# Output module: works as print console function
with open(bookfile, encoding="utf8") as thebook:
    # read text of book and split from white space
    print('\n'.join(set(word.lower().strip(string.punctuation)
                    for word in thebook.read().split()
                    if all(c in word.lower() for c in hunted))))
