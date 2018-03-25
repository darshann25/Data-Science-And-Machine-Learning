
# coding: utf-8

# In[7]:


out = [x for x in range(0,101,10)]


# In[8]:


print(out)


# In[9]:


def times2(var):
    return var * 2


# In[10]:


times2(5)


# In[11]:


seq = [1, 2, 3, 4, 5]
list(map(times2, seq))


# In[12]:





# In[13]:


seq = [1, 2, 3, 4, 5]
list(map(lambda var: var * 2, seq))


# In[24]:


seq = [n for n in range(10)]


# In[25]:


list(filter(lambda x : x % 2 != 0, seq))


# In[26]:


text = 'Go Birds! #Eagles win the superbowl!'


# In[29]:


text.split('#')


# In[30]:


text.split()


# In[32]:


x = [(1,2),(3,4),(5,6)]


# In[33]:


for a,b in x:
    print(a)
    print(b)

