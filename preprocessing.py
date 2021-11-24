#!/usr/bin/env python
# coding: utf-8

# ## 데이터 전처리
#  - 일별로 누적 확진자 수와 누적 사망자 수로 나와있던 데이터를 그 당일 확진자와 사망자가 나오도록 전처리 작업을 실행

# In[1]:


import pandas as pd

df=pd.read_csv('101_DT_COVID19_004_20211107144457.csv')
df.head()


# In[2]:


df.info()


# In[3]:


ndf = pd.DataFrame(columns = ['국가별', '시점', '확진자수[명]','사망자수[명]'])


# In[4]:


ndf = ndf.astype({'확진자수[명]':'int64'})
ndf = ndf.astype({'사망자수[명]':'int64'})


# In[5]:


ndf.head()


# In[6]:


ndf.info()


# In[7]:


country=""
p=0
t=0
for row in df.itertuples():
    if(row[1] != country ):
        country = row[1]
        p=row[3]
        t=row[4]
        ndf = ndf.append({'국가별':row[1], '시점':row[2], '확진자수[명]':row[3],'사망자수[명]':row[4]}, ignore_index=True)
    else:
        ndf= ndf.append({'국가별':row[1], '시점':row[2], '확진자수[명]':row[3]-p,'사망자수[명]':row[4]-t}, ignore_index=True)
        p=row[3]
        t=row[4]


# In[8]:


ndf.info()


# In[9]:


ndf.head()


# In[10]:


ndf.to_csv('korona_world.csv', index=False, header=False, encoding='utf8')

