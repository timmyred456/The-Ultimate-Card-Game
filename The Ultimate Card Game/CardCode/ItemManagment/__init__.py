from CardCode.ItemManagment.InventoryObject import *


def AddItem(ItemToAdd,TargetInv:InventoryObject):
    if((len(TargetInv.Inventory) + 1) <= TargetInv.MaxSlots):
        TargetInv.Inventory.append(ItemToAdd)

def ReadItems(InvToRead:InventoryObject):
    InvToRead = InvToRead.Inventory
    ListOfItems = ""
    if len(InvToRead) <= 0:
        return "Inv Empty!"
    else:
        for x in range(0,len(InvToRead)):
            ListOfItems += "(" + str(x+1) + "): "
            ListOfItems = ListOfItems + str(InvToRead[x][0])
            if (x + 1) != len(InvToRead):
                ListOfItems += ",\n"
            else:
                ListOfItems += ","
        return ListOfItems
