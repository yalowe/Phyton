def averag(mis1):
    print("-------------------output-------------------")
    multi=mis1*4
    smaller=mis1-2
    inte=int(mis1/3)
    inte1=mis1%3 # mis1 = 5 ---> 5 / 3 = 1.66666667 --> 5 % 3 = 0.66666667 * 3 = 2 
    print(multi)
    print(smaller)
    print(inte)
    print(inte1)


print("enter a number:")
print()
num1=int(input())
averag(num1)