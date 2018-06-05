def electionsWinners(votes, k):
    current_max = max(votes)
    possible_winners = 0
    
    if k == 0 and votes.count(current_max) == 1:
        possible_winners += 1
    for vote in votes:
        if vote + k > current_max:
            possible_winners += 1

    return possible_winners