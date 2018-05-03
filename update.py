from readFromFile import *

def updateStats (home, hScore, away, aScore, gameNumberH, gameNumberA):
    #update the home team's stats
    avgHomeOff = teamData[home]['hOffense']
    #teamData[home]['hOffense'] = (avgHomeOff + hScore) / 2
    teamData[home]['hOffense'] = ((avgHomeOff * (82 + gameNumberH - 1)) + hScore) / (82 + gameNumberH)
    #teamData[home]['hOffense'] = ((avgHomeOff * 82) + hScore) / (83)
    #teamData[home]['hOffense'] = ((avgHomeOff * gameNumber) + hScore) / (gameNumber + 1)

    avgHomeDef = teamData[home]['hDefense']  
    #teamData[home]['hDefense'] = (avgHomeDef + aScore) / 2
    teamData[home]['hDefense'] = ((avgHomeDef * (82 + gameNumberH -1)) + aScore) / (82 + gameNumberH)
    #teamData[home]['hDefense'] = ((avgHomeDef * 82) + aScore) / (83)
    #teamData[home]['hDefense'] = ((avgHomeDef * gameNumber) + aScore) / (gameNumber + 1)

    #update the away team's stats
    avgAwayOff = teamData[away]['aOffense']
    #teamData[away]['aOffense'] = (avgAwayOff + aScore) / 2
    teamData[away]['aOffense'] = ((avgAwayOff * (82 + gameNumberA -1)) + aScore) / (82 + gameNumberA)
    #teamData[away]['aOffense'] = ((avgAwayOff * 82) + aScore) / (83)
    #teamData[away]['aOffense'] = ((avgAwayOff * gameNumber) + aScore) / (gameNumber + 1)

    avgAwayDef = teamData[away]['aDefense']  
    #teamData[away]['aDefense'] = (avgAwayDef + hScore) / 2
    teamData[away]['aDefense'] = ((avgAwayDef * (82 + gameNumberA -1)) + hScore) / (82 + gameNumberA)
    #teamData[away]['aDefense'] = ((avgAwayDef * 82) + hScore) / (83)
    #teamData[away]['aDefense'] = ((avgAwayDef * gameNumber) + hScore) / (gameNumber + 1)
    

    #update the average stats
    avgHOff = teamData['Average']['hOffense']
    teamData['Average']['hOffense'] = (avgHOff + teamData[home]['hOffense'])/2

    avgHDef = teamData['Average']['hDefense']
    teamData['Average']['hDefense'] = (avgHDef + teamData[home]['hOffense'])/2

    avgAOff = teamData['Average']['aOffense']
    teamData['Average']['aOffense'] = (avgAOff + teamData[away]['aOffense'])/2
    
    avgADef = teamData['Average']['aDefense']
    teamData['Average']['aDefense'] = (avgADef + teamData[away]['aDefense'])/2
    
