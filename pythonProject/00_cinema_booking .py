
seats = []
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])

class cinimaRoom:
    def __init__(self, numberRoom):
        self.numberRoom = numberRoom

    def tell_room(self):
        print('room Number: ',self.numberRoom, end=" ")

# If subclass contains a constructor
# The subclass must call to the base constructor
class moves(cinimaRoom):

    def __init__(self,numberRoom ,moveName, length):
        cinimaRoom.__init__(self, numberRoom)
        self.moveName = moveName
        self.length = length

    def tell_move(self):
        cinimaRoom.tell_room(self)
        print(' move Name: ',self.moveName," length move: ",self.length,"\n")
    

class chers(moves):
    def __init__(self, numberRoom, moveName, length,cher):
        moves.__init__(self,numberRoom, moveName, length)
        self.chers = cher
        
    def checkSeat():
        ticets = int(input("enter number of ticets you want:\n"))
        for i in range(ticets):
            row = int(input("Enter a row number (between 0 and 5): "))
            column = int(input("Enter a column number (between 0 and 7):  "))
            
            if seats[row][column] == 1:
                print("This seat is already booked.")
            else:
                seats[row][column] = 1
                print("This seat is empty.")
                for i in seats:
                    print(i)

    def tell_chers(self):
        moves.tell_move(self)
        print("seats:")
        print("========================")
        print("")
        for row in seats:
            print(row)
        print("")
        print("========================")
        chers.checkSeat()



"""-----------------------------------main()---------------------------------------"""
       
c = seats
move1 = chers(1,"Alice",150,c)
move1.tell_chers()

print(("\n"))

move2 = chers(2,"avatar",110,c)
move2.tell_chers()