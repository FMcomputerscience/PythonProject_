from RouteM import*
from AirportM import*
#import a from Airport


class Maincode:
    @staticmethod
    def Myfunc():
        def Menu():
            print("a.Add a route.")
            print("b.Add a flight.")
            print("c.Show all routes and flights.")
            print("d.Search a fligt.")
            print("e.Save.")
            print("f.Load.")
            return input()
    
        def Process(choice):
            if choice=='a':
                print("enter routecode: ")
                while(True):
                    try:
                        routecode=int(input())
                        break
                    except:
                        print("You've entered an string! please enter an integer number for routecode: ")
                print("enter source city: ")
                city=input()
                print("enter destination: ")
                destination=input()
                print("is it a twoway ticket?(y/n): ")
                inp=input()
                if inp=="y" or inp=="Y":
                    twoway=True
                else:
                    twoway=False
                r=Route(routecode,city,destination,twoway)
                a.AddRoute(r)
            elif choice=="b":
                print("enter routecode: ")
                while(True):
                    try:
                        routecode=int(input())
                        break
                    except:
                        print("You've entered an string! please enter an integer number for routecode: ")
                print("enter time departure: ")
                departure=input()
                print("enter arrival time: ")
                arrival=input()
                print("enter date: ")
                date=input()
                f=Flight(routecode,departure,arrival,date)
                a.AddFlight(f)
            elif choice=="c":
                a.List()
            elif choice=="d":
                print("enter your source: ")
                source=input()
                print("enter your destination: ")
                dest=input()
                a.Search(source,dest)
            elif choice=="e":
                a.Save()
            elif choice=="f":
                a.Load()
                
                
                
                  
        while(True):
            Process(Menu())

mc=Maincode()
def Run():
    mc.Myfunc()

