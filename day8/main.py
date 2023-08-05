# def threeWorks(name):
#     print(f"Hey there {name}!")
#     print(f"How is your day {name}?")
#     print(f"What did you had in lunch {name}?")

# threeWorks("Babe")

# Functions with more than 1 input

def threeWorks(name, age):
    print(f"Hey there {name}!")
    print(f"How is your day {name}?")
    print(f"What did you had in lunch {name}?")
    print(f"Your age is {age}")

threeWorks(name = "Babe", age = 20)






# Instructions
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5

#                            = 1.6

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# test_h = 3
# test_w = 9
# Example Output
# You'll need 6 cans of paint.



#Write your code below this line 👇
import math
def paint_calc(height , width, cover):
   total_paint = math.ceil(round((height * width)/cover))
   print(f"You'll need {total_paint} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


