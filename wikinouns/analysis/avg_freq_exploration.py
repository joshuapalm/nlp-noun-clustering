#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

df = pd.read_csv('../features.csv')


# In[11]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov1' in c and len(c.split('_')) == 3:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' From the above plot, we can see that when averaging the word class frequencies across all nouns, the most
    frequent word class in the wikipedia article is the noun (when observing the body of text).
    Here are the most frequent word classes:
        1. nn - nouns
        2. jj - adjectives
        3. nns - plural nouns
        4. in - preposition
        5. rb - adverb
        6. dt - determiner
        7. vbn - verb, past participle
        8. vbp - verb, sing. present
        9. vbz - verb, 3rd person sing. present 
        10. vbd - verb, past tense
'''


# In[12]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov2' in c and len(c.split('_')) == 3:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' When looking at only the averages for only the first half of text we see the same word class frequencies.
'''


# In[13]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov3' in c and len(c.split('_')) == 3:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' Same for the first third...
'''


# In[14]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov4' in c and len(c.split('_')) == 3:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' Same for the first fourth. Nothing interesting yet.
'''


# In[15]:


mean_columns = []
for c in list(df.columns):
    if 'freq_4ov4' in c and len(c.split('_')) == 3:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' We can see that for the last fourth of the body of text, there was a minor switch with the ranks of frequencies:
        1. nn - nouns
        2. jj - adjectives
        3. nns - plural nouns
        4. in - preposition
        5. rb - adverb
        6. dt - determiner
        7. vbp - verb, sing. present <------|
        8. vbn - verb, past participle <----|
        9. vbz - verb, 3rd person sing. present 
        10. vbd - verb, past tense
        
    This isn't very interesting because there isn't a huge difference between the frequencies of vbp and vbn.
    Let's now look at the frequencies of pairs of words.
'''


# In[ ]:





# In[16]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov1' in c and len(c.split('_')) == 4:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' So here we can see that the most frequent pairs on average are:
        1. noun - noun
        2. adjective - noun
        3. adjective - noun plural
        4. noun - preposition
        etc.
        
    When we were observing the single word classes (not pairs), there wasn't a whole lot of variance when 
    observing the ranks between the different sections of the wikipedia article content. What about when observing
    with these pairs of words?
'''


# In[18]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov4' in c and len(c.split('_')) == 4:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' Nope, not much difference in frequencies when only looking at the first fourth of the article.
'''


# In[19]:


mean_columns = []
for c in list(df.columns):
    if 'freq_3ov4' in c and len(c.split('_')) == 4:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' The distributions don't appear to be changing too much. '''


# In[20]:


mean_columns = []
for c in list(df.columns):
    if 'freq_4ov4' in c and len(c.split('_')) == 4:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[ ]:


''' That's a bit interesting. When observing the last fourth of the wikipedia article content (on average),
    there is a fairly significant difference when comparing the gap of the top two entries to the other portions.
    Let's take a look at the three word distributions.
'''


# In[21]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov1' in c and len(c.split('_')) == 5:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(10,4))


# In[26]:


mean_columns = []
for c in list(df.columns):
    if 'freq_1ov2' in c and len(c.split('_')) == 5:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(14,4))


# In[27]:


mean_columns = []
for c in list(df.columns):
    if 'freq_2ov2' in c and len(c.split('_')) == 5:
        mean_columns.append(c)
        
mean_df = df[mean_columns].mean()
mean_df = mean_df.sort_values()
mean_df.plot(kind='bar', figsize=(14,4))


# In[ ]:


''' It looks like we are running into the same thing- the overall distributions are quite similar, but
    there are some minor differences when looking at the distributions of different sections of the content.
'''

