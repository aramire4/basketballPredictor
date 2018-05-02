from readFromFile import *

def updateStats (home, hScore, away, aScore):
    #update the home team's stats
    avgHomeOff = teamData[home]['hOffense']
    teamData[home]['hOffense'] = (avgHomeOff + hScore) / 2

    avgHomeDef = teamData[home]['hDefense']  
    teamData[home]['hDefense'] = (avgHomeDef + aScore) / 2

    #update the away team's stats
    avgAwayOff = teamData[away]['aOffense']
    teamData[away]['aOffense'] = (avgAwayOff + aScore) / 2

    avgAwayDef = teamData[away]['aDefense']  
    teamData[away]['aDefense'] = (avgAwayDef + hScore) / 2

    #update the average stats
