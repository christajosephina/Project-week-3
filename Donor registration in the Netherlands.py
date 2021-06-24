#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importing pandas and dataset


# In[7]:


import pandas as pd


# In[8]:


df = pd.read_excel("Donor registration.xlsx")


# In[9]:


#examining the data
df.info()


# In[10]:


df


# In[11]:


#creating columns for percentages
df['Permission_percent'] = df.Permission * 100 / (df.Permission+df.Partly+df.No_permission)
df['Partly_percent'] = df.Partly * 100 / (df.Permission+df.Partly+df.No_permission)
df['No_permission_percent'] = df.No_permission * 100 / (df.Permission+df.Partly+df.No_permission)


# In[12]:


#writing the code for just selecting where people come from, not their generation
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')]


# In[28]:


#graphing the info
import matplotlib.pyplot as plt
ax = plt.gca()

df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(kind='line',x='Time',y=["Permission_percent", "Partly_percent", "No_permission_percent"],ax=ax)

plt.show()


# In[14]:


#This graph is too messy to understand, so I'm making three percentage graphs
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(x ='Time', y=["Permission_percent", "Partly_percent", "No_permission_percent"], kind = 'line')


# In[15]:


#as well as a graphs for just 'No permission'
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(x ='Time', y="No_permission_percent", kind = 'line')


# In[19]:


#making the same graphs for 1st and 2nd generation migrants (unknown whether they are western or not
df[(df.Background =='1gen')|(df.Background =='2gen')].groupby(by='Background').plot(x ='Time', y=["Permission_percent", "Partly_percent", "No_permission_percent"], kind = 'line')


# In[29]:


#making a chart for 'no permission' for all types
ax = plt.gca()

df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(kind='line',x='Time',y='No_permission_percent',ax=ax)

plt.show()

