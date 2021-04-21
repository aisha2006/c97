intro = input("enter your intro: ")
print(intro)
characterCount = 0
wordCount = 1
for character in intro:
    characterCount=characterCount+1
    if(character==" "):
        wordCount=wordCount+1

print("number of words: ")
print(wordCount)
print("number of characters: ")
print(characterCount)