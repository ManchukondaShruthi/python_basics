#write a function to reverse a number 
#input = 125, output = 521

def reversenumber(n):
    count = 0
    digit_list = []
    while(n > 0):
        remainder = n % 10
        quotient = n // 10
        digit_list.append(remainder)
        n = quotient
        count = count + 1

    print(digit_list)
    return count
print(reversenumber(125))
