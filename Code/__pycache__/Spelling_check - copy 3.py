import re
import os

#os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words\Alphabet")
text = 'This is a test file the test file will containz 4 sentence This is the third sentence i like carz'

wrong_words = []
wrong_word_chars = []
seperate_text = []
new_text = []
index_file =[]
words_that_are_testing = {}
can_be_correct_words = []


#seperates the text into invidisual words for future uses such as finding each individual words in a word base.
def seperate(text):
    global seperate_text
    seperate_text = re.split(r'[.|\s]', text)
    seperate_text = [x.lower() for x in seperate_text]
    return seperate_text

def percentage_grader(word_list, percentage):
    global words_that_are_testing
    for x in range(len(words_that_are_testing)):
                if words_that_are_testing[word_list[x]] < (len(wrong_word_chars) *percentage )// 100: # (len(wrong_word)/len(wrong_word)/2) percentage based. say wrong word length is 4, divide that by 2 (4/2) you'll get 2
                    words_that_are_testing.pop(word_list[x])
    
    

    
#Function looks up each word, and if the word is incorrect, it will fix it.
def word_lookup(list):
    Alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    global wrong_words
    global wrong_word_chars
    global index_file
    global words_that_are_testing
    wrong_words_index = []
   

    #switches to Word directory to grab the Main wordbase
    os.chdir(r'C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words')
    word_count = 0
    #Reads and makes a copy of the Main Wordbase
    with open("Word_base.txt", "r") as file:
        txt_file = file.read()

    #Lines 45-57 searches for the words that are in the Main Wordbase, counts if the word is in the file and outputs the words found and not found.
    for word in list:
        if word in txt_file:
            word_count += 1
        # Elif statement activates if the word has an "s" character at end of the word. It will then check the Main wordbase if the word minus the "s" character is in the Wordbase and will allow it to pass as is.
        elif word[len(word)-1] == "s" and word[len(word)-1] in txt_file or word[len(word)-1] == ".": 
           #print(word)
           word_count += 1
        #Another elif statement if that allows the word to slide if it's a numerical value
        elif word.isnumeric():
            word_count +=1
        else:
            wrong_words.append(word)
            wrong_words_index.append(list.index(word))
            list.remove(word)
        print(wrong_words_index)
    
    print("{} word(s) found in the wordbase. {} word(s) not found".format(word_count, len(wrong_words)))
    print(wrong_words)
    
    #The code switches into a more-indept directory that has files seperated for each Letter in the Alphabet
    os.chdir(r"C:\Users\katom\OneDrive\Desktop\python_projects\Grammer_bot\Words\Alphabet")
    for i in range(len(wrong_words)):
      
        #Lines 64-68 will check the first character of each string in the list: wrong_words to see if its an (letter) word and creates a copy of the wordbase of the corresponding file.
        first_char = wrong_words[i][0]
        if first_char in Alphabet_string:
            with open(str(first_char.upper() + '.txt'), 'r') as file:
                for x in file:
                #Appends words from index_file that corresponds to the len()(+1/-1) of each wrong_word to Dictionary: words_that_are_testing as a way to grade each word.
                    if len(x) == len(wrong_words[i]):
                        words_that_are_testing[x] = 0
                    elif len(x)-1 == len(wrong_words[i]) or  len(x)+1 == len(wrong_words[i]):
                        words_that_are_testing[x] = 0

            #for-loop seperates the wrong word into characters for future use with the use of wrong_word_chars.
            for x in range(len(wrong_words[i])):
                wrong_word_chars.append(wrong_words[i][x])
                  
            # First Step of Spelling correction. lines 89-96 looks at both the wrong_word_chars and each word in the Dictionary: words_that_are_testing to see if they share similar characters and counts each one.
            can_be_correct_words = [x for x in words_that_are_testing.keys()]
            for x in range(1, len(wrong_word_chars)):
                for y in range(len(words_that_are_testing.keys())):
                 if wrong_word_chars[x] in can_be_correct_words[y]:
                    #print(can_be_correct_words[y], wrong_word[x])
                    words_that_are_testing[can_be_correct_words[y]] += 1
            #if then will be graded in the function/procedure percentage
            percentage_grader(can_be_correct_words, 50)
            
            
                  
            
            can_be_correct_words = [x for x in words_that_are_testing.keys()] #updates the organzied list of words that can be correct
            
            #might add this in percentage()
            for x in words_that_are_testing.keys():   #resets the counter for next step for correction.
                words_that_are_testing[x] = 0
           
            #The second step in the Spelling correction will check the order of appearance for each word. 
            limit = len(wrong_word_chars) 
            for x in range(len(can_be_correct_words)):
                search_word = can_be_correct_words[x][:limit] # search_word takes up to the limit amount of wrong words to check order of apperance.
                while len(search_word) < limit: #incase search_word length is less than limit, it will add an underscore to it. 
                   search_word = search_word + "_" 
                for z in range(limit):
                    count = 0
                    if search_word[z] == wrong_word_chars[z]:
                        count +=1
                        words_that_are_testing[can_be_correct_words[x]] += count
                
            
            percentage_grader(can_be_correct_words, 75)
            print(words_that_are_testing, "hi")
            
                   
            

            can_be_correct_words = [x for x in words_that_are_testing.keys()] # reupdates it again.

            #highest_num = 0
            
                
            print(can_be_correct_words, "hi")
            
            #Varible "correct_word" takes the first element in list: can_be_correct_words due to it matching most as the potentail word 
            correct_word = can_be_correct_words[0] 
            print(wrong_words_index)
            #Takes the wrong word and replaces with the correct word in the sentecnce. 
            x = 0
            print(wrong_words_index, "test", correct_word)
            #print(wrong_words_index[x])
            list.insert(wrong_words_index[x], correct_word)
            wrong_words_index.remove(wrong_words_index[x])
            for i in range(len(wrong_words_index)):
                wrong_words_index[i] +=1 
            print(x, wrong_words_index)
            x += 1
        
                
            wrong_word_chars = []
            #wrong_words_index = []
    #returns list for future use in main.py 
    print(word_count)
    
    return(list)
    
        
            

                

#print(text, "hi")     
seperate(text)
#print(seperate_text)
new_text = str(word_lookup(seperate_text))
print(new_text)


    

   


    