import json
from adventurer.character import Character

def main():
    c = loadCharacter()
    campaignCharacter = Character(c["name"], c["race"], c["class"])

    startCampaign(campaignCharacter)

def loadCharacter():
    f = open('character.txt', 'r')
    characterStr = f.read()
    characterStr = characterStr
    characterJSON = json.loads(characterStr)
    return characterJSON

def startCampaign(campaignCharacter):
    print('So the journey begins for ' + campaignCharacter.getName() + ' the ' + campaignCharacter.getRace() + ' ' + campaignCharacter.getClass() + '!')
    print('\nLoading...(not really)\n')

    # Fetch adventure from JSON file

    # First pass at asking player response
    response = askPlayerResponse('You wake up in your bed feeling groggy. You want to sleep more but you have to get up and make yourself breakfast and a morning drink. \nWhere do you want to start? (breakfast, drink) ')

    if (response == 'breakfast'):
        print('You proceed to make some eggs')
    elif (response == 'drink'):
        print('You make yourself a protein shake')

def askPlayerResponse(q):
    return input(q)

main()
