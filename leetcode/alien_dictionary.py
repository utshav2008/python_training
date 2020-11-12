dictionary = {'h':1,'w':2,'o':3,'n':4,'e':5}

word1 = 'hello'
word2 = 'wonderland'

for k in range(min(len(word1),len(word2))):
    if word1[k] != word2[k]:
        print('True')
    else:
        break


