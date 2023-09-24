# Bar 차트에서 3개의 데이터를 누적해서 표현
import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]

plt.bar(x, y1, width=0.7, color ='blue')
plt.bar(x, y2, width = 0.7, color ='red', bottom=y1)
plt.bar(x, y3, width = 0.7, color ='green', bottom = bottom1)

plt.title('Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x, xLabel, fontsize = 10)
plt.legend(['chairs', 'desks', 'goods'])
plt.show()
