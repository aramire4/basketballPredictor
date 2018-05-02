# basketballPredictor
Use mid season stats as a base dataset
Keep a dataset of NBA teams and compare defensive and offensive ratings b/w teams
http://www.basketbet.net/how-to-start-betting-online/basketball-betting-types/totals-bets/using-home-away-averages-to-predict-nba-games/

Update team’s ratings after each game, and you can get a basic predictor
Formula for predicting a game:
        vPS (visiting points scored +/-)
        vPA (visiting points allowed +/-)
        hPS (home points scored +/-)
        hPA (home points allowed +/-)

        Find a team’s offense compared to the rest of the league:
            vPS = Road Team's average points scored  League Average road points scored
            hPS = Home Team's average points scored  League Average home points scored

        Find a team’s defense compared to the rest of the league:
                vPA = Road Team's points allowed  Average points allowed by road teams
                hPA = Home Team's average points Allowed  League Average home points allowed


        Find a team’s final score
                vPS * hPA * Team’s Average road score
                hPS * vPA * Team’s Average home score

After the game is finished, update the teams’ averages
