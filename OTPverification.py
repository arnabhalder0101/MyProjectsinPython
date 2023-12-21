import testTwilio1
import random

run = 1
limit = 5
otp = random.randint(1000, 9999)
testTwilio1.MessageNotify("OTP For Login in My App!""\nPlease don't share it with anyone."
                          f"\nYour 4 digit OTP : {otp}", to="+916296790017")
while run:
    code = int(input("Enter the 4 Digit OTP: "))
    if code == otp:
        msg = "This is the Secret message! You've just accessed it.\nYou're Verified!"
        print(msg)
        run = 0
    else:
        limit -= 1
        print("Wrong Code Entered!\nTry Again...")
        print(f"\n{limit} entry left! ")

    if limit == 0:
        print("Out of Entry Limit!\nUser isn't verified!")
        run = 0
