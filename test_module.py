import unittest
import RPS

class TestRPS(unittest.TestCase):
    def test_player_function(self):
        move = RPS.player("", [])
        self.assertIn(move, ["R", "P", "S"])

if __name__ == "__main__":
    unittest.main()
