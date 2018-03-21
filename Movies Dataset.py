
# coding: utf-8

# In[125]:


import pandas as pd
import numpy as np


# In[126]:


import matplotlib.pyplot as plt


# In[64]:


movies = pd.read_csv("C:/Users/priye/Desktop/LearningSpring2018/python/Week-4-Pandas/ml-20m/movies.csv")
type(movies)


# In[65]:


tags = pd.read_csv("C:/Users/priye/Desktop/LearningSpring2018/python/Week-4-Pandas/ml-20m/tags.csv")
type(tags)


# In[145]:


ratings = pd.read_csv("C:/Users/priye/Desktop/LearningSpring2018/python/Week-4-Pandas/ml-20m/ratings.csv")
type(ratings)


# In[95]:


del tags['timestamp']


# In[147]:


del ratings['timestamp']


# In[99]:


movies['year']= movies['title'].str.extract('.*\((.*)\),*',expand = True)


# In[100]:


movies.isnull().any()


# In[101]:


tags.isnull().any()


# In[102]:


ratings.isnull().any()


# In[103]:


movies = movies.dropna()


# In[104]:


tags= tags.dropna()


# In[105]:


ratings = ratings.dropna()


# In[181]:


isSciFi =table2['genres'].str.contains('Sci-Fi')


# In[133]:


table1=pd.merge(movies,ratings,on = 'movieId' , how = 'inner')
table1.head()


# In[117]:


print(min(table1.year), 'to' , max(table1.year))


# In[122]:


print(len(table1['year'].unique().tolist()))


# In[124]:


2015-1893


# 2015-1893 = 122 and our query shows that there are only 115 unique values , it means movies have not ben recorded in the database for 7 distinct years
# 

# In[148]:


ratings['rating'].mean()


# In[196]:


table2['title' ][isSciFi].head()


# In[171]:


avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']

avg_ratings.head()


# In[175]:


table2=pd.merge(movies,avg_ratings,on = 'movieId' , how = 'inner')


# In[227]:


table2.head()


# In[238]:


table3=table2[isSciFi]
type(table3)
table3.head()


# In[268]:


avgscifi_ratings = table3.groupby('year', as_index=False).mean()
avgSF=avgscifi_ratings.drop(avgscifi_ratings.index[90])


# In[285]:


years = avgSF['year'].values
rating = avgSF['rating'].values
avgSF


# In[320]:


# switch to a line plot

fig, ax = plt.subplots(figsize=(20 ,15))
plt.plot(years,rating,)

# Label the axes
plt.xlabel('Year')
plt.ylabel('Rating')

#label the figure
plt.title('Average Rating of Sci-Fi Movie over the years')

# to make more honest, start they y axis at 0
plt.axis([1975, 2015,0,5])
plt.grid(True)
plt.savefig('Average Rating of Sci-Fi Movie.jpeg')
plt.show()


