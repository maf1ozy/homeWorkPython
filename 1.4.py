

def vvod():
    list=[]
    n=1
    while n:
        n=input("type something: ")
        if n:
            list.append(n)
    return list



list=vvod()
print("element  | chastota")
count=0
counted=[]
for elem in list:
    marker=1;
    for rep in counted:
        if elem == rep:
            marker=0
    if marker==0:
        continue
    for elem1 in list:
        if elem==elem1:
            count+=1
            counted.append(elem)
    print ("   ",elem,"   |  ", count)
    count=0