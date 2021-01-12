class driver:
    def __init__(self):
        self.name = "Rinkesh"

class car:
    def __init__(self,obj):
        print("Driver name is ->",obj.name)


d = driver()
c = car(d)
