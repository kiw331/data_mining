Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def avg(*args):
    res = sum(args)/len(args)
    print(res)

avg(5, 3, 12, 9)
7.25
avg(2.4, 3.2, 7.3)
4.3
avg(10, 5)
7.5

import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]
SyntaxError: multiple statements found while compiling a single statement












import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]

SyntaxError: multiple statements found while compiling a single statement





import matplotlib.pyplot as plt
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]

plt.bar(x, y1, width=0.7, color ='blue')
<BarContainer object of 4 artists>
plt.bar(x, y2, width = 0.7, color ='red', bottom=y1)
<BarContainer object of 4 artists>
plt.bar(x, y3, width = 0.7, color ='green', bottom = bottom1)
<BarContainer object of 4 artists>

plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
plt.xlabel('Quarters')
Text(0.5, 0, 'Quarters')
plt.ylabel('sales')
Text(0, 0.5, 'sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x, xLabel, fontsize = 10)
([<matplotlib.axis.XTick object at 0x0000018B75D535B0>, <matplotlib.axis.XTick object at 0x0000018B75D53580>, <matplotlib.axis.XTick object at 0x0000018B75D52DA0>, <matplotlib.axis.XTick object at 0x0000018B75DD5060>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
plt.legend(['charirs', 'desks', 'goods'])
<matplotlib.legend.Legend object at 0x0000018B75DD5DE0>
plt.show()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    plt.show()
  File "C:\Users\kiw\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\pyplot.py", line 527, in show
    return _get_backend_mod().show(*args, **kwargs)
  File "C:\Users\kiw\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\backend_bases.py", line 3442, in show
    cls.mainloop()
  File "C:\Users\kiw\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\backends\backend_qt.py", line 593, in start_main_loop
    with _maybe_allow_interrupt(qapp):
  File "C:\Users\kiw\AppData\Local\Programs\Python\Python310\lib\contextlib.py", line 142, in __exit__
    next(self.gen)
  File "C:\Users\kiw\AppData\Local\Programs\Python\Python310\lib\site-packages\matplotlib\backends\qt_compat.py", line 230, in _maybe_allow_interrupt
    old_sigint_handler(*handler_args)
KeyboardInterrupt



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
SyntaxError: multiple statements found while compiling a single statement

import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]

plt.bar(x, y1, width=0.7, color ='blue')
<BarContainer object of 4 artists>
plt.bar(x, y2, width = 0.7, color ='red', bottom=y1)
<BarContainer object of 4 artists>
plt.bar(x, y3, width = 0.7, color ='green', bottom = bottom1)
<BarContainer object of 4 artists>

plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
plt.xlabel('Quarters')
Text(0.5, 22.440277777777773, 'Quarters')
plt.ylabel('sales')
Text(36.902777777777786, 0.5, 'sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x, xLabel, fontsize = 10)
([<matplotlib.axis.XTick object at 0x0000018B75D535B0>, <matplotlib.axis.XTick object at 0x0000018B75D53580>, <matplotlib.axis.XTick object at 0x0000018B75D52DA0>, <matplotlib.axis.XTick object at 0x0000018B75DD5060>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
plt.legend(['chairs', 'desks', 'goods'])
<matplotlib.legend.Legend object at 0x0000018B65899480>
plt.show()
plt.show()





import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]
x= range(len(y1))
bottom1 = [x+y for x,y in zip(y1,y2)]

plt.bar(x, y1, width=0.7, color ='blue')
<BarContainer object of 4 artists>
plt.bar(x, y2, width = 0.7, color ='red', bottom=y1)
<BarContainer object of 4 artists>
plt.bar(x, y3, width = 0.7, color ='green', bottom = bottom1)
<BarContainer object of 4 artists>

plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
plt.xlabel('Quarters')
Text(0.5, 0, 'Quarters')
plt.ylabel('sales')
Text(0, 0.5, 'sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x, xLabel, fontsize = 10)
([<matplotlib.axis.XTick object at 0x0000018B76F7EBF0>, <matplotlib.axis.XTick object at 0x0000018B76F7EBC0>, <matplotlib.axis.XTick object at 0x0000018B76F7E410>, <matplotlib.axis.XTick object at 0x0000018B76FE47C0>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
plt.legend(['chairs', 'desks', 'goods'])
<matplotlib.legend.Legend object at 0x0000018B77189C00>
plt.show()


print('hello")
      
