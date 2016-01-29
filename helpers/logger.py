class Logger(object):
    """
        helper class to handle logging functions
    """

    # logs hero and monster health
    def health(hero = 0, monster = 0):
        print('%----------------------%')
        print('hero health: {0} \nmosnter:{1} health {2}'.format(hero.hp, monster.name, monster.hp))
        print('%----------------------%')
