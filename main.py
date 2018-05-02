from readFromFile import *
import update

#print(teamData['San_Antonio']['hOffense'])

class main:

    def __init__(self, team, stats):
        self.team = team
        self.stats = stats

    def findWinner(home, away):
        #Points scored
        homePS = (teamData[home]['hOffense']) / (teamData['Average']['hOffense'])
        awayPS = (teamData[away]['aOffense']) / (teamData['Average']['aOffense'])

        #Points allowed
        homePA = (teamData[home]['hDefense']) / (teamData['Average']['hDefense'])
        awayPA = (teamData[away]['aDefense']) / (teamData['Average']['aDefense'])

        homeScore = homePS * awayPA * teamData[home]['hOffense']
        awayScore = awayPS * homePA * teamData[away]['aOffense']

        print(homeScore)
        print(awayScore)
        
        update.updateStats(home, homeScore, away, awayScore)

        if homeScore > awayScore:
            return home
        else:
            return away

    """ 
    def updateStats(self, home, hScore, away, aScore):
        #update the home team's stats
        avgHomeOff = teamData[home]['hOffense']
        teamData[home]['hOffense'] = (avgHomeOff + hScore) / 2

        avgHomeDef = teamData[home]['hDefense'] 
        teamData[home]['hDefense'] = (avgHomeDef + aScore) / 2

        #update the away team's stats
        avgAwayOff = teamData[away]['aOffense']
        teamData[away]['aOffense'] = (avgAwayOff + aScore) / 2

        avgAwayDef = teamData[away]['aDefense'] 
        teamData[away]['aDefense'] = (avgAeayDef + hScore) / 2

        #update the average stats
    """
    print('a) simulate a game?')
    print('b) simulate the series?')
    print('c) simulate the round?')
    choice = raw_input('what do you want to do? ')
    conf = raw_input('w) west?\ne) east? ')

    
    info = {}
    if conf is 'w' or conf is 'W':
        with open('westMatchups.txt') as west:
            for line in west:
                num, team = line.split(' ')
                info[team] = dict(zip('seed', int(num)))
                print(team)
    else:
        with open('eastMatchups.txt') as east:
            for line in east:
                num, team = line.split(' ')
                info[team] = dict(zip('seed', int(num)))
                print(team)

    teamChoice = raw_input('please choose a team from the above options')

    """
    print('San_Antonio')
    print('Golden_State')
    win = findWinner('San_Antonio', 'Golden_State')
    print(win)
    win = findWinner('San_Antonio', 'Golden_State')
    print(win)
    """
