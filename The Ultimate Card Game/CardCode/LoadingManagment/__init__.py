from CardCode import *
import os, json

# mydict[mydict.keys()[0]]

def LoadDebuffs():
    print("E")

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def LoadAllObjectsInDir(Dir,ObjectType):
    ObjsInDir = os.listdir(Dir)
    ArrayOfObjs = []
    DictOfObjs = {}

    for x in range(len(ObjsInDir)):
        LoadedObject = LoadAllItemsInFile(os.path.join(Dir, ObjsInDir[x]))
        for y in range(len(LoadedObject)):
            if(LoadedObject[y][1].Type == ObjectType):
                ArrayOfObjs.append(LoadedObject)
    
    for x in range(len(ArrayOfObjs)):
        DictOfObjs[ArrayOfObjs[x][0][0]] = ArrayOfObjs[x][0][1]

    return DictOfObjs