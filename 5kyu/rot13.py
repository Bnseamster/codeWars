def rot13(message):
    
    return ''.join([chr((ord(char) + 13-65)%26 + 65) if 65 <= ord(char) <= 90 else chr((ord(char) + 13 - 97)%26+ 97) if char.isalpha() else char for char in message])
