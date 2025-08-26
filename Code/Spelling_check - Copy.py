import re
import os

#os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words\Alphabet")
text = 'This is a test file the test file will containz 4 sentences This is the third sentence i like car'
wrong_words = []
wrong_word = []
seperate_text = []
new_text = []
index_file =[]
words_that_are_testing = {}

#for i in os.listdir():
 #   print(i)

#seperates the text for future uss, such as finding the words in a word base.
def seperate(text):
    global seperate_text
    seperate_text = re.split(r'[\s]', text)
    seperate_text = [x.lower() for x in seperate_text]

def if_not_percentage_remover(x, y):
    global words_that_are_testing
    
#looks up words
def word_lookup(list):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    global wrong_words
    global wrong_word 
    global index_file
    global words_that_are_testing

    new_wrong_words = []
    can_be_correct_words = []
    os.chdir(r'C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words')
    word_count = 0

    with open("Word_base.txt", "r") as file:
        txt_file = file.read()

    # Code searches for the words that are in the wordbase
    for i in list:
        if i in txt_file:
            word_count += 1
            print(i)
        elif  i[len(i)-1:] == "s" and i[0:len(i)-1]in txt_file: # Elif statment incase of the the words in the sentence contains an "s" at the end. will 
           word_count += 1
           print(i)
        else:
            wrong_words.append(i)
            list.remove(i)
    print("{} out found in the wordbase. {} words not found".format(word_count, len(wrong_words)))
    print(wrong_words)
    

    os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words\Alphabet")
    for i in range(len(wrong_words)):
        index = wrong_words[i][0]


        #Opens letter file for the word 
        if index in Alphabet:
            with open(str(index.upper() + '.txt'), 'r') as file:
                for x in file:
                    index_file.append(x)

            # make lines 67 to 72 into a seperate file to add functions in the other code(main.py) if needed last minute
            for x in range(len(index_file)):
                index_file[x] = index_file[x].replace("\n", "")
            for y in index_file:
                if y == '':
                    index_file.remove(y)
            

            # Seperates a list for the words that might be the word
            for x in range(len(index_file)):
                if len(index_file[x])-1 == len(wrong_words[i]) or  len(index_file[x])+1 == len(wrong_words[i]):
                    #print(index_file[x])
                    words_that_are_testing[index_file[x]] = 0
            
            

            for x in range(len(wrong_words[i])):
                wrong_word.append(wrong_words[i][x])      
            
            
            
            
            #Checks for similar characters first 
            print(wrong_word)
            #print(words_that_can_be_correct.keys())
            can_be_correct_words = [x for x in words_that_are_testing.keys()]
            print(can_be_correct_words)
            for x in range(1, len(wrong_word)):
                for y in range(len(words_that_are_testing.keys())):
                 if wrong_word[x] in can_be_correct_words[y]:
                    print(can_be_correct_words[y], wrong_word[x])
                    words_that_are_testing[can_be_correct_words[y]] += 1
            
            print(words_that_are_testing)

                
            for x in range(len(words_that_are_testing)): # if words corresponding is less than 50%, remove it from list
                if words_that_are_testing[can_be_correct_words[x]] < (len(wrong_word)// (len(wrong_word)// 2)): # (len(wrong_word)/len(wrong_word)/2) percentage based. say wrong word length is 4, divide that by 2 (4/2) you'll get 2
                    print(can_be_correct_words[x], (len(wrong_word)// (len(wrong_word)//2)))
                    words_that_are_testing.pop(can_be_correct_words[x])
                  
            
            can_be_correct_words = [x for x in words_that_are_testing.keys()] #updates the organzied list of words that can be correct
            
            
            print(words_that_are_testing.keys())
            print(can_be_correct_words)
            
            #checks the letter order
            for x in words_that_are_testing.keys():     #resets the counter
                words_that_are_testing[x] = 0
           
            #indexs if each word has a similar order as wrong word and counts how many times.
            limit = len(wrong_word)
            print(limit, wrong_word)
            for x in range(len(can_be_correct_words)):
                search_word = can_be_correct_words[x][:limit]
                if len(search_word) < 4:
                   search_word = search_word + "_"
                for z in range(limit):
                    count = 0
                    if search_word[z] == wrong_word[z]:
                        count +=1
                        words_that_are_testing[can_be_correct_words[x]] += count
            
            #Sinced used twice, gonna make percentage function, but thats for saturday
            for x in range(len(words_that_are_testing)):
                if words_that_are_testing[can_be_correct_words[x]] < (len(wrong_word)*0.75): # (len(wrong_word)/len(wrong_word)/2) percentage based. say wrong word length is 4, divide that by 2 (4/2) you'll get 2
                    print(can_be_correct_words[x], (len(wrong_word)// (len(wrong_word)//2)))
                    words_that_are_testing.pop(can_be_correct_words[x])
            
            can_be_correct_words = [x for x in words_that_are_testing.keys()] # redoes it
                #if words_that_are_testing[can_be_correct_words[x]] > 2
            print(words_that_are_testing)


            #picks the first one out of the list
            correct_word = can_be_correct_words[0]
            print(wrong_word)
            #adds it to og sentence, returns it then in main.py makes a new text document with the changes
            for i in list:
                if i in txt_file:
                    pass
                else:
                    list.append(correct_word)
            print(list)
            

                
        
   
seperate(text)
print(seperate_text)
word_lookup(seperate_text)

    

   


    