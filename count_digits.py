#write a function given number which gives number of digits in the number
#example - countdigits(9) = 1, countdigits(99) = 2


# def countdigits(n):
#     if n in range(0,10):
#         return 1
#     if n in range(10,99):
#         return 2
#     return 0
# # print(countdigits(35))
# x = countdigits(35)
# print(x)


# def countdigitsofnumber(n):
#     x = ""
#     x = str(n)
#     return(len(x))
# print(countdigitsofnumber(222))



# def countdigitsofnumber(n):
#     x = []
#     x.append(n)
#     return(len(x))
# print(countdigitsofnumber(222))


def countdigitsofnumber(n):
    count = 0
    while (n > 0):
        count = count + 1
        n = int(n / 10)
    return count
print(countdigitsofnumber(100))






