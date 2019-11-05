#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


data_set=pd.read_csv(r"C:\Users\Ashutosh\Desktop\diabetes.csv")


# In[34]:


x=data_set.iloc[:,:-1]


# In[5]:


y=data_set.iloc[:,-1]


# In[8]:


x.head()


# In[9]:


y.head()


# In[32]:


print(data_set.iloc[2,5])


# In[35]:


print(x.isnull().any())


# In[36]:


print(y.isnull().any())


# In[37]:


print(x.info())


# In[39]:


x=x.values
y=y.values


# In[40]:


x


# In[41]:


y


# In[42]:


from sklearn.model_selection import train_test_split


# In[44]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=0)


# In[52]:


from sklearn.preprocessing import StandardScaler


# In[53]:


scalar_x = StandardScaler()
x_train = scalar_x.fit_transform(x_train)
x_test = scalar_x.transform(x_test)


# In[54]:


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)


# In[55]:


y_pred = classifier.predict(x_test)


# In[56]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# In[57]:


print(cm)


# In[58]:


from sklearn.metrics import precision_recall_fscore_support


# In[61]:


prf=precision_recall_fscore_support(y_test,y_pred)
print('\t\t\tZERO\tONE')
print('PRECISION\t:',prf[0]*100)
print('RECALL\t\t:',prf[1]*100)
print('F1 MEASURE\t:',prf[2]*100)
print('SUPPORT\t\t:',prf[3])


# In[62]:


from sklearn import metrics


# In[63]:


print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test,y_pred)*100)


# In[ ]:




