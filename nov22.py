# Write a python program that will take 5 integer inputs from the user. If the total of these inputs is even then particular pattern will be printed according to the second input.If the total is odd , it will print 'No pattern is created'
# if the total of these outputs are even then (the user inputs are 2,4,10,6 and 12. The total of these inputs are 34.As 34 is even, a pattern is printed according to the second output i.e. 4):
# 1&1&
# 2222
# 3&3&
# 4444

sum = 0
sec = 0
for i in range(5):
    inp = int(input())
    if (i == 1):
        sec += inp
        # print(sec, 'second')
    sum += inp
if (sum % 2 == 0):
    for f in range(sec):
        for g in range(sec):
            print(f+1, end='')
            for k in range(0, sec//2, 2):
                if (g == 2):
                    g = '&'

        print()
else:
    print('No pattern is created')
