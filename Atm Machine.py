import time
import random
print("Welcome to ICICI Bank...!!")
print()
print("Pls insert the card.......");print("---------------------------")
class ATM:
    def __init__(self):
        print("Plese select the option".center(35))
        print()
        print("1. Balance Enquiry");print("2. Withdrawl");print("3. Pin Change")
        print("4. Fast cash");print("5. Open Fixed Deposit Account");print("6. Fund Transfer")
        self.cash = 20000;self.pin = 1432
    def balance(self):
        print("---------------------------")
        print("Your Balance is :",float(self.cash)," |")
        print("---------------------------")
    def withdraw(self):
        w_cash = int(input("Please Enter the withdraw Amount: "))
        if w_cash > self.cash:
            print("Insufficent Balance...!!!")
        else:
            self.cash = self.cash-w_cash
            print("Remaining Balance is:",self.cash)
    def pin_change(self):
        print("1. Generate pin");print("2. Change pin")
        option = int(input("Choose the option: "))
        class Dice:
                globals()
                def roll(self):
                    first = random.randint(0,9);second = random.randint(0,9);three = random.randint(0,9)
                    four = random.randint(0,9);five = random.randint(0,9);six = random.randint(0,9)
                    return (first,second,three,four,five,six)
                def otp(self):
                    #validate = input("Click on submit Button: ")
                    validate = "submit"
                    first = time.time()
                    if validate == "submit":
                        otp = obj.roll()
                        otp=list(otp)
                        string = ""
                        for i in otp:
                            string+=str(i)+""
                        print(string)
                    enter = input("Enter the Validate OTP: ")
                    print()
                    if string == enter:
                        time1 = time.time() - first
                        if time1<=30:
                            print("OTP is Validate Successfully.....!!!".center(50))
                            print("Welcome to Python World".center(50))
                        else:
                            print("OTP is Not Valid.......!!!!!!!!")
                    else:
                        print("Entered Wrong OTP Please try again....!!!!!!")
        if option ==1:
            obj = Dice()
            obj.otp()
            n_pin = int(input("Enter the new pin number: "))
            n_pin2 =int(input('Please conform your pin number: '))
            if n_pin ==n_pin2:
                if len(str(n_pin)) == 4:
                    self.pin = n_pin
                    print("Pin change succesfully....!!!!")
                    check = input("If you want validate new pin Y/N").casefold()
                    if check == "y":
                        obj1.info()
                    elif check =="n":
                        exit()
                    else:
                        print("Choose Valid option...!!!")
                else:print("Please Enter vlid pin...!!!")
            else:print("Your pin does not match please try again later....")
        elif option ==2:
            o_pin = int(input("Enter the pin Number: "))
            if o_pin == self.pin:
                n_pin = int(input("Enter the new pin number: "))
                if len(str(n_pin)) == 4:
                    self.pin = n_pin
                    print("Pin change succesfully....!!!!")
                    check = input("If you want validate new pin Y/N").casefold()
                    if check == "y":
                        obj1.info()
                    elif check =="n":
                        exit()
                    else:
                        print("Choose Valid option...!!!")
                else:print("Please Enter vlid pin...!!!")
            else:
                print('Enter the valid pin')
    def fast_cash(self):
        dic= {1:1000,2:2000,3:5000,4:10000,5:20000}
        for k,v in dic.items():
            print(k,". ",v)
        option = int(input('select the withdraw amount: '))
        if option == len(dic):
            value = dic.get(option)
            if value > self.cash:
                print("Insufficent Balance...!!!")
            else:
                self.cash = self.cash-value
                print("Remaining Balance is:",self.cash)
        else:
            print("Please choose correct option...!!")
    def account_opening(self):
        print("1. Online");print("2. Offline")
        option=int(input("Enter the Option: "))
        if option == 1:
            contact = int(input('Enter the contact Number: '))
            class Dice:
                def __init__(self):pass
                    # super().__init__()
                globals()
                def roll(self):
                    first = random.randint(0,9);second = random.randint(0,9);three = random.randint(0,9)
                    four = random.randint(0,9);five = random.randint(0,9);six = random.randint(0,9)
                    return (first,second,three,four,five,six)
                def otp(self):
                    #validate = input("Click on submit Button: ")
                    validate = "submit"
                    first = time.time()
                    if validate == "submit":
                        otp = obj.roll()
                        otp=list(otp)
                        string = ""
                        for i in otp:
                            string+=str(i)+""
                        print(string)
                    enter = input("Enter the Validate OTP: ")
                    print()
                    if string == enter:
                        time1 = time.time() - first
                        if time1<=30:
                            print('Validation Successfully Completed...!!'.center(40))
                            print()
                            name = input("Enter the Name: ")
                            male = input("Select the option M/F").upper()
                            adhar = int(input("Enter the Adhar Number:"))
                            pan = input("Enter the pan card Number: ")
                            amount  = int(input("Enter the Fixed deposit Amount: "))
                            print("Select the Duration :");print("1. 12 months");print("2. 24 months")
                            option = int(input("Select the option: "))
                            if option ==1:
                                duration = 12
                                print('Intrest rate is : 30%')
                            elif option ==2:
                                duration =24
                                print('Intrest rate is : 45%')
                            print("Select your Payment method....!!!");print("1. Online");print("2. Debit/Credit Card")
                            pay_type = int(input("Choose your option:"))
                            if pay_type == 1:
                                user_name = input("Enter User name: ")
                                password = input('Enter your Password: ')
                                print("After cmp Transation ......")
                                print("Your transaction successfully completed..!!!!!")
                                first = random.randint(11111111111,99999999999)
                                print("Your account Number is: ",first);print("aditional Information send to your registered mobile number...")
                            elif pay_type ==2:
                                card_no = int(input("Enter your Card Details: "))
                                e_date = int(input("Enter your expire date: "))
                                cvv = int(input("Enter your CVV number: "))
                                name= input("Enter card holder Name: ")
                                print("Your transaction successfully completed..!!!!!")
                                first = random.randint(11111111111,99999999999)
                                print("Your account Number is: ",first);print("aditional Information send to your registered mobile number...")
                            else:print('Select the Valid option..!!!')
                        else:
                            print("OTP is Not Valid.......!!!!!!!!")
                    else:
                        print("Entered Wrong OTP Please try again....!!!!!!")
            obj = Dice()
            obj.otp()
        elif option ==2:
            name = input('Enter your Name: ')
            male = input("Select the option M/F").upper()
            contact = int(input('Enter your Contct mobile Number: '))
            contact2 = int(input("Enter your Contct temporary Number: "))
            if len(str(contact)) ==10 and len(str(contact2)) ==10:
                if contact != contact2:
                    if male == "M":
                        print("Mr.",name,'Thank you for intrest ICICI Bank....!!!')
                    elif male == "F":
                        print("Miss.",name,'Thank you for intrest ICICI Bank....!!!');print("Our Executive will be contact shortly...")
                else:print("Please enter different two numbers..")
            else:print("Enter valid Contact Number..!!!")

    def fund_transfer(self):
        print("1. icici bank");print("2. Other banks")
        option = int(input("Choose option: "))
        if option ==1:
            acc_no = int(input("Enter the account Number: "))
            ifsc = input("Enter the IFSC code: ")
            amount = int(input("enter the Trnsfer amount: "))
            if w_cash > self.cash:
                print("Insufficent Balance...!!!")
            else:
                self.cash = self.cash-w_cash
                print("Remaining Balance is:",self.cash)
                print("Your transaction is succesfully completed")
        elif option ==2:
            acc_no = int(input("Enter the account Number: "))
            ifsc = input("Enter the IFSC code: ")
            amount = int(input("enter the Trnsfer amount: "))
            bank = input("Enter the Bank Name: ")
            if w_cash > self.cash:
                print("Insufficent Balance...!!!")
            else:
                self.cash = self.cash-w_cash
                print("Remaining Balance is:",self.cash)
                print("Your transaction is succesfully completed")
        else:
            print("Please select valid option...!!!")
class customer(ATM):
    def __init__(self):
        super().__init__()
    def info(self):
        e_pin = input("Enter the pin Number: ")
        if len(e_pin) == 4:
            if int(e_pin) == self.pin:
                print("1. Savings Account");print("2. Current Account")
                a_type = int(input("Please Select  the Type:  "))
                if a_type ==1:pass
                elif a_type ==2:pass
                else:print("Please select Valid option...!!!");exit()
                option = int(input("Please Select  the option:  "))
                if option ==1:self.balance()
                elif option ==2:self.withdraw()
                elif option ==3:self.pin_change()
                elif option ==4:self.fast_cash()
                elif option ==5:self.account_opening()
                elif option ==6:self.fund_transfer()
            else:
                print("Please Enter the Valid Pin...!!!");print("Yhank you for visiting ICICI Bank.....!!!".center(50))
        else:
                print("Please Enter the Valid Pin...!!!");print("Yhank you for visiting ICICI Bank.....!!!".center(50))

obj = ATM()
print("---------------------------")
obj1 = customer()
obj1.info()

