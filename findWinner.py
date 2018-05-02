from readFromFile import *
from main import *

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
    #if(homeScore < awayScore) return awayScore
    #else return homeScore
