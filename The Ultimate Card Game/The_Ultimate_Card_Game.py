import os
from CardCode import *
from colorama import Fore, Back, Style, init
init()

#Sorry if something is broken, i have no idea if this runs on linux operating systems, so im
#trying my best to use libarys that work for win and linux.
#And if i cant find them i just make them myself, with a even higher chance to not work lmao

GameDataDir = os.path.join(os.getcwd(),"GameData")
DebuffsDir = os.path.join(GameDataDir,"Debuffs")
ObjectsDir = os.path.join(GameDataDir,"Objects")

WeaponIDs = LoadAllObjectsInDir(ObjectsDir,"Weapon")
EnemyIDs = LoadAllObjectsInDir(ObjectsDir,"Enemy")

def cls(): ##https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear') #No idea you could nest "if" functions like this
    #Starting to think i should spend an hour or two reading all of the python documents,
    #cause the deeper and deeper i go the more i realise i have no idea what some functions can do.
    
gearSlots = { #Slots for gear, under construction
    "head":None,
    "body":None,
    "legs":None,
    "weapon":None,
    "gear":None
}

PlayerInv = InventoryObject(MaxSlots=15) # Make Player Inv
PlayerHealth = 100

PlayerInv.addItem(WeaponIDs["Stick of Time"])

gearSlots["Weapon"] = WeaponIDs["Stick of Time"] # New Method

#getattr(class,FunctionName) ~ Returns true or false if class has function

while __name__ == "__main__":
    Input = input("Action:")
    if(Input.lower() == "inv"):
        print(ReadItems(PlayerInv))

    if(Input.lower() == "fight"):
        Panel = textPanel(20,10)
        PlayerHP = textObject("Player HP:" + str(PlayerHealth),1,3)
        EnemyHP = textObject("Enemy HP:" + str(PlayerHealth),3,3)
        Div1 = dividerObject(5)
        Panel.addObjects([PlayerHP,EnemyHP,Div1])

        while True:
            cls()
            print(Panel.drawPanel())
            Action = input("Action:")