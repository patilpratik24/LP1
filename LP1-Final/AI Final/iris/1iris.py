#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


from sklearn.datasets import load_iris


# In[5]:


iris=load_iris()


# In[6]:


iris


# In[8]:


data_set=pd.DataFrame(data=np.c_[iris['data'],iris['target']],columns=iris['feature_names']+['targets'])


# In[9]:


print('\n','DATA SET INFORMATION'.center(45,'_'))
print(data_set.info())


# In[10]:


print('\n','STATISTICAL INFORMATION'.center(45,'_'))
print(data_set.describe())


# In[11]:


print('\n','MINIMUM'.center(45,'_'))
print(data_set.min())


# In[12]:


print('\n','MAXIMUM'.center(45,'_'))
print(data_set.max())


# In[13]:


print('\n','STANDARD DEVIATION'.center(45,'_'))
print(data_set.std())


# In[14]:


print('\n','MODE'.center(45,'_'))
print(data_set.mode())


# In[15]:


print('\n','VARIANCE'.center(45,'_'))
print(data_set.var())


# In[17]:


print('\n','COLUMNS DTYPE (IF NOMINAL)'.center(45,'_'))
print(data_set.select_dtypes(include=['category']))


# In[22]:


print('\n','COLUMNS DTYPE (ALL)'.center(45,'_'))
print(data_set.dtypes)


# In[25]:


print('\n','MEMORY USAGE'.center(45,'_'))
print(data_set.memory_usage())


# In[26]:


def num__missing(x):
    return sum(x.isnull())


# In[27]:


print('\n','MISSING VALUE CHECK'.center(45,'_'))
print('\n','MISSING VALUES PER COLUMN:')
print(data_set.apply(num__missing,axis=0))


# In[34]:


data_set[['sepal length (cm)','sepal width (cm)','petal length (cm)','sepal width (cm)']].plot.hist(bins=15,title='All Features')
plt.show()


# In[35]:


data_set[['sepal length (cm)','sepal width (cm)']].plot.hist(bins=15,title='Sepal Features')
plt.show()


# In[36]:


data_set[['petal length (cm)','petal width (cm)']].plot.hist(bins=15,title='Petal Features')
plt.show()


# In[38]:


data_set.plot.box(title="All Features with Outliers")
plt.show()


# In[ ]:




