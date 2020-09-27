import random

class WeaponObject():
    def __init__(self,name,rarity,attributes):
        self.name = name
        self.rarity = rarity
        self.attributes = attributes
    def CreateNew(self):
        return [self.name,WeaponObject(self.name,self.rarity,self.attributes)]
    def GetAttack(self):
        DamageMinMax = self.attributes["DamageMinMax"]
        AttackDebufs = self.attributes["AttackDebufs"]
        Damage = 0
        FinalDebufs = []
        Crit = False

        if(random.uniform(0,1) <= self.attributes["CriticalHitRarity"]):
            Damage = self.attributes["CriticalHitDamage"]
            Crit = True
        else:
            Damage = random.randint(DamageMinMax[0],DamageMinMax[1])


        dmgDelt=[Damage,Crit]

        return dmgDelt