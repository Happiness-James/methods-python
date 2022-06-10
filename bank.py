class Account:
    def __init__(self,accountname,accountnumber):
        self.accountname = accountname
        self.accountnumber = accountnumber
        self.balance = 0  
        self.deposits = []
        self.withdrawals = []
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be positive"
        else: 
            self.balance+=amount
            self.deposits.append(amount)
            print(f"Hello {self.accountname} Your balance is {self.balance} you have deposited {self.deposits}")   
                    

    def withdraw(self,amount):
        self.transaction_fee = 100
        if amount>self.balance:
            return f"Hello {self.accountname} Your balance is {self.balance} you can't withdraw {amount}"
        elif amount<=0:
            return f"Hello {self.accountname} The amount should be positive" 
        else:       
            self.balance-=amount+self.transaction_fee
            self.withdrawals.append(amount)
            return f"Hello, {self.accountname} You have withdraw {amount} with a {self.transaction_fee}and your new balance is {self.balance}"
    def deposits_statement(self):
        for i in self.deposits:
            print(i,end="\n")   

    def withdrawals_statement(self):
        for x in self.withdrawals:
            print(x, end="\n")  
    def current_balance(self):
        return self.balance         

           