class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Current Available balance is:{self.balance}")

    def withdrawal(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Your current balance is {self.balance}")
        else:
            print("!!!Current balance is lower than requested amount.!!!")

    def bankfees(self):
        if self.balance>0:
            bankfee=self.balance*0.05
            self.balance-=bankfee
            print(f"Bankfee {bankfee} and current balance is {self.balance}")

    def display(self):
        print(f'''
                Account Number: {self.accountNumber}\n
                Name:{self.name}\n
                Balance:{self.balance}
            ''')
        
obj=BankAccount(45214875520,"lokesh saini",25550)
obj.display()
obj.deposit(100)
obj.display()
obj.withdrawal(500)
obj.display()
obj.bankfees()
obj.display()
