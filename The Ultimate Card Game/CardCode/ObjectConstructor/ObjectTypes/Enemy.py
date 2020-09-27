import random

class EnemyObject():
    def __init__(self,name,rarity,attributes):
        self.name = name
        self.rarity = rarity
        self.attributes = attributes
        self.health = attributes["health"]

    def CreateNew(self):
        return [self.name,EnemyObject(self.name,self.rarity,self.attributes)]

    def DealDamage(self,DamageToDeal):
        self.health -= DamageToDeal

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