class train:

    def __init__(self,name,seat,yourname):
        self.name=name
        # self.fare=fare
        self.seat=seat 
        print()
    def getStatus(self):
        print(f"Name of train is {self.name}")
        print(f"Seats available:{self.seat}")
    def fareinfo(self):
        print(f"The fare of the ticket is {self.fare}")
    def bookTicket(self):
        if(self.seat>0):
            print(f"Your ticket has been booked! Your seat number is {self.seat}")
            self.seat-=1
        else:
            print("Try in tatkal")
t1=train("Intercity:01",90,100)
t1.getStatus()
# t1.fareinfo()
t1.fare=300
print("Instance object value",t1.fare)
t1.bookTicket()
t1.bookTicket()
t1.getStatus()