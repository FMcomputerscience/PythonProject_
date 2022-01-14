from RouteM import*
from FlightM import*
import json
import os

class Airport:
    def __init__(self):
        pass
    count1=0
    routes=[]
    count2=0
    flights=[]
    def AddRoute(self,r):
        print("i am in Addroute and counti is: " )
        self.routes.append(r)
        #print("count1 is :",self.count1)
        print("route is added")
        print(r.routecode,r.city,r.destination,r.twoway)
        ##print(r.routecode,self.routes[self.count1].city,self.routes[self.count1].destination)
        #self.count1+=1
        
    def AddFlight(self,f):
        self.flights.append(f)
        #print("count1 is :",self.count2)
        print("route is added")
        print(f.routecode,f.departure,f.arrival,f.date)
        #print(self.flights[self.count2].routecode,self.flights[self.count2].departure,self.flights[self.count2].arrival)
        #self.count2+=1
        
    def List(self):
        for ro in self.routes:
            print("all paths: ")
            for fl in self.flights:
                if ro.routecode==fl.routecode:
                    print(ro.city,ro.destination,ro.twoway,
                          fl.departure,fl.arrival,fl.date)
                #print('\n')
            print('\n')

    def Search(self,source,dest):
        result=False
        print(result)
        for ro in self.routes:
            if (ro.city==source) and (ro.destination==dest):
                print("all flight founded for this path: ")
                for fl in self.flights:
                    if fl.routecode==ro.routecode:
                        print(ro.city,ro.destination,ro.twoway,
                               fl.departure,fl.arrival,fl.date)
                result=True
                break
        print("\n")
        if result is False:
            print("There is not any flight for this path.")
                
    def Save(self):
        #print("count1 issssssssssssssss: ",self.count1)
        #print("leeeeeeeeeeeeeeeeeeeeeeeeeeeeen(routes): ",len(self.routes))
        with open("E:\\faradars\\python\\python\\Airport\\text1.txt","w+") as t:
            for ro in self.routes:
                json.dump(ro.routecode,t) 
                t.write("\n")
                t.write(ro.city)
                t.write("\n")
                t.write(str(ro.destination))
                t.write("\n")
                json.dump(ro.twoway,t)  
                t.write("\n")
        
        with open("E:\\faradars\\python\\python\\Airport\\text2.txt","w") as t:
            for fl in self.flights:
                json.dump(fl.routecode,t)
                t.write("\n")
                t.write(fl.departure)
                t.write("\n")
                t.write(fl.arrival)
                t.write("\n")
                t.write(fl.date)
                t.write("\n")
                
    def Load(self):
        self.routes=[]
        self.flights=[]
        #self.count1=0
        #self.count2=0
        with open("E:\\faradars\\python\\python\\Airport\\text1.txt","r") as t:
            line=t.readline().strip()
            while(True):
                if len(line)==0:
                    break
                else:
                    routecode=int(line)
                    city=t.readline().strip()
                    destination=t.readline().strip()
                    inp=t.readline()
                    if inp=='true\n':
                        twoway=True
                    else:
                        twoway=False
                    r=Route(routecode,city,destination,twoway)
                    a.AddRoute(r)
                line=t.readline().strip()
        #os.remove("E:\\faradars\\python\\python\\Airport\\text1.txt")

        with open("E:\\faradars\\python\\python\\Airport\\text2.txt","r") as b:
            line=b.readline().strip()
            while(True):
                if len(line)==0:
                    break
                else:
                    routecode=int(line)
                    departure=b.readline().strip()
                    arrival=b.readline().strip()
                    date=b.readline().strip()
                    f=Flight(routecode,departure,arrival,date)
                    a.AddFlight(f)
                line=b.readline().strip()
        #os.remove("E:\\faradars\\python\\python\\Airport\\text2.txt")
                    
    

    
        
                    
            
            
            
                    
        

a=Airport()

            

    
    
