#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Netflix Movies and TV Shows Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:\\Users\\fakih\\Downloads\\netflix_titles.csv")

# Basic info
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns)

# Data Cleaning
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

#  null values in country, director, cast
df['country'].fillna("Unknown", inplace=True)
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)

# Show distribution by year
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='release_year', order=sorted(df['release_year'].unique())[-20:])
plt.title("Number of Releases Per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  distribution
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Content Type Distribution")
plt.ylabel('')
plt.show()

#  10 Countries
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries with Most Content")
plt.xlabel("Number of Titles")
plt.show()


df['genre_1'] = df['listed_in'].str.split(',').str[0]
top_genres = df['genre_1'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.show()


# In[ ]:





# In[ ]:




