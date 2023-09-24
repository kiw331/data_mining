# 매개변수에 대한 평균을 구한 뒤 출력하는 avg() 함수

def avg(*args):
    res = sum(args)/len(args)
    print(res)
    
    
    
    
avg(5, 3, 12, 9)
avg(2.4, 3.2, 7.3)
avg(10, 5)