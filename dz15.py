from first import func1

def avrg(nums):
    return sum(nums)/len(nums)


list = func1()
numbers = [int(elem) for elem in list]
res = avrg(numbers)
print("Srednee arifmeticheskoe = ", res)
