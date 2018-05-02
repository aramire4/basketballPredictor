
teamData = []
with open('teamInfo.txt') as input_file:
    for line in input_file:
       team, hOR, aOR, hDR, aDR = line.split(' ')
       teamData.append((team, hOR, aOR, hDR, aDR))
       """
       teamData[(team)] = hOR, aOR, hDR, aDR#dict(zip(('homeOffense', 'awayOffense', 'homeDefense', 'awayDefense'), (hOR, aOR, hDR, aDR)))
       #teamData.append(team, hOR, aOR, hDR, aDR)
        """

class printInfo():
    print('initial info: ')
    for x in teamData:
        print('team %r: ' % x[0])
        print('Offensive rating: ')
        print('home '+ x[1] + ' away ' + x[2])
        print('Defensive rating: ')
        print('home '+ x[3] + ' away ' + x[4])
    print('\n')
#class determineWinner(team1, team2):
    
