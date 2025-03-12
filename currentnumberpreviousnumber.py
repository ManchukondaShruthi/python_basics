#print previous_number , current_number and total of both


previous_number = 0
for i in range(0,10,1):
    current_number = i
    previous_number = i
    print("previous_number", previous_number, "current_number", i, "sum", previous_number + i)