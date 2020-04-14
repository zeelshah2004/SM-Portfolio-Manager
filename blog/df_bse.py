#!/usr/bin/env python
# coding: utf-8

# #Data Scraping Using 
# ##Moneycontrol
# ##https://www1.nseindia.com/corporates/content/securities_info.htm

# In[1]:


import pandas as pd 


# In[2]:


def build_df_bse_abrasives():
    raw_data=pd.read_html("https://www.moneycontrol.com/stocks/marketstats/industry-classification/bse/abrasives.html")

    df_bse_abrasives = raw_data[0] #list to dataframe

    df_bse_abrasives[['Company','others']]= df_bse_abrasives['Company Name'].str.split(r"\bAdd\b",expand=True)
    df_bse_abrasives['Company Name']=df_bse_abrasives['Company']

    df_bse_abrasives = df_bse_abrasives.iloc[ ::7 , :7: ]

    df_bse_abrasives['Category'] = 'Abrasives'
    
    return df_bse_abrasives


# In[3]:


def build_bse_aerospace_defence():
    raw_data = pd.read_html("https://www.moneycontrol.com/stocks/marketstats/industry-classification/bse/aerospace-defence.html")

    df_bse_aerospace_defence = raw_data[0]

    df_bse_aerospace_defence[['Company','others']]= df_bse_aerospace_defence['Company Name'].str.split(r"\bAdd\b",expand=True)
    df_bse_aerospace_defence['Company Name']=df_bse_aerospace_defence['Company']
    
    df_bse_aerospace_defence = df_bse_aerospace_defence.iloc[ ::7, :7:]
    
    df_bse_aerospace_defence['Category'] = 'Aerospace-defence'
    
    return df_bse_aerospace_defence


# In[4]:


def build_bse_df():
    df_bse = pd.DataFrame()
    df_bse.head()
    frames = []

    df1 = build_bse_aerospace_defence()
    frames.append(df1)
    df2 = build_df_bse_abrasives()
    frames.append(df2)
    
    df_bse = pd.concat(frames)

    return df_bse


# In[5]:


df_bse =build_bse_df()

#print(df_bse)

#print(df_bse)

