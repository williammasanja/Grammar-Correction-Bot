#The modules we'll be using: re (regex, used for control of parsing) and os (operating sytem, access to different directories on my system)  
import re
import os 
from Spelling_check import seperate, word_lookup

os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Code") #Added this so we always start with the same directory to begin.
main_dir = os.listdir() # Tracks our main location of the folder we want to come back to

# Changing the system path to documents directory to create a copy of the document.
os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Documents")
document_dir = os.listdir() #Document directory list 

#askes the user for an document
print("Choose an document from the list: ")
for x in document_dir:
    print(x)
document = str(input("What document do you want to fix up?: "))

if document in document_dir:
    pass
else:
    print("False try again")
    document = str(input("What document do you want to fix up?: "))

#reads and copies the document text into a list to be used for functions 
with open(document, "r") as file:
    text = file.read()
    sentence_counter = 0 

    sentences = seperate(text) #uses Spelling_check.py
    
    for x in range(len(sentences)):
        sentences[x] = sentences[x].replace("\n", "")
    for y in sentences:
       if y == '':
           sentences.remove(y)

    


print("Original: ", sentences)
new_text = ' '.join(x for x in word_lookup(sentences)) #turns list back into string
print("Corrected: ", new_text)
