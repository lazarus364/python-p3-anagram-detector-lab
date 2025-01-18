# your code goes here!
# lib/anagram.py  

class Anagram:  
    def __init__(self, word):  
        self.word = word  

    def match(self, possible_anagrams):  
        matches = []  
        sorted_word = sorted(self.word)  

        for candidate in possible_anagrams:  
            if sorted(candidate) == sorted_word:  
                matches.append(candidate)  

        return matches
    
listen = Anagram("listen")  
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  
    
