
import pandas as pd

df = pd.DataFrame([[490, 201, 0], 
                   [366, 197, 0], 
                   [863, 7993, 288]], 
                  index = ['교수', '직원', '학생'], 
                  columns = ['찬성', '반대', '무효'])

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontpath = r'C:\Windows\Fonts\malgunsl.ttf'
font_name = fm.FontProperties(fname=fontpath, size=50).get_name()
plt.rc('font', family=font_name)

df.plot(kind='barh', stacked=True)
plt.title('글로컬대학30(대학통합) 관련 투표 결과')
plt.xlabel('Count')
plt.ylabel('Position')
plt.legend(title='투표 옵션')
plt.show()
