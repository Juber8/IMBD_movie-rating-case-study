#!/usr/bin/env python
# coding: utf-8

# # <font color = blue> IMDb Movie Assignment </font>
# 
# we have the data for the 100 top-rated movies from the past decade along with various pieces of information about the movie, its actors, and the voters who have rated these movies online. In this assignment, you will try to find some interesting insights into these movies and their voters, using Python.

# ##  Task 1: Reading the data

# - ### Subtask 1.1: Read the Movies Data.
# 
# Read the movies data file provided and store it in a dataframe `movies`.

# In[4]:


import pandas as pd
df=pd.read_csv('IMDB_dataset (1).csv')
df.head()


# - ###  Subtask 1.2: Inspect the Dataframe
# 
# Inspect the dataframe for dimensions, null-values, and summary of different numeric columns.

# In[5]:


# Check the number of rows and columns in the data
df.shape


# In[6]:


#check data types of each column
df.info()


# In[8]:


#check for null values
df.isnull().sum()


# In[72]:


df.columns


# In[10]:


# Check the column-wise info of the dataframe
df.describe()


# In[11]:


# Check the summary for the numeric columns 
df.describe()


# In[12]:


# Check the summary for the numeric and caretorical columns 
df.info()


# ## Task 2: Data Analysis
# 
# Now that we have loaded the dataset and inspected it, we see that most of the data is in place. As of now, no data cleaning is required, so let's start with some data manipulation, analysis, and visualisation to get various insights about the data. 

# -  ###  Subtask 2.1: Reduce those Digits!
# 
# These numbers in the `budget` and `gross` are too big, compromising its readability. Let's convert the unit of the `budget` and `gross` columns from `$` to `million $` first.

# In[18]:


# Divide the 'gross' and 'budget' columns by 1000000 to convert '$' to 'million $'
x=df[['Gross','budget']]
x[:3]
x/1000000
x*1000000


# In[23]:


# Who is having highest rating in year 2016
df[df['IMDb_rating']==8.8]


# In[71]:


# Which movie has Highest budget till date?
df[df['budget']==260000000].Title


# In[48]:


# Average budget spent in 2013
df[df['title_year']==2013].budget.mean()


# In[94]:


# Plot top 10 genres1 

import matplotlib.pyplot as plt
s=df['genre_1'].value_counts().head(10)
type(s)
plt.hist(s)


# In[ ]:





# In[105]:


#List out X man series (means all movies under name - Xman)
df['Title']


# In[ ]:


# List out actors and actress played role in movie 127 Hours


# -  ###  Subtask 2.2: Let's Talk Profit!
# 
#     1. Create a new column called `profit` which contains the difference of the two columns: `gross` and `budget`.
#     2. Sort the dataframe using the `profit` column as reference.
#     3. Extract the top ten profiting movies in descending order and store them in a new dataframe - `top10`.
#     4. Plot a scatter between the columns `budget` and `profit` and write a few words on what you observed.
#     5. Extract the movies with a negative profit and store them in a new dataframe - `neg_profit`

# In[114]:


# Create the new column named 'profit' by subtracting the 'budget' column from the 'gross' column


# ### My Observations: Movies with higher budgets are not necessarily profitable

# The dataset contains the 100 best performing movies from the year 2010 to 2016. However, the scatter plot tells a different story. You can notice that there are some movies with negative profit. Although good movies do incur losses, but there appear to be quite a few movie with losses. What can be the reason behind this? Lets have a closer look at this by finding the movies with negative profit.
