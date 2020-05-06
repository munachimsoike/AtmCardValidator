import re
import random
import string


# Validating email
def check_email(email):
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if(re.search(regex,email)):  
        print("Valid Email")
        return True         
    else:  
        print("Invalid Email, Fill-in valid email") 
        return False


def acct_number():
    accountNumber = ("30" + str(random.randint(10,999999999)))
    print("Your Account number is:" + " " + str(accountNumber))


# Generating credit card number
def credit_card():
    digits = string.digits
    twelveDigits = str( ''.join(random.choice(digits) for i in range(12)) )
    creditCardNumber = ("4" + twelveDigits)
    return creditCardNumber 

credit_card()


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(ccn):
    # reverse the credit card number
    ccn = ccn[::-1]
    # convert to integer
    ccn = [int(x) for x in ccn]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(ccn, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    sum_of_digits = True
    while sum_of_digits: 
        # converting ccn to string
        x = ccn
        listToStr = ' '.join(map(str, x)) 
        print("Your Credit card number is: " + listToStr)
        break
    else:
        credit_card()
    return sum_of_digits % 10 == 0
    




# getting user details
def user_info():
    firstName = input("Enter your First Name: ")
    lastName = input("Enter your Last Name: ")
    middleName = input("Enter your Middle Name: ")
    homeAddress = input("Enter your Home address: ")
    mail = True
    while mail:
        emailAddress = str(input("Enter Email Adress: "))
        if check_email(emailAddress):
            break
    
    
user_info()
acct_number()
ccn = credit_card()
validate(ccn)