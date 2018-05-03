from readFromFile import *
import update
#from predictRound import *
#import predictRound


class main:

    def __init__(self, team, stats):
        self.team = team
        self.stats = stats

    def findWinner(home, away, num):
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
        teamData[home]['gamesPlayed'] += 1
        teamData[away]['gamesPlayed'] += 1
        
        update.updateStats(home, homeScore, away, awayScore, teamData[home]['gamesPlayed'],
        teamData[away]['gamesPlayed'])

        if homeScore < awayScore:
            return away
        else:
            return home
   

    def roundWinner(teamChoice, teamAgainst, info, findWinner):
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
                    win = findWinner(teamChoice, teamAgainst, game)
                else:
                    win = findWinner(teamAgainst, teamChoice, game)
            else:
                if game is 1 or game is 2 or game is 5 or game is 7:
                    win = findWinner(teamAgainst, teamChoice, game)
                else:
                    win = findWinner(teamChoice, teamAgainst, game)

            print('winner: %s \n' % win)
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
        print('%s wins the series' % champ)
        return champ
   

    def simulateRound(teamOrder, nextRound, info, roundWinner, getCompetition, findWinner):
        nextRound = []
        for i in range(0, len(teamOrder), 2):
            teamChoice = teamOrder[i]
            teamAgainst = getCompetition(teamChoice, teamOrder)
            win = roundWinner(teamChoice, teamAgainst, info, findWinner)
            nextRound.append(win)
            if(i+1 != len(teamOrder)-1):
                cont = raw_input('Press enter to go to the next game ')
        return nextRound


    #def getCompetition(team, data):
    def getCompetition(team, order):
        otherTeam = ''
        pos = order.index(team)
        if pos % 2 is 0:
            otherTeam = order[pos+1]
        else:
            otherTeam = order[pos-1]
        return otherTeam
    
        
    print('a) simulate a game?')
    print('b) simulate the series?')
    print('c) simulate the round?')
    choice = raw_input('what do you want to do? ')
    conf = raw_input('w) west?\ne) east? ')

    
    info = {}
    teamOrder = []
    if conf is 'w' or conf is 'W':
        with open('westMatchups.txt') as west:
            for line in west:
                num, team = line.split(' ')
                team = team.rstrip('\n')
                num = int(num)
                teamOrder.append(team)
                info[team] = num
                print(team)
    else:
        with open('eastMatchups.txt') as east:
            for line in east:
                num, team = line.split(' ')
                team = team.rstrip('\n')
                num = int(num)
                teamOrder.append(team)
                info[team] = num
                print(team)

    if choice is 'a' or choice is 'A':
        teamChoice = raw_input('please choose a team from the above options ')
        teamAgainst = getCompetition(teamChoice, teamOrder)
        #teamAgainst = getCompetition(teamChoice, info)
        print('%s vs %s' % (teamChoice, teamAgainst))
        win = None
        if(info[teamChoice] > info[teamAgainst]):
            win = findWinner(teamChoice, teamAgainst, 1)
        else:
            win = findWinner(teamAgainst, teamChoice, 1)
        print('winner: %s' % win)

    elif choice is 'b' or choice is 'B':
        teamChoice = raw_input('please choose a team from the above options ')
        teamAgainst = getCompetition(teamChoice, teamOrder)
        #teamAgainst = getCompetition(teamChoice, info)
        win = roundWinner(teamChoice, teamAgainst, info, findWinner)

    else:
        nextRound = []
        while (len(teamOrder) != 1):
            temp = simulateRound(teamOrder, nextRound, info, roundWinner, getCompetition,
            findWinner)
            #nextRound = temp
            teamOrder = temp
            ans = raw_input('do you want to see the results of the next round?\ny or n? ')
            ans = ans.rstrip('\n')
            if ans == 'n' or ans == 'N':
                break
                #cont = False
                
        """
        for i in range(0, len(teamOrder), 2):
            teamChoice = teamOrder[i]
            teamAgainst = getCompetition(teamChoice, teamOrder)
            win = roundWinner(teamChoice, teamAgainst, info, findWinner)
            nextRound.append(win)
            if(not i is len(teamOrder)):
                cont = raw_input('Press enter to go to the next game ')
        """ 
        #print('To be done')

                
        
