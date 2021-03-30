import nltk
from nltk.tokenize import sent_tokenize
from statistics import mean

with open("etchison.txt", "r", encoding="utf-8") as f:
    text = f.read()

'''
sent_tokenize = sent_tokenize(text)
ns = len(sent_tokenize)


word_count = lambda sentence: len(word_tokenize(sentence))
word_tok = nltk.word_tokenize(text)
NoWord = [',','(',')',':',';','.','%','\x96','{','}','[',']','!','?',"''","``"]
word_tok2 = [i for i in word_tok if i not in NoWord]
nw = len(word_tok2)

print(float(nw)/ns)

sent_len = []
for i in sent_tokenize:
    sent_w1 = nltk.word_tokenize(i)
    sent_w2 = sent_w2 = [i for i in sent_w1 if i not in NoWord]
    sent_len.append(len(sent_w2))

import pandas as pd
import matplotlib.pyplot as plt
dfh = pd.DataFrame(sent_len)
dfh.hist(bins=50)
dfh.hist()
plt.show()
'''

tokened_sent = sent_tokenize(text)

main_dict = {}

for item in tokened_sent:
    item1 = list(item.split(" "))
    item2 = [' '.join(item1)]
    Length = []
    Length.append(len(item1))
    mydict = dict(zip(item2, Length))
    main_dict.update(mydict)

print('Maximum Value: ', max(main_dict.values()))
print('Minimum Value: ', min(main_dict.values()))
print('average Value: ', mean(main_dict.values()))
