def play(player1, player2, num_games, verbose=False):
    print(f"Playing {num_games} games:")
    p1_prev = ""
    p2_prev = ""
    p1_history = []
    p2_history = []
    p1_wins = 0
    p2_wins = 0
    ties = 0

    for _ in range(num_games):
        p1_move = player1(p2_prev, p1_history)
        p2_move = player2(p1_prev, p2_history)

        p1_history.append(p1_move)
        p2_history.append(p2_move)

        if p1_move == p2_move:
            ties += 1
            result = "Tie"
        elif beats(p1_move, p2_move):
            p1_wins += 1
            result = "Player 1 wins"
        else:
            p2_wins += 1
            result = "Player 2 wins"

        if verbose:
            print(f"P1: {p1_move} | P2: {p2_move} => {result}")

        p1_prev = p1_move
        p2_prev = p2_move

    print(f"Player 1 wins: {p1_wins}")
    print(f"Player 2 wins: {p2_wins}")
    print(f"Ties: {ties}")

def beats(one, two):
    return (
        (one == "R" and two == "S")
        or (one == "S" and two == "P")
        or (one == "P" and two == "R")
    )
