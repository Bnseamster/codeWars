def generate_hashtag(s):
    
    if 0 < len(s) <= 140:
        s = s.split(' ')
        return ''.join(['#'] + [word.capitalize() for i, word in enumerate(s)]) 
                
    return False