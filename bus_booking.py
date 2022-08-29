import datetime
print(":->->->->-> Welcome to the Express_Bus_Booking service <-<-<-<-<-:")
print("Enter the number for that corresponding city\n\t\t1. Ahemdabad\n\t1.4:00 \n\t2. 5:00\n\t3. 10:00\n\t4. 16:00\n\t5. 23:00 \n\t\t2. Gandhinagar\n\t1.3:00 \n\t2. 5:00\n\t3. 16:00\n\t4. 22:00\n\t5. 23:00\n\t\t3. Rajkot\n\t1. 6:00\n\t2. 7:00\n\t3. 8:00\n\t4.16:00\n\t5. 19:00\n\t\t4. Bhavnagar\n\t1. 6:00 \n\t2. 7:00\n\t3. 9:00\n\t4. 15:00\n\t5.19:00\n\t\t5. Surat\n\t1. 02:00 \n\t2. 18:00 \n\t3. 20:00\n\t4. 22:00\n\t5. 23:00")
dest=input("Enter the name of city")
day=int(input("Enter the day"))
month=int(input("Enter the month"))
year=int(input("Enter the year"))
time=int(input("Enter time in 24hrs format"))
n=int(input("Enter number of seats(1 to 10\nIf you want to book the whole bus enter other than 10"))

class bus:
    s="seats"#seatdefined
    def __init__(self):
        with open("bus_book_resulwt.txt","a") as f:
            today=datetime.datetime.now()
            f.writelines(f"\n\t\t*****New session started:{today}*****")
            boker=input("Enter name person who is booking: ")
            f.writelines(f"\nFirst name of personbooking{boker}")
            if n>10:
                f.writelines(f"\n\t\t#####Booked whole bus#####")
            else:    
                f.writelines(f"\n\t\t#####Number of tickets book: {n}#####")
    def provideDetails(self):
        occassion=None
        numberbook=0
        c_name=input("Enter name: ")
        id_no=int(input("Enter 14 digit Aadhar card: "))
        age=int(input("Enter your age: "))
        mo=int(input("Enter your mobile number: "))
        gender=input("Enter your gender(m/f/other): ")
        self.getDetails(numberbook,c_name,id_no,age,gender,mo,occassion)
    def getDetails(self,numberbook,name,id_no,age,gender,mo,occassion):
        with open("bookdetails.txt","a") as f:
            if numberbook==0:
                f.writelines(f"\nName: {name}")
                f.writelines(f"\nAadhar number: {str(id_no)}")
                f.writelines(f"\nAge: {str(age)}")
                f.writelines(f"\nGender: {gender}")
                f.writelines(f"\nMobile no: {str(mo)}")
            else:
                f.writelines(f"\nName: {name}")
                f.writelines(f"\nAadhar number: {str(id_no)}")
                f.writelines(f"\nAge: {str(age)}")
                f.writelines(f"\nGender: {gender}")
                f.writelines(f"\nMobile no: {str(mo)}")
                f.writelines(f"\nOccassion: {occassion}")
 
                
    def wholebus(self):
        numberbook=1
        print("To book whole bus you want to provide following info:")
        book_name=input("Enter name who is booking whole bus: ")
        id_no=int(input("Enter 12 digit Aadhar number: "))
        age=int(input("Enter age: "))
        mo=int(input("Enter your contact number: "))
        gender=input("Enter gender: ")
        occassion=input("For which occassion you want to book the bus: ")
        self.getDetails(numberbook,book_name,id_no,age,gender,mo,occassion)
    def number(self):
        
        if n==1:
            self.provideDetails()
        elif n==2:
            self.provideDetails()
            self.provideDetails()
        elif n==3:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==4:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==5:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==6:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==7:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==8:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==9:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        elif n==10:
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
            self.provideDetails()
        else:
            print("So, You want to book whole bus OK!")
            self.wholebus()
   
    def check(self,a,day,month,year,hour):
        if a=='Ahemdabad' or a=='Rajkot' or a=='Bhavnagar' or a=='Surat' or a=='Gandhinagar':
            print("Loading")
        else:
            print("You entered other then our provided destinations!")
            exit(0)
     
            
    
        validate=True
        try:
            datetime.datetime(year,month,day,hour)
        except ValueError:
            validate=False

        if validate==False:
            print("You entered wrong date")
            exit(0)
    
    def Ahemdabad(self,a_time):
        seat=45
        if a_time==4:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Ahemdabad***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Ahemdabad")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif a_time==5: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Ahemdabad***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Ahemdabad")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif a_time==10: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Ahemdabad***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Ahemdabad")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif a_time==16:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Ahemdabad***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Ahemdabad")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False    
        elif a_time==23:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Ahemdabad***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Ahemdabad")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()

                print(f"Seats available:{seat}")
            else:
                print("Seats are full")
                return False
        return True
    def Rajkot(self,r_time):
        seat=45
        if r_time == 6:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Rajkot***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Rajkot")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif r_time == 7: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Rajkot***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Rajkot")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif r_time == 8: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Rajkot***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Rajkot")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif r_time==16:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Rajkot***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Rajkot")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False    
        elif r_time==19:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Rajkot***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Rajkot")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        return True
    def Gandhinagar(self,Gandhinagar_time):
        seat=45
        if Gandhinagar_time==3:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Gandhinagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Gandhinagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Gandhinagar_time==8: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Gandhinagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Gandhinagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Gandhinagar_time==16: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Gandhinagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Gandhinagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Gandhinagar_time==22:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Gandhinagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Gandhinagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False    
        elif Gandhinagar_time==23:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Gandhinagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Gandhinagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        return True
    def Surat(self,Surat_time):
        seat=45
        if Surat_time==2:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Surat***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Surat")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Surat_time==18:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Surat***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Surat")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Surat_time==20: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Surat***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Surat")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Surat_time==22:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Surat***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Surat")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False    
        elif Surat_time==23:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Surat***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Surat")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        return True
    def Bhavnagar(self,Bhavnagar_time):
        seat=45
        if Bhavnagar_time==6:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Bhavnagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Bhavnagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Bhavnagar_time==7: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Bhavnagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Bhavnagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Bhavnagar_time==9: 
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Bhavnagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Bhavnagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        elif Bhavnagar_time==15:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Bhavnagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Bhavnagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False    
        elif Bhavnagar_time==19:
            if seat!=0:
                if n>10:
                    seat=0
                    print("***Whole bus will be booked of Bhavnagar***")
                else:
                    seat-=n
                    print(f"After your {n}seats are booked of Bhavnagar")
                print(f"Seats available:{seat}")
                sure=input("Are you sure you want to book it?(y/n)")
                if sure=='n':
                    seat+=n
                else:
                    self.number()
            else:
                print("Seats are full")
                return False
        return True
    def city(self,dest,time):
        if dest=='Ahemdabad':
            self.Ahemdabad(time)
        if dest=='Rajkot':
            self.Rajkot(time)
        if dest=='Bhavnagar':
            self.Bhavnagar(time)
        if dest=='Gandhinagar':
            self.Gandhinagar(time)    
        if dest=='Surat':
            self.Surat(time)
        return True
        
new=bus()
new.check(dest,day,month,year,time)
book=new.city(dest,time)

if book:
    print("Congratulations! You have successfully booked your ticket")
else:
    print("Sorry! Your ticket can't be book \nTry again later")
    exit(0)
    
print("End")
