from HashTable import HashTable

tableOfWords = HashTable( 500 )

paragraph =  "I like to eat pizza. I also like to eat hamburgers. And I like to eat pasta."


def setHashTable( paragraph ):
    paragraph = paragraph.lower()
    
    allWords = []
    word = ""
    for letter in paragraph:
        if ord( letter ) >= 97 and ord( letter ) <= 122:
            word += letter
        if letter == " ":
            allWords.append( word )
            word = ""
    allWords.append( word )

    for currentWord in allWords:
        tableOfWords.add( currentWord )

setHashTable( paragraph )


word = "fish"
result = tableOfWords.findCount( word )
print( f"The word {word} is {result} times in the paragraph.")