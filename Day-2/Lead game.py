def find_winner(n, scores):
    max_lead = 0
    winner = 0
    total_scores = [0, 0]

    for i in range(n):
        total_scores[0] += scores[i][0]
        total_scores[1] += scores[i][1]
        lead = abs(total_scores[0] - total_scores[1])
        if lead > max_lead:
            max_lead = lead
            winner = 1 if total_scores[0] > total_scores[1] else 2

    return winner, max_lead

n = int(input())
scores = []
for i in range(n):
    scores.append(list(map(int, input().split())))

winner, max_lead = find_winner(n, scores)
print(winner, max_lead)