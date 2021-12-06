#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd


# In[5]:


#Qn. 1

X = np.array([[1, 0.2, 0.5], [0.2, 1, 0.8], [0.5,0.8, 1]])
X


# In[6]:


#a)

np.transpose(X)


# In[7]:


b)np.linalg.det(X)


# In[ ]:





# In[21]:


#Question2
num_data = ([[1, 0.2, 0.5], [0.2, 1, 0.8], [0.5, 0.8, 1]])
df = pd.DataFrame(data = num_data, index = ['A', 'B', 'C'], columns = ['A', 'B', 'C'])
print(df)


# In[ ]:


#Qn 3


# In[64]:


#Qn.5

COVID = pd.read_csv('COVID-19 Cases.csv')
#COVID.set_index('Date')
COVID = COVID.set_index('Date')

#pd.to_datetime(COVID.Date)

COVID


# In[61]:


COVID.head(10)


# In[ ]:





# In[77]:


#Qn. 6
df_results1 = COVID[(COVID.Difference >0) & (COVID.Case_Type == 'Confirmed') & (COVID.Country_Region == 'Italy')]
df_results2 = COVID[(COVID.Difference >0) & (COVID.Case_Type == 'Confirmed') & (COVID.Country_Region == 'Germany')]


# In[80]:


df_results1
df_results1.sort_values("Cases")


# In[81]:


df_results2
df_results2.sort_values("Cases")


# In[84]:


#Qn 7
df_results1['Difference'].hist()
df_results2['Difference'].hist()


# In[90]:


#Qn8
df_results1['Difference'].describe()
df_results1['Cases'].describe()


# In[91]:


#Qn9
df_results1.boxplot(by='Country_Region', column=['Difference'], grid=False)


# In[92]:


df_results2.boxplot(by='Country_Region', column=['Difference'], grid=False);


# In[ ]:





# In[93]:


##Qn10.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[96]:


#Qn. 11
df_results1


# In[97]:


df_results2

