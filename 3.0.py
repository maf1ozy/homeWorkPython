class Date:
    year = 0
    month = 0
    day = 0

    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def selfinput(self):
        self.day = int(input("Input day: "))
        self.month = int(input("Input month: "))
        self.year = int(input("Input year: "))

    def displaydate(self):
        print("Day: ", self.day)
        print("Month: ", self.month)
        print("Year: ", self.year)


date1 = Date(2021, 11, 24)
date1.displaydate()
date1.selfinput()
date1.displaydate()
