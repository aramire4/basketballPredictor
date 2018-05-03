teamData = {}
#teamInfo.txt
#round2Info.txt
with open('teamInfo.txt') as input_file:
    for line in input_file:
       team, hOR, aOR, hDR, aDR = line.split(' ')
       teamData[team] = dict(zip(('hOffense', 'aOffense', 'hDefense', 'aDefense', 'gamesPlayed'), 
                                (float (hOR), float (aOR), float (hDR), float (aDR), 0)))
       


def printInfo():
    print('initial info: ')
    for x in teamData:
        print(x)
        print('Offensive rating: ')
        print('home '+ teamData[x]['hOffense'] + ' away ' + teamData[x]['aOffense'])
        print('Defensive rating: ')
        print('home '+ teamData[x]['hDefense'] + ' away ' + teamData[x]['aDefense'])
    print('\n')


"""
    print('team %r: ' % x[0])
    print('Offensive rating: ')
    print('home '+ x[1] + ' away ' + x[2])
    print('Defensive rating: ')
    print('home '+ x[3] + ' away ' + x[4])
    print('\n')
"""
#class determineWinner(team1, team2):

