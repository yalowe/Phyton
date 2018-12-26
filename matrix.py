
def handle_mat(space_x,space_y):
    global matrix
    for row in range(0,rank):
        for col in range(0,rank):
            if matrix[row][col]!="x" and matrix[row][col]!="o":
                if space_x==matrix[row][col]:
                    matrix[row][col]="x"
                if space_y==matrix[row][col]:
                    matrix[row][col]="o"

def input_place():
    global matrix
    print("Enter a place you want put 'x'")
    space_x=int(input())

    print("Enter a place you want put 'o'")
    space_y=int(input())
    handle_mat(space_x,space_y)
    
    for row in matrix:
        print(row)
    print("----------------------------")

def biult_matrix(mat,rank):
    for row in range(0,rank):
        matrix.append([])
        for col in range(0,rank):
            matrix[row].append(row*rank+col+1)
       


matrix=[]
a="y"
print("Enter a rank:")
rank=int(input())
biult_matrix(matrix,rank)

print("you want to play:'y'/'n'")
b=str(input())
if b==a:
    row=0
    for row in range(0,rank+1):
        input_place()

for row in matrix:
    print(row)


    





