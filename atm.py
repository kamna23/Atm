#small atm project on python
#in this project we form a atm in which if pin is equal to passard then we can perform 4 tasks that is check balance,withdraw money,add money in bank or exit fro88pm bank
import time
print("Please insert your CARD")
time.sleep(5)
passward=1234
pin=int(input("Enter your atm pin"))
balance= 5000
if pin==passward:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
        """
        )
        try:
            option=int(input("Please enter your choice\n"))
        except:
            print("please enter valid option")
        if option==1:
            print(f"Your current balance is {balance}")
            print("=========================================================")
            print("=========================================================")
            print("=========================================================")
        if option==2:
            withdraw_amount=int(input("Please enter withdraw amount\n"))
            print("=========================================================")
            print("=========================================================")
            print("=========================================================")
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print("=========================================================")
            print("=========================================================")
            print(f"Your updated balance is {balance}")
            print("=========================================================")
            print("=========================================================")
        if option==3:
            deposit_amount=int(input("Please enter deposit amount \n"))
            print("=========================================================")
            print("=========================================================")
            print("=========================================================")
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited from your account")
            print("=========================================================")
            print("=========================================================")
            print(f"Your updated balance is {balance}")
            print("=========================================================")
            print("=========================================================")
        if option==4:
            break
else:
    print("wrong pin Please try again")
