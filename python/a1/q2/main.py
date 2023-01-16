import os
print (os.getcwd())
paragraph = input("Please input a paragraph:\n")
word_list = paragraph.split()
word_dict = {}
pos=0
PUNCTUATION = [".", "?", "!", ","]
for word in word_list:
    if len(word)>1 and word[-1] in PUNCTUATION:
        word_list.insert(pos+1, word[-1])
        word=word[0:len(word)-1]
    if not word in word_dict:
        word_dict[word]=[]
    word_dict[word].append(pos)
    pos+=1

def key_fun (item1):
    return len(item1[1])


while True:
    user_sel = input("Make a selection:\n\
        R: Replace a Word\n\
        D: Print the Dictionary\n\
        P: Print the Paragraph\n\
        C: Print Most Frequent Uncommon Word\n\
        X: Exit the program\n")
    user_sel = user_sel.lower()

    if user_sel == "x":
        print("Thank you for using the program!")
        break

    elif user_sel == "r":
        to_replace = input("Input the word you would like to replace:\n")
        replace_with = input("Input the word you want to use as the replacement:\n")

        occurences = word_dict.pop(to_replace)
        word_dict[replace_with] = occurences

        print("A total of "+str(len(occurences))+" replacement(s) have been made.\n")

    elif user_sel == "p":
        reverse_dict = {}
        for item in word_dict.items():
            for position in item[1]:
                reverse_dict[position]=item[0]
        constructed_paragraph = ""
        for i in range(len(reverse_dict)):
            word = reverse_dict[i]
            if not word in PUNCTUATION:
                constructed_paragraph += " "
            constructed_paragraph += word
        constructed_paragraph = constructed_paragraph[1:]
        print(constructed_paragraph)
        
    elif user_sel == "d":
        dict_items = word_dict.items()
        for item in dict_items:
            print(item[0]+"->"+str(item[1]))

    elif user_sel == "c":
        dict_items = word_dict.items()
        dict_items_sorted = sorted(dict_items, key = key_fun, reverse = True)
        common_words = open("CommonWords.txt","r").read()
        common_words.split("\n")
        print(common_words)
        for i in range(len(dict_items_sorted)):
            if not dict_items_sorted[i][0] in common_words:
                print("Most frequent uncommon word(s) are: " + dict_items_sorted[i][0])
                break