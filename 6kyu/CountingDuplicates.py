from collections import Counter

def duplicate_count(text):
    count = 0
    charCounter = Counter()

    for char in text:

        if char.lower() in charCounter and charCounter[str(char.lower())] == 1:

            count += 1

        charCounter.update({char.lower():1})
        
    return count
     