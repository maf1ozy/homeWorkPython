class Date:
    year = 0
    month = 0
    day = 0

    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def selfinput(self):
        self.day = input("Введите день: ")
        self.month = input("Введите месяц: ")
        self.year = input("Введите год: ")

    def displaydate(self):
        print("Год: ", self.year)
        print("Месяц: ", self.month)
        print("День: ", self.day)


date1 = Date(2021, 11, 24)
date1.displaydate()
date1.selfinput()
date1.displaydate()
