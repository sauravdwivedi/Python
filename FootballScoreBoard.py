#! /usr/bin/python3

"""
The script provides an inplimentation of the Football World Cup Score 
Board. The game starts with capturing home team and away team names,
with initial scoreboard 0 - 0, and updates scoreboard by capturing
teams' scores. Finally script clears score board and finishes a game.
The summary of games is listed by hishest total scores. In case of 
total score clash, most recent game listed appears first.

Input: 

5
Mexico,Canada,0,5
Spain,Brazil,10,2
Germany,France,2,2
Uruguay,Italy,6,6
Argentina,Australia,3,1

First line refers to number of matches. Each following line has home
team, away team, home team score and away team scores.

Output:

Uruguay 6 - Italy 6
Spain 10 - Brazil 2
Mexico 0 - Canada 5
Argentina 3 - Australia 1
Germany 2 - France 2
"""

class Game:
    """Class to model a game"""
    def __init__(self):
        self.home_team = "TeamA"
        self.away_team = "TeamB"
        self.home_team_score = 0
        self.away_team_score = 0
        self.score_board = " - - "
        self.total_score = 0
        self.summary = ""
    
    def start_game(self, home_team, away_team):
        """Method to start a game and update the score board"""
        self.home_team = home_team
        self.away_team = away_team
        self.score_board = f"{self.home_team} {self.home_team_score}"\
            f" - {self.away_team} {self.away_team_score}"
        return self.score_board
        
    def update_score(self, home_team_score, away_team_score):
        """Method to update score board by capturing teams' scores"""
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score
        self.score_board = f"{self.home_team} {self.home_team_score}"\
            f" - {self.away_team} {self.away_team_score}"
        return self.score_board
        
    def finish_game(self):
        """Method to finish the game and clean up dashboard"""
        self.total_score = self.home_team_score + self.away_team_score
        self.summary = self.score_board
        self.score_board = " - - "
        return self.score_board

if __name__ == '__main__':
    input_file = "FootballScoreBoard_input.txt"
    output_file = "FootballScoreBoard_output.txt"
    try:
        with open(input_file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    else:
        num_of_games = int(lines[0].strip())
        matches = [lines[i].strip().split(",") for i in range(1, num_of_games+1)]
        games = []
        print("\tNew match!")
        print("Scoreboard: ", " - - ")
        for match in matches:
            game = Game()
            home_team = match[0].strip()
            away_team = match[1].strip()
            game.start_game(home_team, away_team)
            print("Scoreboard: ", game.score_board)
            home_team_score = int(match[2].strip())
            away_team_score = int(match[3].strip())
            game.update_score(home_team_score, away_team_score)
            print("Scoreboard: ", game.score_board)
            game.finish_game()
            if match != matches[num_of_games-1]:
                print("\tNew match!")
                print("Scoreboard: ", game.score_board)
            games.insert(0, game)
        games = sorted(games, key=lambda x: x.total_score, reverse=True)
        print("\n\tSummary of games! \n")
        with open(output_file, 'w') as outfile:
            for game in games:
                print(game.summary)
                outfile.write(game.summary)
                outfile.write('\n')
        print(f"\nOutput written in file {output_file}!")
            
