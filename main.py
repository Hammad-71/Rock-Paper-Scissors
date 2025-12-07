from RPS import player
from RPS_game import play

# Simple opponent bot that always plays Rock
def opponent(prev_play, opponent_history=[]):
    return "R"

# Play 50 games and print results
play(player, opponent, 50)