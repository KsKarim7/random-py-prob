# Question : https://drive.google.com/file/d/1ZkFGRfIuRkQOBHAt9j7tW-Xc8LNQxG5O/view?usp=sharing

alphabets = ['J', 'D', 'H', 'O', 'Z']
morse_code_clues = [(1, 3, True), (4, 0, True),
                    (2, 1, False), (0, 3, False), (2, 3, False)]


def func(lst, lstt):
    count = 1
    alpha = lst[:]
    for i in alphabets:
        if (count == len(alphabets)):
            break
        else:
            # alpha.append(i)
            num = (ord(i)+ord(alphabets[count]))//2
            alpha.append(chr(num))
            count += 1
    print(alpha)


func(alphabets, morse_code_clues)
