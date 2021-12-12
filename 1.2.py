def season(n):
    seas = int(n)//3
    index = ""
    if seas == 2:
        index = "Лето"
    elif seas == 3:
        index = "Осень"
    elif seas == 4 or seas == 0:
        index = "Зима"
    elif seas == 1:
        index = "Весна"
    return index


a = input("Введите число от 1 до 12:")
print(season(a))
