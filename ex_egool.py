"""
---------------GLOBAL PROPS------------------
"""
rank= None
is_win= False
is_x_turn= False
play_again = "y"

matrix= None
x_array= None
o_array= None


"""
---------------FUNCTIONS----------------------
"""
def get_board_rank():
    global rank
    rank=int(input("Enter the rank of the board: "))



def build_matrix():
    global matrix
    global x_array
    global o_array

    x_array=[]
    o_array=[]
    matrix=[]
    for row in range(0,rank):
        matrix.append([])
        for col in range(0,rank):
            matrix[row].append(row*rank+col+1)

    for element in range(0,rank*2+2):
        x_array.append(0)
        o_array.append(0)

    



def get_position():
    global rank
    global matrix
    global is_x_turn
 
    for row in range(0,rank):  
        strFormat=""  
        for col in range(0,rank):
            strFormat+=str(matrix[row][col]) + " | "
        print(strFormat)
        print("-----------")
    if is_x_turn:
        char="x"
    else:
        char="o"

    print("************ user ",char,"****************")
    return int(input("Enter the position (1 - "+ str(rank*rank)+")"))


def check_if_win(row,col):
    global is_x_turn
    global is_win
    global rank
    global x_array
    global o_array
    if is_x_turn:
        arr=x_array
    else:
        arr=o_array
    arr[row]+=1
    arr[rank+col]+=1

    if row==col:
        arr[rank+rank]+=1

    if (row+col)==(rank-1):
        arr[rank+rank+1]+=1

    is_win=(arr[row]==rank) or (arr[rank+col]==rank) or (arr[rank+rank+1]==rank) or (arr[rank+rank]==rank)

    if(is_win):
        if(is_x_turn):
            print("x won")
        else:
            print("o won")
    else:
        sum=0
        for element in range(0,rank):
            sum+=x_array[element]
            sum+=o_array[element]
        if(sum==rank*rank):
            is_win=True
            print("Game Over")



def handle_turn(position):
    global matrix
    global is_x_turn
    row=(position-1)//rank
    col= (position-1) %rank

    if matrix[row][col]!="x" and matrix[row][col]!="o":
        if is_x_turn:
            matrix[row][col]="x"
        else:
            matrix[row][col]="o"
        
        check_if_win(row,col)

        # change the turn to the other player
        # if is_x_turn was true - it will get false
        # if is_x_turn was false - it will get true
        is_x_turn=not is_x_turn

        return True


    else:
        return False




"""
---------------MAIN CODE-----------------------
"""

while play_again=="y":
    get_board_rank()
    build_matrix()

    while not is_win:
        flag=False
        while not flag:
            selectedPos=get_position()
            flag=handle_turn(selectedPos)
    

    is_win=False
    play_again=input("Do you want to play again (y or n)")
