def spin_words(sentence):        
 
    return ' '.join(''.join(reversed(word)) if len(word) >= 5 else word for i,word in enumerate(sentence.split(' ')))