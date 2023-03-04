# 3.Write a Python program that takes a tuple of tuples as an input from the user. Then calculates the average value of the numbers for
# each tuple of tuples and find the tuple whose sum is the maximum. [You are not allowed to use max () function here. You are not
# allowed to use Regex split in this task.]
# Hints: Since the input function converts everything to string by default. You might need to use strip() and split() to get the
# data/tuples.
inp = input()
# inp = inp[1:-1]
# tup = ()
a = inp.split(',')

# print(inp)

for i in a:
    print(i)
    # tup += i
