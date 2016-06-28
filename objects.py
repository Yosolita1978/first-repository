""" 
In this program I'm learning OOP starting with a class
"""

class Account(object):
    """
    This class is an example of management accounts in a bank
    """

    def __init__(self, name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return "Cuenta de %s con un balance de %d." %(self.name, self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        return True


class AccountMinimunBalance(Account):
    
    def __init__(self, name, balance, minimun):
        self.name = name
        self.balance = balance
        self.minimun = minimun
        if balance < minimun:
            print "Your account needs a minimun balance"

    def withdrawal(self, amount):
        new_balance = self.balance - amount
        if new_balance < self.minimun:
            return False
        else:
            self.balance = new_balance
            return True

def transfer(source, destination, amount):
    if source.withdrawal(amount):
        destination.deposit(amount)    
    else:
        print "Transfer Fail"

def main():
    account_1 = Account("Juan",500)
    account_2 = AccountMinimunBalance("Pedro",1000, 500)
    transfer(account_2, account_1, 300)
    transfer(account_2, account_1, 300)
    print account_1
    print account_2



if __name__ == '__main__':
    main()