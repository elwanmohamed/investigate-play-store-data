#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv("E:/Level 3/Semester1/DSS/DataAnalysis/data challenger/googleplaystore.csv")


# In[3]:


df.head(5)


# In[4]:


df.shape


# In[5]:


df.drop(['Price','Last Updated','Current Ver','Android Ver'], inplace=True, axis=1)


# In[6]:


df.head(5)


# In[7]:


df.columns


# In[8]:


df.shape


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


df.drop(df[(df['Reviews'] == '3.0M')].index,inplace=True)


# In[12]:


df['Reviews']=df.Reviews.astype('int')


# In[13]:


df[df['Reviews']==df['Reviews'].max()]


# In[14]:


df['Installs']=df['Installs'].str.replace('+',' ',regex=True)


# In[15]:


df['Installs']=df['Installs'].str.replace(',','',regex=True)


# In[16]:


df['Installs']


# In[17]:


df['Installs']=df.Installs.astype('int')


# In[18]:


df.info()


# In[19]:


df[df['Installs']==df['Installs'].max()]


# In[20]:


play_df=df.set_index('Category')


# In[21]:


df['Content Rating'].describe()


# In[22]:


play_df.head(10)


# In[23]:


play_df['Content Rating'].unique()


# In[24]:


play_df['Genres'].unique()


# In[25]:


play_df['Size'].describe()


# In[26]:


play_df['Size'].unique()


# In[27]:


play_df.drop_duplicates()


# In[28]:


df.info()


# In[29]:


df['Rating'].describe()


# In[30]:


df['Type'].fillna(method='pad',inplace=True)


# In[31]:


df.info()


# In[32]:


df.hist()


# In[33]:


x = df['Installs']
y = df['Reviews']
colors = np.random.rand(10840)
plt.scatter(x, y, c=colors, alpha=0.5)
plt.show()


# In[34]:


df_ContentValues=df['Content Rating'].value_counts()


# In[35]:


df['Content Rating'].unique()


# In[36]:


print(df_ContentValues)


# In[37]:


x = df['Content Rating'].unique()
y=df_ContentValues     
plt.pie(y,labels=[' Everyone',' Teen',' Mature 17+',' Everyone 10+',' Adults only 18+',' Unrated'],autopct=' %0.2f%% ',pctdistance=0.85,radius=1.5,explode=[0.0,0.0,0.0,0.0,1.5,0.3])
plt.show()


# In[38]:


df_CategoryValues=df['Category'].value_counts()
print(df_CategoryValues)


# In[39]:


Cat_x=list(df['Category'].unique())
print(type(Cat_x))


# In[40]:


Cat_y=df_CategoryValues     
plt.pie(x=Cat_y,labels=Cat_x,radius=2,shadow=True,labeldistance=1,autopct=' %0.2f%% ',pctdistance=0.85)
plt.show()


# In[52]:





# In[ ]:





# In[ ]:


ypos=np.arange(len(df['Category']))
plt.xticks(ypos,df['Category'])
plt.ylabel("Installs(ln)")
plt.title("Category Installations")
plt.bar(ypos,df['Installs'],label="Installs")


# In[ ]:




