#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


# In[4]:


sigmoid(15)


# In[5]:


sigmoid(1)


# In[6]:


sigmoid(-84)


# In[7]:


sigmoid(0.5)


# In[8]:


def tanh(x):
  return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))


# In[9]:


tanh(-56)


# In[10]:


tanh(50)


# In[11]:


tanh(1)


# In[12]:


def relu(x):
    return max(0,x)


# In[13]:


relu(-100)


# In[14]:


relu(8)


# In[15]:


def leaky_relu(x):
    return max(0.1*x,x)


# In[16]:


leaky_relu(-100)


# In[17]:


leaky_relu(8)


# In[ ]:




