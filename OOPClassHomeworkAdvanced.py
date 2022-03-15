import sys

## CLASSES ##

class Account():
    account_user_pass = {'admin':'password' , 'Fred':'swordfish123'}
    account_list = ['admin','Fred']
    def __init__(self,owner,password,deposit=0):     #owner expects string, desposit expects int or nothing
        self.owner = owner
        self.balance = 0 + deposit      #sets 'balance' attribute to be equal to 0 by default, and equal to the first deposit, if there is one
        print(f"Account created for user {self.owner}!")
        print(f"Starting balance is ${self.balance}.")
        Account.account_user_pass[f'{owner}'] = f'{password}'
        Account.account_list.append((f'{owner}',f'{password}'))
    def __str__(self):
        return self.owner
    def __int__(self):
        return self.balance
    def deposit(self):
        print(f"You are attempting to deposit ${amount}.")
        self.balance = self.balance + amount
        print(f"Success! Your new balance is ${self.balance}.")
        return self.balance
    def withdraw(self,amount):
        print(f"You are attempting to withdraw ${amount}. Your account has ${self.balance}.")
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Success! Your new balance is ${self.balance}.")
            return True
        else:
            print("Error! You cannot withdraw more money than you have!")
            return False
    def balanceCheck(self):
        print(f"Your current balance is {self.balance}.")
        return self.balance
    def createAccount(cls):
        while True:
            try:
                new_acct_name = str(input())
            except:
                print("You've typed an invalid account name. Please try again.")
                continue
            if new_acct_name not in account_list:       ##verifies that acct name is unique
                print("Success! That is a valid account name.")
            else:
                break
        while True:
            try:
                new_acct_pass = str(input())
            except:
                print("That is an invalid password. Please try again.")
            print("That is a valid password!")
        while True:
            try:
                new_acct_bal = int(input())
            except:
                print:("You've typed an invalid balance. Please try again.")
                continue
            print("Success! You've typed a valid balance!")
            print("Account creating...")
        return


## FUNCTIONS ##

def chooseAction(*args):
    while True:
        for i in args[2:]:
            print(i)
        print(f"Please input an integer between {args[0]} and {args[1]}, inclusive.")
        try:
            user_input = int(input())
        except:
            print("ERROR: Non integer typed.")
            continue
        if user_input == 'stop':
            break
        elif int(user_input) >= args[0] and int(user_input) <= args[1]:
            return user_input
        else:
            print(f"ERROR: You must type any integer between {args[0]} and {args[1]}, inclusive.")
            continue

##def userLogin(user,pass):


## DEFAULT VARIABLE VALUES ##

take_an_action = True
attempt_check_balance = False
attempt_withdraw = False
attempt_deposit = False
selected_action = 0       #   0 == do nothing without exiting; 1 == login; 2 == create acct; 3 == check balance; 4 == attempt withdrawl; 5 == deposit

## USERDATA ##

admin = Account('admin','password',0)
Fred = Account('Fred','swordfish123',200)
current_account = ''  ##SET TO NULL

##      CODE BEGINS     ##




while take_an_action is True:
    if current_account == False:
        chooseAction("You must sign in before using TeleScam Banks Services!","Please type (1) to login, or (2) to create an account.")
    else:
        selected_action = chooseAction(0,3,"Which action would you like to take?","You can check your balance (1), attempt a withdrawl (2), make a deposit (3), or do nothing (0).")
        if selected_action == 1:
            Account.balanceCheck(Fred)
        elif selected_action == 2:
            Account.withdraw(Fred)
        elif selected_action == 3:
            Account.deposit(Fred)
        elif selected_action == 0:
            print("Thank you for your patronage!")
            take_an_action == False
        else:
            print("It shouldn't be possible to see this message. Please report this error.")
            continue

print("Thank you for your patronage")
sys.exit()

#withdraw_attempt = False
#deposit_attempt = False
#while not deposit_attempt:
