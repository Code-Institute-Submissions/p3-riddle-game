import unittest
import run

class TestRiddleGame(unittest.TestCase):
    """
    Test suite for riddle game
    """
    def test_load_players(self):
        """
        Test to ensure we can read players list from json file
        """
        players = run.load_players()
        self.assertEqual(len(players),15)

    def test_load_riddles(self):
        """
        Test to ensure we can read riddles list from json file
        """
        riddles = run.load_riddles()
        self.assertEqual(len(riddles),6)

    def test_update_player(self):
        """
        Test to ensure we can update a player's status in players.json
        """
        players = run.load_players()
        players[0]["available"] = False
        run.update_players(players)
        self.assertEqual(run.load_players()[0]["available"], False)