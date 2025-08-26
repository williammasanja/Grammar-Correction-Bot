words = ['a', 'aaaas', 'b', 'bs', 'c' ]
words_to_remove = []
with open("text.txt", "r") as file:
    words = []
    for x in file:
        words.append(x)

for x in range(len(words)):
    y = len(words[x])
    y = y - 2
    if words[x][y] == "s":
        print(words[x])  
        words_to_remove.append(words[x])
for x in words_to_remove:
    if x in words:
        words.remove(x)
with open("New_text.txt", "w") as file2:
    for x in words:
        file2.write(x)
      