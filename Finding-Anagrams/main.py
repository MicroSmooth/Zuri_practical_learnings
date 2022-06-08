# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from dataclasses import replace
from distutils.command.check import SilentReporter


def find_anagrams(word, anagram):
    # [assignment] Add your code here

    #change word to lowercase
    word = word.lower()
    anagrama = anagram.lower()

    #remove whitespace
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    #sorted(word) == sorted(anagram) #true or false

    return sorted(word) == sorted(anagram)

print("calling find_anagrams with 'silent' and 'listen' ", find_anagrams("silent", "listen"))
print("calling find_anagrams with 'elvis' and 'lives' ", find_anagrams("elvis", "lives"))
print("calling find_anagrams with 'lovers' and 'hovers' ", find_anagrams("lovers", "hovers"))
