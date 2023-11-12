'''
Bank System
If you want to create an account in the id parameter add "None"
A -> Account Creation
D -> Deposit
W -> Withdraw
C -> Check Balance
'''
import random
import string
global IDS
global NAMES

IDS=[]
NAMES=[]
class Bank:
    def __init__(self,user_name,id):
        self.user_name=user_name
        self.id=id

    def account_create(self):
        code=""
        name_of_account=raw_input("Input a name of the account that you want to create: ")
        NAMES.append(name_of_account)
        for i in range(12):
            code+=str(random.randint(0,9))
        IDS.append(code)
        print "Your account ID is",code,"with account name",name_of_account
        
    def deposit(self):
        global money_deposited
        money_deposited=[]
        money=input("Add the amount of money that you want to deposit: ")
        while money < 10:
            print "You need to deposit more than 10$"
            exit_bank=raw_input("Do you wish to exit the bank or do you want to deposit more money?\nAnswer with an 'E' for exit and a 'D' for deposit")
            while exit_bank not in ["E","D"]:
                print "Invalid Input"
                exit_bank=raw_input("Do you wish to exit the bank or do you want to deposit more money?\nAnswer with an 'E' for exit and a 'D' for deposit")
            if exit_bank == "E":
                quit()
            else:
                money=input("Add the amount of money that you want to deposit: ")
            money_deposited.append(money)
            print "Money deposited in ID",self.id,"with user name",self.user_name

    def withdraw(self):
        if self.id in IDS:
            amount=input("Give me the amount of money that you want to withdraw ")
            while amount <= 0:
                print "Negative number or 0 given"
                amount=input("Give me the amount of money that you want to withdraw ")
        else:
            print "Your id does not belong in our id list\nYou should consider making an account"

    def check_balance(self):
        if self.id in IDS:
            pos=-1
            i=0
            while i < len(money_deposited) and pos == -1:
                if self.id == money_deposited[i]:
                    pos = i
                else:
                    i+=1
            print "Your total balance is ",money_deposited[pos]
        else:
            print "Your id does not belong in our id list\nYou should consider making an account"
B=Bank(None,None)
A=B.account_create()
D=B.deposit()
W=B.withdraw()
C=B.check_balance()


while True:
    print "A -> Account Creation\nD -> Deposit\nW -> Withdraw\nC -> Check Balance"
    action=raw_input("Give me what action you want to perform in your account: ")
    if action not in ["A","D","W","C"]:
        print "Invalid Action"
        action=raw_input("Give me what action you want to perform in your account: ")
    if action == "A":
        id=None
    else:
        user_name=raw_input("Give me your name: ")
        id=input("Write your id: ")
        

        
            
