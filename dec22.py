# 1. Magic number: If the summation of even indexed digits is equal to the summation of odd indexed digits, then the number is a magic number.
# Now, write a Python program that will take a string of numbers where each number is separated by a comma. The program should
# print a tuple containing two sub-tuples, where the first sub-tuple will hold the magic numbers and the second sub-tuple will hold
# the non-magic numbers.
# input : "1232, 4455, 1234, 9876, 1111" output: ((1232, 4455, 1111), (1234, 9876))

def tup(stri):
    lst = stri.split(', ')
    lstt = []
    for i in lst:
        lstt.append(int(i))

    st = 0
    end = 0
    sum = 0
    t = ''
    for i in lst:
        # if(i[0] == i[])
        # i = int(i)
        # if (i[0] == i[2] and i[1] == i[3]):
        #     print(i)
        st = 0
        end = 0
        st = int(i[0]) + int(i[2])
        end = int(i[1]) + int(i[3])

        if (st == end):
            # print(i)
            # t += i
            # print(t)
            # print(type(i))
            t += i
            print(t)


tup("1232, 4455, 1234, 9876, 1111")
