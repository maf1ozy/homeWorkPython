def func1():
    spisok = []
    n = 1
    while n:
        n = input("Введите что-нибудь: ")
        if n == '' or n == ' ':
            break
        spisok.append(n)

    return spisok


print(func1())
