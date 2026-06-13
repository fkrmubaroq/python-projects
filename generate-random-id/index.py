# import os
# import sys
# import string
from random_id import random_id
# os.mkdir("modules-test-baka")
# os.chdir("modules-test-baka")
# print("CurrentDir : ",os.getcwd())
# os.rmdir("modules-test-baka")
# print("remove dir successfully")

# print("Maxsize :", sys.maxsize)
# print("env path :", sys.path)
# print("version py :", sys.version)
# print("exit :", sys.exit())

# print("ASCII : ", string.ascii_letters)
# print("DIGITS : ", string.digits)
# print("Punctuation : ", string.punctuation)
user_input = input("Enter length for random ID : ")
many = int(input("How many random ID do you want? : "))
for i in range(many):
    print("Random ID : ", random_id(int(user_input)))
