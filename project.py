#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the all required libraries
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


#getting the data set
data=pd.read_csv(r"E:\Kaggle File\country_wise_latest.csv") 


# In[3]:


#printing the data
data


# In[4]:


#Getting the index of the data
data.columns


# In[5]:


#EDA
data.isnull().sum()


# In[6]:


#EDA
data.describe()


# In[7]:


#EDA
data.info()


# In[8]:


#scatter plotting using seaborn relation ploting(relplot)
sns.relplot(x="New cases",y="New deaths",hue="Active",data=data)


# In[10]:


sns.pairplot(data)


# In[14]:


#line plotting using seaborn relation ploting(relplot)
sns.relplot(x='Recovered',y='Active' ,kind='line',data=data)


# In[ ]:




