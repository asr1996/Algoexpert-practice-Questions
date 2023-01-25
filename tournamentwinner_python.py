def tournamentWinner(competitions, results):
    r = []
    for competition, result in zip(competitions, results):
        winner = competition[(result +1)% 2]
        r.append(winner)
    maxkey = max(r, key =r.count)
    return maxkey
