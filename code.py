#Bank operation using OOP

class Bank:
    bankname="STATE BANK OF INDIA"
    branch="ERAMALOOR,RR TOWER,CHERTHALA,ALAPPUZHA,INDIA"

    #create account
    def __init__(self,account,IFSC,date,username,father,pan,adhar,address,email,phone):
        self.account=account
        self.account=account
        self.IFSC=IFSC
        self.username=username
        self.father=father
        self.pan=pan
        self.adhar=adhar
        self.address=address
        self.email=email
        self.phone=phone
        self.balance=0.0 # set account balance to 0.0
        print(f'Hello {self.username} cong! your account craeted successfully ')

    #depoist
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully')

    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficent Fund...')

    #ministatement
    def ministatement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname} , {Bank.branch}')
#collect user data for account creation
account=input('Enter your account type : ')
account=input('Enter your account number : ')
IFSC=input('Enter your IFSC code : ')
date=input('Enter your account openings date : ')
username=input('Enter Your name :')
father=input('Enter your father name : ')
pan=input('Enter pan card number : ')
adhar=input('Enter your adhar card number : ')
address=input('Enter Your address : ')
email=input('Enter your email id : ')
phone=input('Enter your phone number : ')

b=Bank(account,IFSC,date,username,father,pan,adhar,address.email,phone) # object creation based on user provided data

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option=int(input(' '))

    if option==1:
        amount=float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option==2:
        amount=float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option==3:
        b.ministatement()

    elif option==4:
        print('Thanks for using Indian Express Bank .... ')
        break
    else:
        print('Invalid Option plz select a  valid option')
