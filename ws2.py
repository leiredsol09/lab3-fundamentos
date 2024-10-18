import requests 
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://api.idescat.cat/onomastica/v1/nadons/dades.json?id=40683&lang=en&t=2019-2023&class=t'
response = requests.get(url)

if response.status_code==200: 
    data= response.json()
    records= data['onomastica_nadons']['ff']['f']
    df = pd.DataFrame(records)

    df['c']= df['c'].astype(int)
    df['total_rank']= df['rank'].apply(lambda x: x['total']).astype(int)
    df['female_rank']= df['rank'].apply(lambda x: x['sex']).astype(int)
    df['freq_name']= df['pos1'].apply(lambda x: x['v']).astype(int)
    df['weight_1000_total']= df['pos1'].apply(lambda x: x['w']).apply(lambda x: x['total']).astype(float)
    df['weight_1000_female']= df['pos1'].apply(lambda x: x['w']).apply(lambda x: x['sex']).astype(float)
    df = df.drop(columns=['rank', 'pos1'], axis =1 )
    df = df[df['c']>=2019]


    
    # plot the total rank vs the female for maria 
    plt.figure(figsize=(6,6))
    plt.plot(df['c'],  df['total_rank'], marker='o', linestyle='-', color='b', label='Total Rank')
    plt.plot(df['c'],  df['female_rank'], marker='o', linestyle='-', color='r', label='Female Rank')
    plt.title('Total vs Female rank')
    plt.xlabel('Year')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Frequency of the name 
    plt.figure(figsize=(6,6))
    plt.plot(df['c'],  df['freq_name'], marker='o', linestyle='-', color='b', label='Total Rank')
    plt.title('Frequency of "Maria" per year')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

    #plot newborns named Maria per thousand vs among females 
    plt.figure(figsize=(6,6))
    plt.plot(df['c'],  df['weight_1000_total'], marker='o', linestyle='-', color='b', label='Total newborns')
    plt.plot(df['c'],  df['weight_1000_female'], marker='o', linestyle='-', color='r', label='Female newborns')
    plt.title('Total vs Female newborns')
    plt.xlabel('Year')
    plt.legend()
    plt.tight_layout()
    plt.show()


## City with most Marias in Cataluña -- Counties
url_com = 'https://api.idescat.cat/onomastica/v1/nadons/dades.json?id=40683&lang=en&class=com'
response_com = requests.get(url_com)

if response_com.status_code==200: 
    data= response_com.json()
    records= data['onomastica_nadons']['ff']['f']
    df = pd.DataFrame(records)

    df['comarca_id']= df['c'].apply(lambda x: x['id'] if isinstance(x, dict) else None)
    df['comarca_content']= df['c'].apply(lambda x: x['content'] if isinstance(x, dict) else None)
    df['total_rank']= df['rank'].apply(lambda x: x['total'] if x['total'] != "_" else 0).astype(float)
    df['female_rank']= df['rank'].apply(lambda x: x['sex'] if x['sex'] != "_" else 0).astype(float)
    df['freq_name']= df['pos1'].apply(lambda x: x['v'] if x['v'] != "_" else 0).astype(float)
    df['weight_1000_total']= df['pos1'].apply(lambda x: x['w']['total'] if x['w']['total'] != "_" else 0).astype(float)
    df['weight_1000_female']= df['pos1'].apply(lambda x: x['w']['sex'] if x['w']['sex'] != "_" else 0).astype(float)
    
    df = df.drop(columns=['c', 'rank', 'pos1'], axis =1 )
    county_total = df[df['total_rank']==df['total_rank'].max()]['comarca_content'].values[0]
    county_female = df[df['female_rank']==df['female_rank'].max()]['comarca_content'].values[0]
    print( 'The county with more Marías born is: ', county_total)
    print( 'The county with more Marías born as female is: ', county_female)


## City with most Marias in Cataluña -- Provinces
url_prov= 'https://api.idescat.cat/onomastica/v1/nadons/dades.json?id=40683&lang=en&class=prov'
response_prov= requests.get(url_prov)

if response_prov.status_code==200: 
    data= response_prov.json()
    records= data['onomastica_nadons']['ff']['f']
    df = pd.DataFrame(records)

    df['comarca_id']= df['c'].apply(lambda x: x['id'] if isinstance(x, dict) else None)
    df['comarca_content']= df['c'].apply(lambda x: x['content'] if isinstance(x, dict) else None)
    df['total_rank']= df['rank'].apply(lambda x: x['total'] if x['total'] != "_" else 0).astype(float)
    df['female_rank']= df['rank'].apply(lambda x: x['sex'] if x['sex'] != "_" else 0).astype(float)
    df['freq_name']= df['pos1'].apply(lambda x: x['v'] if x['v'] != "_" else 0).astype(float)
    df['weight_1000_total']= df['pos1'].apply(lambda x: x['w']['total'] if x['w']['total'] != "_" else 0).astype(float)
    df['weight_1000_female']= df['pos1'].apply(lambda x: x['w']['sex'] if x['w']['sex'] != "_" else 0).astype(float)
    
    df = df.drop(columns=['c', 'rank', 'pos1'], axis =1 )
    county_total = df[df['total_rank']==df['total_rank'].max()]['comarca_content'].values[0]
    county_female = df[df['female_rank']==df['female_rank'].max()]['comarca_content'].values[0]
    print( 'The province with more Marías born is: ', county_total)
    print( 'The province with more Marías born as female is: ', county_female)

