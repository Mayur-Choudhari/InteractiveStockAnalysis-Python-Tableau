#!/usr/bin/env python
# coding: utf-8

# ## Stock Market Projects

# In[1]:


import pandas as pd


# **Reading all CSV Files**

# In[2]:


apple=pd.read_csv('AAPL.csv')
facebook=pd.read_csv('FB.csv')
google=pd.read_csv('GOOGL.csv')
nvdia=pd.read_csv('NVDA.csv')
tesla=pd.read_csv('TSLA.csv')
twitter=pd.read_csv('TWTR.csv')


# In[3]:


apple.head()


# In[4]:


twitter.head()


# In[5]:


dfs=[apple, facebook, google, nvdia, tesla, twitter]


# **Reason to create list:- Better than applying same functions six times, I will use for loop and apply function to our list.**

# In[6]:


for df in dfs:
    df['MA50']=df.Close.rolling(50).mean()
    df['MA200']=df.Close.rolling(200).mean()


# In[7]:


apple.sample(5)


# **Previous Day Close**

# In[8]:


for df in dfs:
    df['Previous Day Close']=df.Close.shift(1)


# In[9]:


apple.head()


# **Change in Price**

# In[10]:


for df in dfs:
    df['Change in Price']= df['Close']-df['Previous Day Close']


# In[11]:


apple.head()


# **Percent change in price**

# In[12]:


for df in dfs:
    df['Percent change in price']=df.Close.pct_change()


# In[13]:


apple.head()


# **Previous Day Volume**

# In[14]:


for df in dfs:
    df['Previous Day Volume']=df.Volume.shift(1)


# In[15]:


apple.head()


# **Change in Volume**

# In[16]:


for df in dfs:
    df['Change in Volume']=df['Volume']-df['Previous Day Volume']


# In[17]:


apple.head()


# **Percent Change in Volume**

# In[18]:


for df in dfs:
    df['Percent Change in Volume']=df.Volume.pct_change()


# In[19]:


apple.sample(5)


# **Save it to csv file**

# In[20]:


apple.to_csv('APPLE.csv')
google.to_csv('GOOGLE.csv')
facebook.to_csv('FACEBOOK.csv')
nvdia.to_csv('NVDIA.csv')
tesla.to_csv('TESLA.csv')
twitter.to_csv('TWITTER.csv')


# In[ ]:





# In[ ]:




