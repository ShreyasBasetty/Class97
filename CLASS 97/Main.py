text=input("Enter string : Hi")

characterCount=0
wordCount=1

for i in text:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1

print("Number of word in the string:")       
print(wordCount)
print("Number of character in the string:")
print(characterCount)
