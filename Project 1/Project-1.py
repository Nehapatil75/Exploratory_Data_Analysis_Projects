#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install numpy
pip install pandas
pip install matplotlib
pip install seabornc


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[ ]:





# # Drop Unnamed column
# 

# In[10]:


df = df.drop("Unnamed: 0",axis = 1)
print(df.head())


# # changw weekly study hours columns

# In[ ]:


# df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
#df.head()


# In[11]:


df.head()


# # gender distribution

# In[25]:


plt.figure(figsize = (5,5))
ax = sns.countplot(data= df, x= "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# In[ ]:


# from the baovr we have analyzed number of females data is 
#more than the number of males data 


# In[17]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[ ]:





# In[27]:


plt.figure(figsize = (5,5))

sns.heatmap(gb, annot = True)
plt.title("Relationship Between Parents's Education and Students's Score")
plt.show()


# In[ ]:





# In[ ]:


#from the above chart we have concluded theta the education of the parents have a good impact of scores.


# In[21]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[29]:


plt.figure(figsize = (5,5))

sns.heatmap(gb1, annot = True)
plt.title("Relationship Between Parents Marital Status and Students's Score")

plt.show()


# In[ ]:


# from the above chart we have concluded that the parents marital status have no impact or negligible impact on the stidents scores..


# # To detect outliers

# In[31]:


sns.boxplot(data = df, x= "MathScore")
plt.show()


# In[32]:


sns.boxplot(data = df, x= "ReadingScore")
plt.show()


# In[33]:


sns.boxplot(data = df, x= "WritingScore")
plt.show()


# In[34]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[49]:


groupA = df.loc[(df['EthnicGroup']=="group A")].count()
groupB = df.loc[(df['EthnicGroup']=="group B")].count()
groupC = df.loc[(df['EthnicGroup']=="group C")].count()
groupD = df.loc[(df['EthnicGroup']=="group D")].count()
groupE = df.loc[(df['EthnicGroup']=="group E")].count()

l = ["group A","group B","group C","group D","group E"]
mylist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

print(mylist)
plt.pie(mylist,labels= l, autopct = "%1.2f%%")
plt.title("Distributions of Ethincs Groups")
plt.show()


# In[48]:


ax = sns.countplot(data = df, x ='EthnicGroup')
ax.bar_label(ax.containers[0])

