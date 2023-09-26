#2022 전정대, 경영대, 사과대 학과별 재학생
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd


file_path = 'C:/Users/kiw/github_15zd/data_mining/data/충북권 대학 등록금.csv' 
df = pd.read_csv(file_path, encoding='utf-8')

fontpath = 'C:/Windows/Fonts/malgunsl.ttf'
font_name = fm.FontProperties(fname=fontpath, size=50).get_name()
plt.rc('font', family=font_name)

data_his = df['등록금']

plt.hist(data_his, bins = [3000000, 4000000, 5000000, 6000000, 7000000, 8000000], edgecolor='white')

# 히스토그램 그리기
plt.title('충북권 대학 등록금 히스토그램')
plt.xlabel('등록금 (백만원)')
plt.ylabel('학교 수')

# 그래프 표시
plt.show()





