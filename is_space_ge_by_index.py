
"""
def max_letter(arr):   
    max=arr[0][0][0]
    for x in range(0,len(arr)):
        for n in range(0,len(arr[x])):
            for s in range(0,len(arr[n])):
                if arr[x][n][s] > max:
                    max=arr[x][n][s]
    return max

arr=[["fbejcd"],["asdfg"],["jhgk"],["sertzyzio"]]
max_1 = max_letter(arr)
print("max_1:",max_1)


lst1 = [5, 20, -10]
lst2 = [7, -2, -2, 4]

for x in lst1+lst2:
    print(x)


max_2 =max([5, 20, -10])
print("max_2:",max_2)



def my_str(lst):
    cnt=0
    for x in range(0,len(lst)):
         for n in range(0,len(lst[x])):
             for s in range(0,len(lst[x][n])):
                if lst[x][n][s] == " ":
                    cnt+=1
                    print("in[",x,"][",s,"]")#the place of has space                 
    return cnt
"""
string=[["yal we gib te"],["av ielg abi"],["li lw et"]]
#result=my_str(string)
#print("the sum of spaces is:",result)

cnt=0
for x in string:
    for char in x:
        if char == " ":
                cnt+=0
print(cnt)                