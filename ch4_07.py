import pandas as pd

df = pd.DataFrame([[500, 450, 520, 610], 
                   [690, 700, 820, 900], 
                   [1100, 1030, 1200, 1380], 
                   [1500, 1650, 1700, 1850], 
                   [1990, 2020, 2300, 2420], 
                   [1020, 1600, 2200, 2550]], 
                  index = ['2015년', '2016년', '2017년', '2018년', '2019년', '2020년'], 
                  columns = ['1분기', '2분기', '3분기', '4분기'])


df.to_csv('data/ch4_07.csv', encoding='utf-8-sig')
#df.to_csv('C:/Users/kiw/github_15zd/data_mining/data/ch4_07.csv', encoding='utf-8-sig')

