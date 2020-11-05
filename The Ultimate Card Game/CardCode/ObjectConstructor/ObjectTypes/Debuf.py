import random

class DebuffObject():
    def __init__(self,name,attributes):
        self.name = name
        self.attributes = attributes
        self.Type = "Debuff"
        LastsFor = self.attributes["LastsFor"]
        self.TurnsToLast = random.randint(LastsFor[0],LastsFor[1])

    def CreateNew(self):
        return [self.name,WeaponObject(self.name,self.attributes)]
    
    def FightStarted(self):
        if(self.attributes["DamageOnInflicted"][0] != False):
            return self.attributes["DamageOnInflicted"][1]
        else:
            return False

    
    def TurnTick(self):
        self.TurnsToLast -= 1
        if(TurnsToLast > 0):
            return GetAttack()
        else:
            return [self.attributes["EndText"]]


    def GetAttack(self):
        DamagePerTurn = self.attributes["DamagePerTurn"]
        ReducesAttack = self.attributes["ReducesAttack"]
        DebuffText = self.attributes["DebuffText"]

        DmgToDo = 0
        AtkToReduce = 0

        if(DamagePerTurn[0] != False):
            DmgToDo = random.randint(DamagePerTurn[1][0],DamagePerTurn[1][1])

        if(ReducesAttack[0] != False):
            AtkToReduce = random.randint(ReducesAttack[1][0],ReducesAttack[1][1])
        
        StuffDelt=[DmgToDo,AtkToReduce,False]

        return [StuffDelt, DebuffText]