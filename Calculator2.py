class calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print("{} + {} = ".format(self.num1, self.num2),self.num1 + self.num2)
    def sub(self):
        print("{} - {} = ".format(self.num1, self.num2),self.num1 - self.num2)
    def mult(self):
        print("{} x {} = ".format(self.num1, self.num2),self.num1 * self.num2)
    def div(self):
        print("{} / {} = ".format(self.num1, self.num2),self.num1 / self.num2)
    
num1 = float(input("Enter a Number: "))
num2 = float(input("Enter another Number: "))

c1 = calc(num1, num2)

c1.add() 
c1.sub()
c1.mult()
c1.div()





