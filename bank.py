class Bank:
    def __init__(self,accountname,accountnumber):
        self.accountname = accountname
        self.accountnumber = accountnumber
        self.balance = 0  
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be positive"
        else: 
            self.balance+=amount   
            return f"Hello {self.accountname} Your balance is {self.balance}"    
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Hello {self.accountname} Your balance is {self.balance} you can't withdraw {amount}"
        elif amount<=0:
            return f"Hello {self.accountname} The amount should be positive" 
        else:       
            self.balance-=amount
            return f"Hello, {self.accountname} You have withdraw {amount} and your new balance is {self.balance}"       
           