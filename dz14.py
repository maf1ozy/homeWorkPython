from first import func1

list = func1()
print("element  |  chastota")
counted = []
for elem in list:
    marker = 1;
    for rep in counted:
        if elem == rep:
            marker = 0
    if marker == 0:
        continue
    for elem1 in list:
        if elem == elem1:
            counted.append(elem)
    print ("   ", elem, "  |  ", list.count(elem))
