# Task :
#
# Write a class for banking scenario that deposits or withdraws money for a given
# bank account.


class Bank:
    deposit_money = 0
    withdraw_money = 0
    total_money = 0
    money_entered = 0

    def __init__(self,money):
        self.money = money

    def counter(self):

        print(f'******************* MENU *******************')
        print(f'Press 1 : DEPOSIT MONEY')
        print(f'Press 2 : WITHDRAW MONEY')
        print(f'Press 3 : DISPLAY BALANCE and EXIT')
        print(f'********************************************')

        choice = int(input('Enter your Choice : '))
        Bank.total_money += self.money

        while(choice < 1 and choice > 3):
            print('Wrong Choice Entered... TRY AGAIN')
            choice = int(input('Enter your Choice : '))

        while(choice != 3):
            if(choice == 1):
                Bank.deposit_money = int(input('Enter Money to Deposit : '))
                Bank.total_money += Bank.deposit_money

            if(choice == 2):
                Bank.withdraw_money = int(input('Enter Money to Withdraw : '))
                if(Bank.total_money > Bank.withdraw_money):
                    Bank.total_money -= Bank.withdraw_money
                else:
                    print('Not Enough Money to withdraw')

            choice = int(input('Enter your Choice : '))

        print(f'Your Total Money : {Bank.total_money}')


money = int(input('Enter Initial Amount to Deposit in your Account : '))
my_obj = Bank(money)
my_obj.counter()
