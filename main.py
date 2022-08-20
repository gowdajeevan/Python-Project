'''
Name: Jeevan HS
College: Government Engineering College Kushalnagar
Year of Passing: 2022
Email: gowdajeevan664@gmail.com
Mobile Number: 6361327282
'''
from tkinter.messagebox import NO


class planet:
    all_gases = []
    def __init__(self,name,gasses,noOfMoons,hasRing):
        self.name = name
        self.gasses = gasses
        self.noOfMoons = noOfMoons
        self.hasRing = hasRing
        planet.all_gases.extend(gasses)
    
    def get_noOfMoons(self):
        # count = 0
        # if self.hasRing == 'YES':
        #     count += 
        return self.noOfMoons

    def get_maxGas():
        return max(planet.all_gases,key=planet.all_gases.count)
    

mercury = planet('Mercury',[],0,'NO')
venus = planet('Venus',["Carbon Dioxide", "Nitrogen"],0,'No')
earth = planet('Earth',["Nitrogen", "Oxygen"],1,'No')
jupitor = planet('Jupitor',["Hydrogen", "Helium"],79,'Yes')
saturn = planet('Saturn',["Hydrogen", "Helium"],83,'Yes')
uranus = planet('uranus',["Hydrogen", "Helium", "Methane"],27,'Yes')


print(mercury.get_noOfMoons())
print(planet.get_maxGas())


