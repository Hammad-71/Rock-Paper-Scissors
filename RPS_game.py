import random

# --- Existing Bots ---
def quincy(prev_play, opponent_history=[]):
    """Quincy repeats opponent's last move"""
    if not prev_play:
        return random.choice(['R','P','S'])
    return prev_play

def random_bot(prev_play, opponent_history=[]):
    """Random bot"""
    return random.choice(['R','P','S'])

def pattern_bot(prev_play, opponent_history=[]):
    """Pattern bot: R -> P -> S -> repeat"""
    if not opponent_history:
        return 'R'
    mapping = {'R':'P','P':'S','S':'R'}
    return mapping[opponent_history[-1]]

# --- New Challenging Bot ---
def adaptive_bot(prev_play, opponent_history=[]):
    """
    AdaptiveBot:
    - Predicts your next move based on your last move
    - Plays the counter to it
    """
    if not opponent_history:
        return random.choice(['R','P','S'])
    
    # Predict your next move based on your last move
    last_your_move = opponent_history[-1]
    # Simple prediction: assume you repeat the same move
    counter = {'R':'P','P':'S','S':'R'}
    return counter[last_your_move]

# --- Game engine ---
def play(player1, player2, num_games=1000, verbose=False):
    score1 = 0
    score2 = 0
    last1 = ''
    last2 = ''
    history1 = []
    history2 = []
    
    for i in range(num_games):
        move1 = player1(last2, history1)
        move2 = player2(last1, history2)
        
        history1.append(move2)
        history2.append(move1)
        
        # Determine winner
        if move1 == move2:
            winner = 0
        elif (move1=='R' and move2=='S') or (move1=='P' and move2=='R') or (move1=='S' and move2=='P'):
            winner = 1
            score1 += 1
        else:
            winner = 2
            score2 += 1
        
        last1 = move1
        last2 = move2
        
        if verbose:
            print(f"Game {i+1}: Player1={move1}, Player2={move2}, Winner={winner}")
    
    print(f"\nFinal Score -> Player1: {score1}, Player2: {score2}")
    print(f"Player1 Win Rate: {score1/num_games*100:.2f}%")
    print(f"Player2 Win Rate: {score2/num_games*100:.2f}%\n")
