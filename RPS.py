def player(prev_play, opponent_history=[], strategy_score={"freq": 0, "pattern": 0, "cycle": 0}):
    # Save opponent moves
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history, play Rock by default
    if len(opponent_history) < 3:
        return "R"

    counter = {"R": "P", "P": "S", "S": "R"}

    # --- Frequency Strategy ---
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1
    most_common = max(freq, key=freq.get)
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
    guess_by_cycle = None
    if len(opponent_history) >= 5:
        recent = opponent_history[-5:]
        if len(set(recent)) == 3:
            cycle_order = {"R": "P", "P": "S", "S": "R"}
            last = opponent_history[-1]
            guess_by_cycle = cycle_order[last]
        else:
            guess_by_cycle = guess_by_pattern
    else:
        guess_by_cycle = guess_by_pattern

    # --- Adaptive Countering System ---
    strategy_outputs = {
        "freq": guess_by_freq,
        "pattern": guess_by_pattern,
        "cycle": guess_by_cycle
    }

    # Update score of each strategy
    if prev_play:
        for strat, move in strategy_outputs.items():
            if (
                (move == "R" and prev_play == "S") or
                (move == "P" and prev_play == "R") or
                (move == "S" and prev_play == "P")
            ):
                strategy_score[strat] += 1  # that strategy would have won

    # Pick strategy with highest score
    best_strategy = max(strategy_score, key=strategy_score.get)

    return strategy_outputs[best_strategy]
