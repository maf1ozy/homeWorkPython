def vvod():
    list=[]
    n=1
    while n:
        n=input("put your number: ")
        if n:
            list.append(int(n))
    return list

def avrg(lis):
    spisok=lis
    counter=0
    sum=0
    for ele in spisok:
        sum+=ele
        counter+=1
    res = sum/counter
    return res

list=vvod()
res = avrg(list)
print("Srednee arifmeticheskoe = ",res)