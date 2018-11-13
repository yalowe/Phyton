print("")
print("the app check if what we get from the user is palindrom or not:")
print("")
print("please enter number or string to cheke if the input is palindrom or not:")
print("")
palindrom=input()
lenhgt = len(palindrom)
for x in range(0,lenhgt-1):
    if palindrom[x] != palindrom[lenhgt-x-1]:
        print("not palindrom")
        break
else:
    print("polindrom")
    