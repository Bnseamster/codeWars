from collections import Counter

def find_it(seq):
    count = Counter()
    for num in seq:
        count.update({num:1})
    for key, val in count.items():
        if val % 2 == 1:
            return key
            
