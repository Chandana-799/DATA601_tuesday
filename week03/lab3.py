#!/usr/bin/env python
# coding: utf-8

# # Lab 3
# 
# 
# Tasks:
# 
# By using the flights data find all flights:
# 
# 1. Had an arrival delay of two or more hours.
# 
# 2. Flew to Houston (IAH or HOU)
# 
# 3. Were operated by American, Delta
# 
# 4. How many values are missing in `dep_time`?
# 
# 5. Sort `flight` to find fastest flight.
# 
# 6. Which flights travelled the shortest?

# In[6]:


import pandas as pd

flights = pd.read_csv('https://raw.githubusercontent.com/msaricaumbc/DS_data/master/nyc_flights.csv')


# In[7]:


(flights.dep_delay>=2)


# In[8]:


flights[(flights.dest=="IAH") | (flights.dest=="HOU")]


# In[9]:


flights[(flights.carrier=="AA")|(flights.carrier=="DL")]


# In[13]:


flights[flights.dep_time.isnull()].flight.count()


# In[15]:


flights.sort_values(["hour","minute"]).head(1)


# In[17]:


flights.sort_values(["distance"])


# In[ ]:





# In[ ]:




