#given list [10,20,30,40,50] print the data as [50,40,30,20,10]
def reverselist(n):
    for x in range(-1,-len(n)-1, -1):
        print(n[x])
x_array = [10,20,30,40,50]
reverselist(x_array)