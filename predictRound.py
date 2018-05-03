from readFromFile import *

def roundWinner(teamChoice, teamAgainst):
    import main
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
                win = main.findWinner(teamChoice, teamAgainst)
            else:
                win = main.findWinner(teamAgainst, teamChoice)
        else:
            if game is 1 or game is 2 or game is 5 or game is 7:
                win = main.findWinner(teamAgainst, teamChoice)
            else:
                win = main.findWinner(teamChoice, teamAgainst)

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
    print('%s wins!\n' % champ)
    return champ
