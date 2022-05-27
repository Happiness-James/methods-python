class Bank:
    def __init__(self,accountname,accountnumber,pin,balance,amount):
        self.accountname = accountname
        self.accountnumber = accountnumber
        self.pin = pin
        self.balance = balance
        self.amount = amount
    def deposit(self):
        self.balance+=self.amount
        return f"Your balance is {self.balance}" 
    def withdraw(self):
        self.balance-=self.amount
        return f"Your balance is {self.balance}"       
           