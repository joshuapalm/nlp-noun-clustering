#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift


df = pd.read_csv('../features.csv')
features = df.loc[:, (df.columns != 'noun') & (df.columns != 'tag')]
X = features.to_numpy()


# In[18]:


df


# In[28]:


clustering = MeanShift().fit(X)
cluster_labels = list(clustering.labels_)


# In[31]:


grouped_indices = pd.Series(range(len(cluster_labels))).groupby(cluster_labels, sort=False).apply(list).tolist()


# In[32]:


grouped_indices


# In[33]:


''' So according to this initial grouping, the nouns at index 69 and index 85 were close together in feature space.
    Let's take a look...
'''


# In[35]:


print(df['noun'][69])


# In[36]:


print(df['noun'][85])


# In[ ]:


''' That's pretty cool. We were able to cluster together these two math-related Wikipedia articles based on word class
    distributions on our first attempt with very a little effort:
        https://en.wikipedia.org/wiki/Area
        https://en.wikipedia.org/wiki/Integral
    More analysis coming soon...
'''.

