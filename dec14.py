# Write a python program function that takes the "amount" of money as user input. Then splits that money into 500,100,50,20,10,5,2 and 1 taka notes and print the final result.

def amount(taka):
    fifty = 0
    note5 = taka // 500
    taka %= 500
    hundred = taka // 100
    taka %= 100
    if (taka >= 50):
        fifty = taka // 50
        taka %= 50
    else:
        one = taka // 1

    print(f' {note5}, {hundred},{fifty},{one} ')


# inp = int(input())
# amount(inp)

# Write a python code of a program that reads three sides of a triangle and check whether the triangle is valid or not.
inp = input().split(',')
# print(inp)
idx = int(inp[0])

for i in inp:
    if (idx < int(i)):
        idx = int(i)

sides = 0
for j in inp:
    if (int(j) < idx):
        sides += int(j)
if (sides > idx):
    print('Valid Triangle')
else:
    print('Not a valid Triangle')
