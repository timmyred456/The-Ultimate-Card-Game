from CardCode import *
import os, json

# mydict[mydict.keys()[0]]

GameData = os.path.join(os.getcwd(),"GameData")
Debuffs = os.path.join(GameData,"Debuffs")
Objects = os.path.join(GameData,"Objects")

LoadedObjects = []
LoadedDebuffs = []

def LoadDebuffs():
    print("E")


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def LoadAllObjectsInDir(Dir):
    ObjsInDir = os.listdir(Dir)
    ArrayOfObjs = []
    DictOfObjs = {}

    for x in range(len(ObjsInDir)):
        print(ObjsInDir[x])
        LoadedObject = LoadAllItemsInFile(os.path.join(Objects, ObjsInDir[x]))
        ArrayOfObjs.append(LoadedObject)
    
    for x in range(len(ArrayOfObjs)):
        DictOfObjs[ArrayOfObjs[x][0][0]] = ArrayOfObjs[x][0][1]

    return DictOfObjs

print(LoadAllObjectsInDir(Objects))