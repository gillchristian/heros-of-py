import json


class Interface(object):
    """
        handles the game output and input
    """

    def showWarriosData():
        """
        outputs the heros information
        """
        with open('data/heros.json') as data_file:
            data = json.loads(data_file.read())
        for value in data:
            print('------------------------')
            print('--- {0} ---'.format(value['name']))
            print('Health points: {0}'.format(value['health']))
            print('Damage: {0}'.format(value['damage']))
            print('Habilities:')
            for hability in value['habilities']:
                print('      {0}'.format(hability))
        print('------------------------')

    def classPick(classesAmount):
        """
        prompts the player to pick a class

        @param {int} amount of classes
        @return {int} picked class id
        """
        print('Hello hero!!! Are you ready to start your adventure?')
        print('First you have to choose your Class:')
        Interface.showWarriosData()
        # TODO change the range to programatic number
        print( 'Pick your class inputing a number from 1 to {0}:'.format(classesAmount) )
        picked = input()
        return int(picked) - 1

    def greetPick(className):
        """
        greetings on class pick
        """
        print( 'You chose {0}'.format(className) )
        print( 'Good luck on the road that awaits you hero!')
