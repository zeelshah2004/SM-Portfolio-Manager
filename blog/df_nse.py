#!/usr/bin/env python
# coding: utf-8

# #Data Scraping Using
# 
# ##Moneycontrol
# 
# ##https://www1.nseindia.com/corporates/content/securities_info.htm

# In[1]:


import pandas as pd


# In[2]:


def build_df_nse_abrasives():
    raw_data=pd.read_html("https://www.moneycontrol.com/stocks/marketstats/industry-classification/nse/abrasives.html")

    df_nse_abrasives = raw_data[0] #list to dataframe

    df_nse_abrasives[['Company','others']]= df_nse_abrasives['Company Name'].str.split(r"\bAdd\b",expand=True)
    df_nse_abrasives['Company Name']=df_nse_abrasives['Company']

    df_nse_abrasives = df_nse_abrasives.iloc[ ::7 , :7: ]

    df_nse_abrasives['Category'] = 'Abrasives'
    
    return df_nse_abrasives


# In[3]:


def build_nse_aerospace_defence():
    raw_data = pd.read_html("https://www.moneycontrol.com/stocks/marketstats/industry-classification/nse/aerospace-defence.html")

    df_nse_aerospace_defence = raw_data[0]

    df_nse_aerospace_defence[['Company','others']]= df_nse_aerospace_defence['Company Name'].str.split(r"\bAdd\b",expand=True)
    df_nse_aerospace_defence['Company Name']=df_nse_aerospace_defence['Company']
    
    df_nse_aerospace_defence = df_nse_aerospace_defence.iloc[ ::7, :7:]
    
    df_nse_aerospace_defence['Category'] = 'Aerospace-defence'
    
    return df_nse_aerospace_defence


# In[4]:


def build_nse_df():
    df_nse = pd.DataFrame()
    frames = []

    df1 = build_nse_aerospace_defence()
    frames.append(df1)
    df2 = build_df_nse_abrasives()
    frames.append(df2)
    
    df_nse = pd.concat(frames)

    return df_nse


# In[5]:


df_nse =build_nse_df()

#print(df_nse)

