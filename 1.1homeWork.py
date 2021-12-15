def func1():
    list = []
    n = input("Введите что-нибудь: ")
    while n:
        list.append(n)
        n = input("Введите что-нибудь: ")
    return list


print(func1())
