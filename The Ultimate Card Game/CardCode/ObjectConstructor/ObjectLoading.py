from CardCode.ObjectConstructor.ObjectTypes import *
import json, random

def LoadObject(ObjectData):
    curType = ObjectData["type"]

    if(curType == "Weapon"):
        Newobject = WeaponObject(ObjectData["name"],ObjectData["rarity"],ObjectData["attributes"])
    if(curType == "Enemy"):
        Newobject = EnemyObject(ObjectData["name"],ObjectData["rarity"],ObjectData["attributes"])
    
    x = [ObjectData["name"],Newobject]
    
    return x



def LoadAllItemsInFile(ItemFile):
    ToLoad = open(ItemFile,"r")
    JsonLoaded = json.loads(ToLoad.read())
    DictOfObjs = {}

    for x in range(len(JsonLoaded)):
        LoadedObject = LoadObject(JsonLoaded[x])
        DictOfObjs[x] = LoadedObject

    return DictOfObjs
