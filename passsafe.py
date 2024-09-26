import re
import time

stop = True

while stop:
    password = input("enter a strong password for chak has strongth :\n")
    if re.fullmatch(r'[A-Za-z0-9@#!$%^&+=]{8,}', password): 
        print("\n")
        time.sleep(2)
        print("your password is strong like you my frind")
        time.sleep(1)
        print("Good luck")
        time.sleep(1)
        chakAgane = input("Do you want to check another password?[yas , no]\n")
        if re.search(r"^n" , chakAgane):
            stop = False
            print("I hope Asta helped you and made you happy my friend, good bye.")
        
    else:
        print("I'm sorry, my friend, but your password is weak")
        time.sleep(2)
        print("I have an idea that")
        time.sleep(1)
        print("you can use special signs(!@#$), uppercase and lowercase letters, and numbers to make it stronger")
        













