def whatNumber(n):
    marker = True
    if n == 1 or n == 0:
        return False
    for num in range(n):
        if num != 0 and num != 1 and num != n and n%num == 0:
            marker = False

    return marker

a = input("put your number: ")
print(whatNumber(int(a)))
