from FlightM import*
from RouteM import*
from AirportM import*

def Run():
    def Menu():
        print("1.Add a route.")
        print("2.Add a flight.")
        print("3.Show all routes and flights.")
        return input()
    
    def Process(choice):
        if choice=='1':
            print("enter routecode: ")
            routecode=int(input())
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
                  
    while(True):
        Process(Menu())
  
Run()
    



                
            
    


    
