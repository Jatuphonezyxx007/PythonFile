def CheckVowel(strText):
    strText = strText.upper()
    vowels = ("A","E","I","O","U")
    for item in vowels:
        if item not in strText:
            return False
    return True

newText = input("Enter a word in English:")
if CheckVowel(newText):
    print(newText,"contains every vowel.")
else:
    print(newText,"does not contain every vowel.")
