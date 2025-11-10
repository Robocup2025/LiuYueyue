import random
import statistics

def f():
    data = []
    for i in range(10):
        x=[random.randint(1,100) for i in range(3)]
        data.append(x)
    f=open('data.csv','w')
    for x in data:
        f.write(','.join(map(str,x))+'\n')
    row_two=[x[1] for x in data]
    results={
        '最大值:':max(row_two),
        '最小值:':min(row_two),
        '平均值:':sum(row_two)/len(row_two),
        '中位数:':statistics.median(row_two),
    }
    return results

if __name__=='__main__':
    result=f()
    for k,v in result.items():
        print(k,v)