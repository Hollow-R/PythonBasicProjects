name = input("Name :")
surname = input("Surname :")
balance = int(input("Balance :"))

class Customer(object):

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def withdrawMoney(self, amount):
        if amount > self.balance:
            raise RuntimeError("Insufficient Balance !")
        self.balance -= amount
        self.showInfo()
        return self.balance

    def depositMoney(self, amount):
        self.balance += amount
        self.showInfo()
        return self.balance

    def showInfo(self):
        print(self.name + ", your balance is >>" + str(self.balance) + " Dolar .")

customer1 = Customer(name + " " + surname, balance)

procedure = input("Chose Procedure\nWithdraw : 1\nDeposit : 2\n")

if procedure == "1":
    cek = float(input("Enter the amount\n"))
    customer1.withdrawMoney(cek)
elif procedure == "2":
    yatır = float(input("Enter the amount.\n"))
    customer1.depositMoney(yatır)