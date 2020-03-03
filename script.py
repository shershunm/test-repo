import sys
import requests
from os import rename
import math


# to track the code on the git - click on the source control button

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

# if input needed for the code - run it in the Terminal view, otherwise use code (output)
# name = input("Your Name? ")
# print("Hello,", name)

