def anagrams(word, words):
    sortedWord = sorted(word)
            
    return [wordinList for wordinList in words if sortedWord == sorted(wordinList)] 