# A python fizz-buzz implementation that outputs in ascii art
# Author: @jonot-cyber

#The ascii art that is used
ascii = """
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000::::::::::::0000::::0000::::::::::::0000::::::::::::00000::::::::::000000::::0000::::0000::::::::::::0000::::::::::::00000
00000::::::::::::0000::::0000::::::::::::0000::::::::::::00000:::::::::::00000::::0000::::0000::::::::::::0000::::::::::::00000
00000::::000000000000::::000000000000::::000000000000::::00000::::0000::::0000::::0000::::000000000000::::000000000000::::00000
00000::::000000000000::::00000000000::::000000000000::::000000::::0000::::0000::::0000::::00000000000::::000000000000::::000000
00000::::::::::::0000::::0000000000::::000000000000::::0000000::::::::::000000::::0000::::0000000000::::000000000000::::0000000
00000::::::::::::0000::::000000000::::000000000000::::00000000:::::::::0000000::::0000::::000000000::::000000000000::::00000000
00000::::000000000000::::00000000::::000000000000::::000000000::::000:::::0000::::0000::::00000000::::000000000000::::000000000
00000::::000000000000::::000000::::000000000000::::00000000000::::0000::::0000::::0000::::000000::::000000000000::::00000000000
00000::::000000000000::::00000::::000000000000::::000000000000::::0000::::0000::::0000::::00000::::000000000000::::000000000000
00000::::000000000000::::0000::::000000000000::::0000000000000::::0000::::00000:::0000:::00000::::000000000000::::0000000000000
00000::::000000000000::::0000::::::::::::0000::::::::::::00000::::0000::::00000::::00::::00000::::::::::::0000::::::::::::00000
00000::::000000000000::::0000::::::::::::0000::::::::::::00000:::::::::::00000000::::::0000000::::::::::::0000::::::::::::00000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
"""

#This segment actually generates the fizzbuzz. Its pretty standard
output = str()

for x in range(387):
    x += 1
    result = str()
    if x % 3 == 0:
        result += "Fizz"
    if x % 5 == 0:
        result += "Buzz"
    if result == "":
        result = str(x)
    output += result

#This is where it maps the string to the ascii art
fizz_buzz_index = 0

new_ascii = ""

for char in ascii:
    if char == ":":
        new_ascii += " "
    elif char == "0":
        new_ascii += output[fizz_buzz_index]
        fizz_buzz_index += 1
    else:
        new_ascii += char

#And here it outputs the data
print(new_ascii)