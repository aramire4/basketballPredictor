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

        print(int(round(homeScore)))
        print(int(round(awayScore)))
        
        update.updateStats(home, homeScore, away, awayScore)

        if homeScore < awayScore:
            return away
        else:
            return home

    def getCompetition(team, data):
        otherTeam = ''
        num = data[team]
        for t in data:
            if data[t] + num is 9:
                otherTeam = t
        return otherTeam
    
        
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
                team = team.rstrip('\n')
                num = int(num)
                info[team] = num
                print(team)
    else:
        with open('eastMatchups.txt') as east:
            for line in east:
                num, team = line.split(' ')
                team = team.rstrip('\n')
                num = int(num)
                info[team] = num
                print(team)

    teamChoice = raw_input('please choose a team from the above options ')
    teamAgainst = getCompetition(teamChoice, info)
    
    if choice is 'a' or 'A':
        print('%s vs %s' % (teamChoice, teamAgainst))
        win = None
        if(info[teamChoice] > info[teamAgainst]):
            win = findWinner(teamChoice, teamAgainst)
        else:
            win = findWinner(teamAgainst, teamChoice)
        print('winner: %s' % win)

    if choice is 'b' or 'B':
        print('%s vs %s' % (teamChoice, teamAgainst))
        adv = False
        winner = False
        game = 1
        win = None
        t1W = 0
        t2W = 0
        champ = None
        if(info[teamChoice] > info[teamAgainst]):
            adv = True
        else:
            adv = False

        while winner is False:
            print('game %s:' % game)
            if adv is True:
                if game is 1 or game is 2 or game is 5 or game is 7:
                    win = findWinner(teamChoice, teamAgainst)
                else:
                    win = findWinner(teamAgainst, teamChoice)
            else:
                if game is 1 or game is 2 or game is 5 or game is 7:
                    win = findWinner(teamAgainst, teamChoice)
                else:
                    win = findWinner(teamChoice, teamAgainst)

            print('winner: %s' % win)
            if win is teamChoice:
                t1W += 1
            else:
                t2W += 1

            if t1W is 4 or t2W is 4:
                winner = True
                if t1W is 4:
                    champ = teamChoice
                else:
                    champ = teamAgainst
            game +=1
        print('%s wins!' % champ)

    else:
        print('To be done')
                
        
