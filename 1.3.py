def fibb(n):
    list = []
    i = int(n)
    temp = 0
    last = 0
    new = 1
    while i != 0:
        i -= 1
        temp = new
        list.append(last)
        new = last+new
        last = temp

    print("first", n, "number(s) of Fibonacci's numbers: ")
    return list


a = input("Put the number of members Fibonacci's numbers: ")
print(fibb(a))
