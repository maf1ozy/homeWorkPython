#user inputs text. show biggest word and most used word
def divide(txt):
    list = []
    word = ''
    for letter in txt:
        if letter !=' ':
            if letter == txt[len(txt)-1]:
                word+=letter
                list.append(word)
            else:
                word += letter
        else:
            list.append(word)
            word=''
    return list

def biggest(l):
    biggest=''
    for word in l:
        if len(word) > len(biggest):
            biggest = word
    return biggest

def mostUsed(l):
    max=''
    maxCounter=0
    counter=0
    for word in l:
        for word1 in l:
            if word1==word:
                counter+=1
        if counter>maxCounter:
            max=word
    return max


text = input("input your text: ")
list=divide(text)
biggestValue=biggest(list)
mostUsedValue=mostUsed(list)
print("Samoe dlinnoe:",biggestValue,"| Samoe chastoe:", mostUsedValue)