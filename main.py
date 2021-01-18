# ============ Power Ball Number Generator ===========

from random import shuffle

# Range of numbers for the five Power Ball numbers from 1 - 69
# This will auto-generate five of those numbers.

lottery = list(range(1, 69))
powerball = list(range(1, 26))
numbers = []
num = []

# Title
print("POWER BALL NUMBERS")

# For loop to append (sort) the five Power Ball numbers selected above
for i in range(5):
    shuffle(lottery)
    x = lottery.pop()

# Check to see if the numbers have been picked..
# If yes, then pick a new number
    while lottery in numbers:
        lottery = list(range(1, 69))
    numbers.append(x)

# Displays the five numbers in an ascending order
numbers.sort()
print("Today is your lucky day, my friend! The numbers are: ", numbers)

# For loop to append (sort) the red Power Ball number
for j in range(1):
    shuffle(powerball)
    y = powerball.pop()

# Check to see if the numbers have been picked..
# If yes, then pick a new number
    while powerball in num:
        powerball = list(range(1, 26))
    num.append(y)

# Displays the final (sixth) Power Ball number
num.sort()
print('POWER BALL number is: ', num)
