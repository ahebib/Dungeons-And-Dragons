class Character:
    def __init__(self, cName, cRace, cClass):
        self.characterName = cName
        self.characterRace = cRace
        self.characterClass = cClass

    def getName(self):
        return self.characterName
    
    def getRace(self):
        return self.characterRace
    
    def getClass(self):
        return self.characterClass
