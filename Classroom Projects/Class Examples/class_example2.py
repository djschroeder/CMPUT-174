class Account:
    def __init__(self,acc_id,acc_balance):
        # initializes the instance attributes
        # acc_id is of type str represents the account number
        # acc_balance is of type float represents the amount
        self.account_id = acc_id
        self.balance = acc_balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
    def display(self):
        print('Account :' + self.account_id + '  Amount :' + str(self.balance))
    def transfer(self,account_to,transfer_amount):
        self.withdraw(transfer_amount)
        account_to.deposit(transfer_amount)
        
def main():
    accountA = Account('0123',1200)
    accountA.deposit(500)
    accountA.deposit(500)
    accountA.withdraw(200)
    accountA.display()
    accountB = Account('0456',200)
    accountB.deposit(500)
    accountB.withdraw(100)
    accountB.display()
    accountA.transfer(accountB,500)
    print('After transfer:')
    accountA.display()
    accountB.display()
    
main()