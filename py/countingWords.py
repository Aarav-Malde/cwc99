userInput = input("Write a short sentence/para/story")
k= 0
characterCount = 0
for i in userInput:
    characterCount = characterCount + 1
    if (i == " "):
        k = k +1
        characterCount = characterCount-1
  
    




wordCount = k
print(wordCount , "is the number of words in the sentece entered by you ")
print(characterCount , "is the number of characters in the sentece entered by you ")
