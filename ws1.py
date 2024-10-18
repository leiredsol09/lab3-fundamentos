import requests
import pandas as pd 
import matplotlib.pyplot as plt 

################## avg EU for the last 5 years (2019-2023) ##################

url = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ei_bsco_m?format=JSON&unit=BAL&indic=BS-CSMCI&s_adj=SA&lang=en&sinceTimePeriod=2019&untilTimePeriod=2023&geo=EU27_2020'
data = requests.get(url).json()

values= data['value']
time_indices= data['dimension']['time']['category']['index']
df = pd.DataFrame(list(values.items()), columns=['index', 'value'])

indices_time = {i: f for f, i in time_indices.items()}
df['index']=df['index'].astype(int)
df['time']= df['index'].map(indices_time)
df.drop('index', axis=1, inplace = True)
df['year']= df['time'].str[:4]

df['value'] =df['value'].astype(float).abs()

avg_eu = df.groupby('year')['value'].mean()

plt.figure(figsize=(6, 6)) 
avg_eu.plot(kind='bar', color='blue')
plt.title('Average EU Consumer Confidence per Year')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.tight_layout()
plt.show()


################## avg EU for each month 2023 ##################
df['month']= df['time'].str[5:]
df_eu = df[df['year']=='2023']
avg_es = df_eu.groupby('month')['value'].mean()

plt.figure(figsize=(6, 6)) 
avg_es.plot(kind='bar', color='blue')
plt.title('Average EU Consumer Confidence in 2023')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.tight_layout()
plt.show()




################## avg Spain for each month 2023 ##################

url_es = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ei_bsco_m?format=JSON&unit=BAL&indic=BS-CSMCI&s_adj=SA&lang=en&sinceTimePeriod=2019&untilTimePeriod=2023&geo=ES'
data_es = requests.get(url_es).json()

values_es= data_es['value']
time_indices_es= data_es['dimension']['time']['category']['index']
df_es = pd.DataFrame(list(values_es.items()), columns=['index', 'value'])
indices_time_es = {i: f for f, i in time_indices_es.items()}
df_es['index']=df_es['index'].astype(int)
df_es['time']= df_es['index'].map(indices_time_es)
df_es.drop('index', axis=1, inplace = True)
df_es['year']= df_es['time'].str[:4]
df_es['month']= df_es['time'].str[5:]
df_es = df_es[df_es['year']=='2023']
df_es['value'] =df_es['value'].astype(float).abs()
avg_es = df_es.groupby('month')['value'].mean()

plt.figure(figsize=(6, 6)) 
avg_es.plot(kind='bar', color='blue')
plt.title('Average ES Consumer Confidence in 2023')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.tight_layout()
plt.show()
