
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('C:/Users/priye/Desktop/LearningSpring2018/python/Week5-Visualization\dataset/Indicators.csv')
data.shape


# In[3]:


data.head(10)


# In[4]:


countries = data['CountryName'].unique().tolist()
len(countries)


# In[5]:


indicators = data['IndicatorName'].unique().tolist()
len(indicators)


# In[6]:


countryCodes=data['CountryCode'].unique().tolist()


# In[7]:


len(countryCodes)


# In[8]:


years = data['Year'].unique().tolist()
len(years)


# In[9]:


print(min(years), 'to', max(years))


# In[10]:


hist_indicator= 'CO2 emissions \(metric'
hist_country = 'USA'


# In[11]:



mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country)


# In[12]:


stage = data[mask1 & mask2]


# In[13]:


stage.head()


# In[14]:


_


# In[29]:


years = stage['Year'].values
co2 = stage['Value'].values


# # BAR CHART
# 

# In[30]:


plt.bar(years,co2)
plt.show()


# ### This chart does not contain any detail about the axis
# 

# In[61]:


plt.plot(years, co2)
plt.xlabel('Year')
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.title("Co2 Emissions in USA over the years")
#plt.axis([1959,2011,0,25])
plt.grid(True)
plt.show()


# ### This chart as its Y axis starting from 15, Which may make this graph misleading

# # Line Chart

# In[60]:


plt.plot(years, co2)
plt.xlabel('Year')
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.title("Co2 Emissions in USA over the years")
plt.axis([1959,2011,0,25])
plt.grid(True)
plt.show()


# ### This chart as its Y axis starting from 0, Which makes this graph more trustworthy

# # Histogram

# ### Plotting all values

# In[49]:


hist_data = stage['Value'].values


# In[50]:


len(hist_data)


# In[59]:


plt.hist(hist_data,10,normed=False,facecolor ='red')
plt.xlabel('Year')
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.title("Co2 Emissions in USA over the years")
plt.grid(True)


# # Comparing USA's data with other countries

# In[79]:


hist_indicator1 ='CO2 emissions \(metric '
hist_year = 2011
mask3 = data['IndicatorName'].str.contains(hist_indicator1) 
mask4 = data['Year'].isin([hist_year])


# In[82]:


co2_2011= data[mask3 & mask4]
co2_2011.head()


# In[83]:


print (len(co2_2011))


# In[93]:


fig, ax = plt.subplots()


ax.annotate("USA", xy = ( 18 ,5 ), xycoords ='data',xytext=(18,30), textcoords ='data' , arrowprops = dict (arrowstyle = ' ->',connectionstyle ='arc3'),)

plt.xlabel('Co2 Emission per capita')
plt.ylabel('Number of Countries')
plt.title("No. of Countries vs Co2 Emisssion per capita in 2011")
plt.grid(True)


plt.hist( co2_2011['Value'] , 10, normed = False , facecolor= 'Red')


# <font color=blue> We can clearly say that USA was having higher Co2 Emission per capita than most of the countries </font>

# In[102]:


hist_indicator2= 'GDP per capita \(constant 2005'
hist_country1 ='USA'


# In[103]:


mask5 = data['IndicatorName'].str.contains(hist_indicator2) 
mask6 = data['CountryCode'].str.contains(hist_country1)


# In[104]:


gdp_stage = data[mask5 & mask6]


# In[105]:


gdp_stage.head()


# GDP Per Capita over the years in USA

# In[124]:


#plt.axis([0,50000,1959,2012])
plt.plot(gdp_stage['Year'].values,gdp_stage['Value'].values)
plt.axis([1959,2012,0,50000])
plt.xlabel('Year')
plt.ylabel('GDP Per Capita')
plt.title("GDP per capita in USA over the years")
plt.grid(True)
plt.show()


# <font color=blue> It can be noted that GDP in USA is growing over the years with a little bit of fluctuation , in 2008 we can notice the fluctuation caused by recession.

# # Scatter Plot

# In[139]:


print('GDP Min year =',gdp_stage['Year'].min(),'GDP Max year =', gdp_stage['Year'].max())

print('Co2 Min year =',stage['Year'].min(),'Co2 Max year =', stage['Year'].max())


# In[158]:


gdp_stage_trunc = gdp_stage[gdp_stage['Year'] < 2012]


# In[159]:


print(len(gdp_stage_trunc))


# In[160]:


print(len(stage))


# In[118]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[162]:


fig, axis = plt.subplots()

plt.grid(True)
axis.set_title('Co2 Emission vs GDP',fontsize = 10)
axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[2],fontsize= 10)
axis.set_ylabel(stage['IndicatorName'].iloc[2],fontsize= 10)
x= gdp_stage_trunc['Value'].values
y =stage['Value'].values
axis.scatter(x,y)
plt.show()


# In[165]:


np.corrcoef(gdp_stage_trunc['Value'],stage['Value'])


#  0.077 is pretty weak correlation
