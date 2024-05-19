# Python3 code to demonstrate working of
# Add Space between Potential Words
# Using regex() + list comprehension
import re

# initializing list
test_list = ["gfgBest", "forGeeks", "andComputerScience"]

# printing original list
print("The original list : " + str(test_list))

# using regex() to perform task
res = [re.sub(r"(\w)([A-Z])", r"\1 \2", ele) for ele in test_list]

# printing result
print("The space added list of strings : " + str(res))