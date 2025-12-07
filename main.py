from RPS import player
from RPS_game import play, quincy, random_bot, pattern_bot, adaptive_bot

if __name__ == "__main__":
    num_games = 1000
    
    print("=== Testing against Quincy ===")
    play(player, quincy, num_games, verbose=False)
    
    print("=== Testing against Random Bot ===")
    play(player, random_bot, num_games, verbose=False)
    
    print("=== Testing against Pattern Bot ===")
    play(player, pattern_bot, num_games, verbose=False)
    
    print("=== Testing against Adaptive Bot ===")
    play(player, adaptive_bot, num_games, verbose=False)
