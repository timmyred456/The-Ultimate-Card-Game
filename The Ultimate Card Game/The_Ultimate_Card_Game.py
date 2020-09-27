import os
from CardCode import *
from colorama import Fore, Back, Style, init

weaponIDs = LoadAllItemsInFile("TestWeapons.json")
init()

def cls(): ##https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')
    
gearSlots = { #Slots for gear, under construction
    "head":None,
    "body":None,
    "legs":None,
    "Weapon":None,
    "Gear":None
}

PlayerInv = InventoryObject(MaxSlots=15) # Make Player Inv
PlayerHealth = 100
gearSlots["Weapon"] = weaponIDs[0][1].CreateNew() #Sets player weapon to the first weapon in TestWeapons.json



def CheckBetween(String,Seperators):
    ExtractedString = ""
    ExtractedData = []
    StringSplit = list(String)
    Nested = False

    for char in range(len(StringSplit)):
        if StringSplit[char] == Seperators[0]:
            Nested = True
        elif StringSplit[char] == Seperators[1]:
            Nested = False
            ExtractedData.append(ExtractedString)
            ExtractedString = ""
        elif Nested == True:
            ExtractedString += StringSplit[char]

    return ExtractedData



TestString = "Oh no random shit o--ee aghfdjgh {ImportantData} Oh no im dying oh Bleg ah dam{MoreData}"
print(CheckBetween(TestString,("{","}")))



while True:
    Input = input("Command:")
    if(Input == "Open Inv" or Input == "Open Inventory" or Input == "Inv" or Input == "Open Inventory"):
        print(ReadItems(PlayerInv))

    if(Input == "Fight" or Input == "fight"):
        Panel = textPanel(20,10)
        PlayerHP = textObject("Player HP:" + str(PlayerHealth),1,3)
        EnemyHP = textObject("Enemy HP:" + str(PlayerHealth),3,3)
        Div1 = dividerObject(5)
        Panel.addObjects([PlayerHP,EnemyHP,Div1])

        while True:
            cls()
            print(Panel.drawPanel())
            Action = input("Action:")