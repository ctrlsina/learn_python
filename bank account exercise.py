class BankAccount:
    def __init__(self, account_holder, initial_balance =0.0):
        try:
            self.balance = initial_balance
            float(self.balance)
            self.account_holder = account_holder
            print(f'Account creation success! here is your info: \n Account Name : {self.account_holder} \n Balance: {self.balance}')
        except TypeError:
            print('please input a number for balance')
        except ValueError:
            print('please input a number for balance')
        except:
            print('there is something wrong')
    
    def deposit(self,amount):
        '''Add amount to balance'''
        try:
            if amount >= 0:
                self.balance += amount
                print (f'Your balance is updated!\n Deposit amount: {amount} \n Your balance is {self.balance}')
            elif amount < 0:
                print('Please input positive number')
        except TypeError:
            print('please input number for balance')
        except ValueError:
            print('please input number for balance')
    
    def withdraw(self, amount):
        '''Subtract amount to balance'''
        try:
            if (self.balance - amount >= 0) and amount > 0:
                self.balance -= amount
                print(f'Withdraw success!\n Withdraw amount: {amount} \n Balance: {self.balance}')
            elif amount < 0: #To check amount withdrawed is positive number
                print('Please input positive number')
            elif self.balance - amount < 0: #to check if the remaining balance >= 0
                print('Your balance is insufficient')
        except TypeError:
            print('please input number for balance')
        except ValueError:
            print('please input number for balance')

    def display_balance(self):
        '''Display current balance'''
        print(f'Your balance is {self.balance}')

alex = BankAccount('Alex Smith', 1000)
alex.withdraw(500)
alex.deposit(2000)
alex.display_balance()
