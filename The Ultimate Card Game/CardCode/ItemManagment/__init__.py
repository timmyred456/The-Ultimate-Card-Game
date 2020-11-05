from CardCode.ItemManagment.InventoryObject import *

def ReadItems(InvToRead:InventoryObject):
    InvToRead = InvToRead.Inventory
    ListOfItems = ""
    if len(InvToRead) <= 0:
        return "Its empty"
    else:
        for x in range(0,len(InvToRead)):
            ListOfItems += "(" + str(x+1) + "): "
            ListOfItems = ListOfItems + str(InvToRead[x][0])
            ListOfItems += ",\n" if (x + 1) != len(InvToRead) else "."
        return ListOfItems
