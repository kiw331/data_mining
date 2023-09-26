#2022 전정대, 경영대, 사과대 학과별 재학생
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

# csv파일 불러오기
file_path = 'C:/Users/kiw/github_15zd/data_mining/data/충북권 대학 등록금.csv' 
df = pd.read_csv(file_path, encoding='utf-8')

fontpath = 'C:/Windows/Fonts/malgunsl.ttf'
font_name = fm.FontProperties(fname=fontpath, size=50).get_name()
plt.rc('font', family=font_name)

# 국립 대학과 사립 대학 데이터 분리
national = df[df['구분'] == '국립']['등록금']
private = df[df['구분'] == '사립']['등록금']

# 박스 플롯 그리기
fig, ax = plt.subplots()
ax.boxplot([national, private], labels=['국립 대학', '사립 대학'])
ax.set_title('충북권 대학 등록금 박스 플롯')
ax.set_ylabel('등록금 (백만원)')

plt.show()





