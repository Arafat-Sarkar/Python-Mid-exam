class Star_Cinema :
    __hall_list = []
    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        
    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.__show_list.append(show_info)
        self.seats[id] = []
        for row in range(self.rows):
            row_seats = []
            for col in range(self.cols):
                row_seats.append(0)
            self.seats[id].append(row_seats)
            
    def book_seats(self, id, seats_to_book):
        if id in self.seats:
            for row, col in seats_to_book:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[id][row][col] == 0:
                        self.seats[id][row][col] = 1
                        print(f"Seat ({row}, {col}) in show {id} booked successfully.")
                    else:
                        print(f"Seat ({row}, {col}) in show {id} is already booked.")
                        
                else:
                    print(f"Invalid seat ({row}, {col}) in show {id}.")
        
        else:
            print(f"Show with ID {id} not found.")
            
    def view_show_list(self):
        print()
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
            
        print()
        
    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col] == 0:
                         print("0", end=" ")
                         
                    else:
                        print("1", end=" ")
                        
                print() 
                
            print()
            
        else:
            print(f"Show with ID {id} not found.")
            
hall1 = Hall(5,5,1)
hall1.entry_show(1, "Jawan ",  "10:00 AM" )
hall1.entry_show(2, "Superman", "02:30 PM")

while True:
    print('1: VIEW ALL SHOW TODAY')
    print('2: VIEW AVAILABLE SEATS')
    print('3: BOOK TICKET')
    print('4: Exit')
    
    op=int(input("Enter Option: "))
    
    if op == 1:
        hall1.view_show_list()
        
    elif op == 2:
        show_id = int(input("Enter the show ID: "))
        hall1.view_available_seats(show_id)
        
    elif op == 3:
        show_id = int(input("Enter the show ID: "))
        num_seats = int(input("Enter the number of seats to book: "))
        seats_to_book = []
        for i in range(num_seats):
            row = int(input(f"Enter the row for seat {i}: "))
            col = int(input(f"Enter the column for seat {i}: "))
            seats_to_book.append((row, col))
            
        hall1.book_seats(show_id, seats_to_book)
        
    elif op == 4:
        break
    
    else:
        print("Invalid choice. Please try again.")
                
            
        