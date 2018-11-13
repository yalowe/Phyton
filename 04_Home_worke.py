numbers_names=['one','two','three','four','five','six','seven','eight','nine']
print("Enter number:")
num=int(input())
if num>0 and num<10:
    print(numbers_names[num-1])
if num>0 and num<99:
    digit1=num%10
    digit2=((num/10)-(num%10)/10)
    sum=digit1+digit2
    print("the sum of numbers is:",int(sum))
if num>99 and num<1000:
    ezer=num
    digit1=ezer%10
    digit2= ezer%100%10
    digit3=int(ezer/100)
    sum=digit1*digit2*digit3
    print("the sum of double:",sum)



    