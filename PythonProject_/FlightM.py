from RouteCodeM import*

class Flight(RouteCode):
    def __init__(self,routecode,departure,arrival,date):
        RouteCode.__init__(self,routecode)
        self.departure=departure
        self.arrival=arrival
        self.date=date

