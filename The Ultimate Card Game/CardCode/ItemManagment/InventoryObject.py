class InventoryObject():
    def __init__(self,MaxSlots=8):
        self.Inventory = []
        self.MaxSlots = MaxSlots
    def addItem(self,item):
        try:
            self.Inventory.append(item.CreateNew())
        except:
            raise TypeError


