import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('data/ch4_07.csv', encoding='utf-8')
#df = pd.read_csv('C:/Users/kiw/github_15zd/data_mining/data/ch4_07.csv', encoding='utf-8')

    
quarters = ['first', 'second', 'third', 'fourth']
years = df.index

for year in years:
    plt.plot(quarters, df.loc[year].tolist(), label=year)   

         
plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.legend(['2015', '2016', '2017', '2018', '2019', '2020'])
plt.show()