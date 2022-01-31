#! /usr/bin/python3

import unittest
import FootballScoreBoard as fsb

class ScoreBoardTestCase(unittest.TestCase):
    """Tests for 'FootballScoreBoard.py'."""
    
    def test_start_game_one(self):
        """Do home and away teams like 'Mexico' and 'Canada' work?"""
        home_team = "Mexico"
        away_team = "Canada"
        game = fsb.Game()
        result = game.start_game(home_team, away_team)
        self.assertEqual(result, 'Mexico 0 - Canada 0')
        
    def test_start_game_two(self):
        """Do home and away teams like ' ' and 'United States of America' work?"""
        home_team = " "
        away_team = "United States of America"
        game = fsb.Game()
        result = game.start_game(home_team, away_team)
        self.assertEqual(result, '  0 - United States of America 0')
        
    def test_update_score_one(self):
        """Do home team and away team scores like '0' and '5.6' work?"""
        home_team_score = 0
        away_team_score = 5.6
        game = fsb.Game()
        result = game.update_score(home_team_score, away_team_score)
        self.assertEqual(result, 'TeamA 0 - TeamB 5.6')
        
    def test_update_score_two(self):
        """Do home team and away team scores like 'None' and '15616546451651' work?"""
        home_team_score = None
        away_team_score = 15616546451651
        game = fsb.Game()
        result = game.update_score(home_team_score, away_team_score)
        self.assertEqual(result, 'TeamA None - TeamB 15616546451651')        
        
    def test_finish_game(self):
        """Does finish game work?"""
        game = fsb.Game()
        result = game.finish_game()
        self.assertEqual(result, ' - - ')
        
if __name__ == '__main__':
    unittest.main()
