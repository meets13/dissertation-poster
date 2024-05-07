#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'IPL_Ball_by_Ball_2008_2022.csv')


# In[3]:


df.head()


# In[4]:


df.isnull().sum()


# In[5]:


powerplay_df = df[df['overs'].between(1, 6)]


# In[6]:


powerplay_runs = powerplay_df.groupby(['ID', 'BattingTeam'])['total_run'].sum().reset_index(name='powerplay_runs')


# In[7]:


powerplay_balls = powerplay_df[(powerplay_df['extra_type'] != 'wides') & (powerplay_df['extra_type'] != 'noballs')].groupby(['ID', 'BattingTeam']).size().reset_index(name='legal_balls')


# In[8]:


powerplay_data = pd.merge(powerplay_runs, powerplay_balls, on=['ID', 'BattingTeam'])


# In[9]:


powerplay_data['run_rate'] = powerplay_data['powerplay_runs'] / (powerplay_data['legal_balls'] / 6)


# In[10]:


powerplay_data


# In[11]:


from scipy.stats import chi2_contingency


# In[13]:


matches_df = pd.read_csv(r'IPL_Matches_2008_2022.csv')


# In[14]:


powerplay_data = pd.merge(powerplay_data, matches_df[['ID', 'WinningTeam']], on='ID')


# In[15]:


powerplay_data['run_rate_category'] = pd.cut(powerplay_data['run_rate'], bins=[0, 6, 8, 12], labels=['Low', 'Medium', 'High'])


# In[16]:


powerplay_data['won_match'] = powerplay_data['BattingTeam'] == powerplay_data['WinningTeam']


# In[17]:


contingency_table = pd.crosstab(powerplay_data['run_rate_category'], powerplay_data['won_match'])


# In[18]:


chi2, p, dof, ex = chi2_contingency(contingency_table)


# In[19]:


dof


# In[20]:


ex


# In[27]:


print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")


# In[ ]:





# In[ ]:





# In[ ]:




