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
        try:
            self.deposit = amount
            self.balance = self.balance + self.deposit
            print (f'Your balance is updated!\n Deposit amount: {self.deposit} \n Your balance is {self.balance}')
    
        except TypeError:
            print('please input number for balance')
        except ValueError:
            print('please input number for balance')
        except:
            print('there is something wrong')
    
    def withdraw(self, amount):
        try:
            self.withdraw = amount
            if (self.balance - self.withdraw >= 0):
                self.balance = self.balance - self.withdraw
                print(f'Withdraw success!\n Withdraw amount: {self.withdraw} \n Balance: {self.balance}')
            else:
                print('Your balance is not enough to do a withdrawal.')
        
        except TypeError:
            print('please input number for balance')
        except ValueError:
            print('please input number for balance')
        except:
            print('there is something wrong')

    def display_balance(self):
        print(f'Your balance is {self.balance}')

alex = BankAccount('Alex Smith', 1000)
alex.withdraw(500)
alex.deposit(2000)
alex.display_balance()
