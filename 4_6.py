#原代码的问题：list.pop(idx)在迭代中会改变列表的长度
#在每一次迭代后，原来的奇数位会变成偶数位，而偶数位会变成奇数位
if __name__=='__main__':
    list = list(range(1000))
    for idx in range(len(list)-1,-1,-1):
        if list[idx]%2==1:
            list.pop(idx)
    print(list)