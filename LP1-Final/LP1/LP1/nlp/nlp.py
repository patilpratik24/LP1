#!/usr/bin/env python
# coding: utf-8

# In[5]:


import nltk


# In[6]:


a="my name is ash"


# In[7]:


words=nltk.word_tokenize(a)
print(words)


# In[8]:


b="the sun rises at east. sets at west"


# In[9]:


sents=nltk.sent_tokenize(b)
print(sents)


# In[10]:


c="It originated from the idea that there are readers who prefer learning new skills from the comfort of their drawing rooms"


# In[11]:


from nltk.stem.porter import PorterStemmer
po_ste=PorterStemmer()


# In[12]:


tok=nltk.word_tokenize(c)


# In[13]:


for w in tok:
    print(w,":",po_ste.stem(w))


# In[14]:


words=["program","programs","programer","programing","programers"]


# In[15]:


for i in words:
    print(i,":",po_ste.stem(i))


# In[16]:


from nltk.stem import WordNetLemmatizer
wlem=WordNetLemmatizer()


# In[20]:


for j in tok:
    print(j,":",wlem.lemmatize(j))


# In[24]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# In[29]:


stop_words=set(stopwords.words('english'))


# In[30]:


txt="Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station"


# In[36]:


tokenized = sent_tokenize(txt)


# In[44]:


for k in tokenized:
    wordList=nltk.word_tokenize(k)
    wordList=[l for l in wordList if not l in stop_words]
    tagged=nltk.pos_tag(wordList)
    print(tagged)


# In[45]:


from nltk import Nonterminal, nonterminals, Production, CFG


# In[47]:


nt1=Nonterminal('NP')
nt2=Nonterminal('VP')


# In[48]:


nt1.symbol()


# In[49]:


nt1==Nonterminal('NP')


# In[50]:


nt1==nt2


# In[56]:


S, NP, VP, PP = nonterminals('S, NP, VP, PP')
N, V, P, DT = nonterminals('N, V, P, DT')
prod1=Production(S, [NP,VP])
prod2=Production(NP, [DT,NP])


# In[52]:


prod1.lhs()


# In[53]:


prod1.rhs()


# In[57]:


prod1 == prod2


# In[61]:


grammar=CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> 'the' N | N PP | 'the' N PP
VP -> V NP | V PP | V NP PP
N -> 'cat'
N -> 'dog'
N -> 'rug'
V -> 'chased'
V -> 'sat'
P -> 'in'
P -> 'on'
""")


# In[62]:


from nltk.parse import RecursiveDescentParser
rd=RecursiveDescentParser(grammar)


# In[63]:


sentence1='the cat chased the dog'.split()
sentence2='the cat chased the dog on the rug'.split()


# In[64]:


for t in rd.parse(sentence1):
    print(t)


# In[65]:


for t in rd.parse(sentence2):
    print(t)


# In[66]:


from nltk.parse import ShiftReduceParser
sr=ShiftReduceParser(grammar)


# In[67]:


for t in sr.parse(sentence1):
    print(t)


# In[70]:


for t in sr.parse(sentence2):
    print(t)


# In[71]:


nltk.parse.chart.demo(2, print_times=False, trace=1, sent='I saw a dog', numparses=1)


# In[73]:


nltk.parse.chart.demo(2, print_times=False, trace=0, sent='I saw John with a dog', numparses=2)


# In[74]:


nltk.parse.chart.demo(1, print_times=False, trace=0, sent='I saw John with a dog', numparses=2)


# In[75]:


nltk.parse.chart.demo(5, print_times=False, trace=1, sent='I saw John with a dog', numparses=2)


# In[ ]:




