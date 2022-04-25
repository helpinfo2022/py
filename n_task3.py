# Task 3
# String Challenge
# Have the function StringChallenge(str) take the str parameter being passed and determine if it passes as a valid password that follows the list of constraints:
#
# 1. It must have a capital letter.
# 2. It must contain at least one number.
# 3. It must contain a punctuation mark or mathematical symbol.
# 4. It cannot have the word "password" in the string.
# 5. It must be longer than 7 characters and shorter than 31 characters.
#
# If all the above constraints are met within the string, the your program should return the string true, otherwise your program should return the string false. For example: if str is "apple!M7" then your program should return "true".
# Examples
# Input: "passWord123!!!!"
# Output: false
# Input: "turkey90AAA="
# Output: true

def StringChallenge(my_str):

    for i in my_str:
        if i.isupper():

            for x in my_str:
                if x.isdigit():

                    if "password" not in my_str:

                        symbol_check=("+" or "-" or "*" or "," or ".")
                        if  symbol_check in my_str:

                            my_len = len(my_str)
                            if my_len>7 or my_len>31:
                                return True
    else: return False

print(StringChallenge("ffff+fF6"))