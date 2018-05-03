from readFromFile import *

def updateStats (home, hScore, away, aScore, gameNumber):
    #update the home team's stats
    avgHomeOff = teamData[home]['hOffense']
    #teamData[home]['hOffense'] = (avgHomeOff + hScore) / 2
    #teamData[home]['hOffense'] = ((avgHomeOff * (82 + gameNumber - 1)) + hScore) / (82 + gameNumber)
    teamData[home]['hOffense'] = ((avgHomeOff * 82) + hScore) / (83)

    avgHomeDef = teamData[home]['hDefense']  
    #teamData[home]['hDefense'] = (avgHomeDef + aScore) / 2
    #teamData[home]['hDefense'] = ((avgHomeDef * (82 + gameNumber -1)) + aScore) / (82 + gameNumber)
    teamData[home]['hDefense'] = ((avgHomeDef * 82) + aScore) / (83)

    #update the away team's stats
    avgAwayOff = teamData[away]['aOffense']
    #teamData[away]['aOffense'] = (avgAwayOff + aScore) / 2
    #teamData[away]['aOffense'] = ((avgAwayOff * (82 + gameNumber -1)) + aScore) / (82 + gameNumber)
    teamData[away]['aOffense'] = ((avgAwayOff * 82) + aScore) / (83)

    avgAwayDef = teamData[away]['aDefense']  
    #teamData[away]['aDefense'] = (avgAwayDef + hScore) / 2
    #teamData[away]['aDefense'] = ((avgAwayDef * (82 + gameNumber -1)) + hScore) / (82 + gameNumber)
    teamData[away]['aDefense'] = ((avgAwayDef * 82) + hScore) / (83)
    

    #update the average stats
    avgHOff = teamData['Average']['hOffense']
    teamData['Average']['hOffense'] = (avgHOff + teamData[home]['hOffense'])/2

    avgHDef = teamData['Average']['hDefense']
    teamData['Average']['hDefense'] = (avgHDef + teamData[home]['hOffense'])/2

    avgAOff = teamData['Average']['aOffense']
    teamData['Average']['aOffense'] = (avgAOff + teamData[away]['aOffense'])/2
    
    avgADef = teamData['Average']['aDefense']
    teamData['Average']['aDefense'] = (avgADef + teamData[away]['aDefense'])/2
    
