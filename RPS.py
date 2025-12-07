import random
from collections import defaultdict

def player(prev_play, opponent_history=[], markov_table=defaultdict(lambda: defaultdict(int))):
    """
    Strong RPS player using:
    - Markov chain prediction of opponent sequences
    - Frequency analysis fallback
    - Randomization to avoid predictability
    """
    # Update opponent history
    if prev_play:
        opponent_history.append(prev_play)
    
    # First move is random
    if not opponent_history:
        return random.choice(['R', 'P', 'S'])
    
    # --- Update Markov table ---
    if len(opponent_history) >= 3:
        prev_seq = tuple(opponent_history[-3:-1])  # last 2 moves
        next_move = opponent_history[-1]
        markov_table[prev_seq][next_move] += 1
    
    # --- Predict next move using Markov chain ---
    if len(opponent_history) >= 2:
        last_seq = tuple(opponent_history[-2:])
        if last_seq in markov_table and markov_table[last_seq]:
            # Predict most likely next move
            predicted_move = max(markov_table[last_seq], key=lambda k: markov_table[last_seq][k])
        else:
            predicted_move = None
    else:
        predicted_move = None
    
    # --- Fallback: Frequency analysis ---
    if not predicted_move:
        count_R = opponent_history.count('R')
        count_P = opponent_history.count('P')
        count_S = opponent_history.count('S')
        predicted_move = max(('R', count_R), ('P', count_P), ('S', count_S), key=lambda x: x[1])[0]
    
    # --- Counter the predicted move ---
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    next_move = counter[predicted_move]
    
    # --- Randomize occasionally ---
    if random.random() < 0.1:
        next_move = random.choice(['R', 'P', 'S'])
    
    return next_move
