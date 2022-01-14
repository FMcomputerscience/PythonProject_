from RouteCodeM import*

class Route(RouteCode):
    def __init__(self,routecode,city,destination,twoway):
        RouteCode.__init__(self,routecode)
        self.city=city
        self.destination=destination
        self.twoway=twoway
        
