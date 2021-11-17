def Fibbonaci(n):
    q = n
    res=[]
    last=0
    new=1
    while q!=0:
        res.append(last)
        temp=new
        new=new+last
        last=temp
        q-=1
    return res;


a=input("Введите желаемое количество членов последовательности: ")
print(Fibbonaci(a))