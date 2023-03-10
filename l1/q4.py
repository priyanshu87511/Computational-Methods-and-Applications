import random

# creating the class text generator
class TextGenerator:
    # taking two_tuple as keys in dict and following words as values
    def assimilateText(self, file):
        # maintaining prefix dictionary
        prefix_dic = {}
        prev2 = ""
        prev = ""
        now = ""
        self.file = file
        # opening the file
        file =  open('sherlock.txt','r')
        # for every line and every word
        for line in file:
            for word in line.split(): 
                # changing the values after each iteration to maintain dictionary
                prev2 = prev  
                prev = now
                now = word
                # after first two words
                if(prev2 != ""):
                    # if tuple is yet not there in the dictionary
                    if (prefix_dic.get(tuple([prev2, prev])) == None):
                        prefix_dic[(prev2, prev)] = [now]
                    # if it is there than append it to the list
                    else:
                        prefix_dic[tuple([prev2, prev])].append(now)
        # storing prefix_dic in self.prefix
        self.prefix = prefix_dic

    # function to generate text
    def generateText(self, n, word = "London"):
        # for the first word maintaining list of all the words which came after it
        word_list = []
        for key in (self.prefix).keys():
            if(key[0] == word):
                word_list.append(key[1])
        # if there is only one word
        if(n==1):
            flag = []
            file = open(self.file, 'r')
            # checking if that word is there in the file
            for line in file:
                for words in line.split(): 
                    if(word == words):
                        flag.append(word)
            # if it is there then printing the word
            if(flag!=[]):
                print(word)
            else:
                raise Exception("Unable to produce text with the specified start word")
        # if the word was not there in the text it will raise exception
        elif(word_list == []):
            raise Exception("Unable to produce text with the specified start word")
        # other wise
        else:
            # taking random word from the list and searching it in the dictionary 
            random_num = random.choice(word_list)
            print(word+" "+random_num,end=" ")
            # given number of times
            n-=2
            while(n):
                # if tuple has no element after it then it will take second argument as beginning and repeat again
                if((self.prefix).get(tuple([word, random_num])) == None):
                    self.generateText(n, random_num)
                else:
                    # taking random item from the available words present
                    items = (self.prefix)[tuple([word, random_num])]
                    item = random.choice(items)
                    print(item, end = " ")
                    # modifying the values
                    word = random_num
                    random_num = item
                    n -= 1

# testing
t = TextGenerator()
t.assimilateText("sherlock.txt")
t.generateText(2, "considerable")