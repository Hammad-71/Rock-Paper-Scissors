
def player(prev_play, opponent_history=[]):
    # Save opponent moves
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history, play Rock by default
    if len(opponent_history) < 3:
        return "R"

    # --- Frequency Strategy ---
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1
    most_common = max(freq, key=freq.get)
    counter = {"R": "P", "P": "S", "S": "R"}
    guess_by_freq = counter[most_common]

    # --- Pattern Prediction Strategy ---
    if len(opponent_history) >= 3:
        last_two = "".join(opponent_history[-2:])
        patterns = {}

        for i in range(len(opponent_history) - 2):
            key = opponent_history[i] + opponent_history[i + 1]
            next_move = opponent_history[i + 2]
            if key not in patterns:
                patterns[key] = {"R": 0, "P": 0, "S": 0}
            patterns[key][next_move] += 1

        if last_two in patterns:
            predicted = max(patterns[last_two], key=patterns[last_two].get)
            guess_by_pattern = counter[predicted]
        else:
            guess_by_pattern = guess_by_freq
    else:
        guess_by_pattern = guess_by_freq

    # --- Anti-Cycle Strategy ---
    if len(opponent_history) >= 5:
        recent = opponent_history[-5:]
        if len(set(recent)) == 3:
            cycle_order = {"R": "P", "P": "S", "S": "R"}
            last = opponent_history[-1]
            return cycle_order[last]

    return guess_by_pattern
