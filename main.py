class planet:
    def __init__(self,name,gasses,noOfMoons,hasRing):
        self.name = name
        self.gasses = gasses
        self.noOfMoons = noOfMoons
        self.hasRing = hasRing
    
    def get_noOfMoon(self):
        return self.noOfMoons
    

mercury = planet('Mercury', [], 10 , False)
print(mercury.get_noOfMoon())
