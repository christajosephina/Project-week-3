#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing pandas and dataset


# In[10]:


import pandas as pd


# In[139]:


df = pd.read_excel("Donor registration.xlsx")


# In[140]:


#examining the data
df.info()


# In[141]:


df


# In[142]:


#creating columns for percentages
df['Permission_percent'] = df.Permission * 100 / (df.Permission+df.Partly+df.No_permission)
df['Partly_percent'] = df.Partly * 100 / (df.Permission+df.Partly+df.No_permission)
df['No_permission_percent'] = df.No_permission * 100 / (df.Permission+df.Partly+df.No_permission)


# In[143]:


#writing the code for just selecting where people come from, not their generation
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')]


# In[144]:


#graphing the info
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].plot(x ='Time', y=["Permission_percent", "Partly_percent", "No_permission_percent"], kind = 'line')


# In[153]:


#This graph is too messy to understand, so I'm making three percentage graphs
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(x ='Time', y=["Permission_percent", "Partly_percent", "No_permission_percent"], kind = 'line')


# In[146]:


#as well as a graph for just 'No permission'
df[(df.Background =='Dutch') | (df.Background =='Western') | (df.Background=='Non-western')].groupby(by='Background').plot(x ='Time', y="No_permission_percent", kind = 'line')


# In[158]:


#making the same graphs for 1st and 2nd generation migrants (unknown whether they are western or not
df[(df.Background =='1gen')|(df.Background =='2gen')].groupby(by='Background').plot(x ='Time', y=["Permission_percent", "Partly_percent", "No_permission_percent"], kind = 'line')

