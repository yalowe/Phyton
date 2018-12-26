seats = []
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0])

def displayBookings():
  #Display Bookings
  print("")
  print("======================================")
  print("")
  for row in seats:
    print(row)
  print("")
  print("======================================")

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
  


#Main Program Starts Here
checkSeat()  
displayBookings()