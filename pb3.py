class Bankaccount():
    def __init__(self,name,number,balance):
    
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self):
        amount=float(input("enter amount to deposite :"))
        self.balance= self.balance + amount
        return self.balance
    def withdrawl(self):
       # if self.balance>1.00:
            cash=float(input("enter amount to withdraw:"))
            balance=self.balance-cash
            return balance
    
o=Bankaccount("suresh",123456789101,0.00) 
print(" Name:",o.name)
print(" acc.noo:",o.number)
print("balance:",o.balance)
print("total balance",o.deposit())
print("total balance",o.withdrawl())
        
