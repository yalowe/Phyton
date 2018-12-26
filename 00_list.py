def print_params(meseg,*numbers,**pairs):
    print("meseg:",meseg)
    for x in numbers:
        print(x)
    for i,j in pairs.items():
        print("key :",i,"value: ", j)


print_params("hello",1,2,3,4,"world",name="bob",age=12)