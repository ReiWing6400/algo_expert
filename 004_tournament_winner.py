HOME_TEAM_WON = 1


# O(nlog(n)) time | O(n) space
def tournament_winner_my(competitions, results):
    scores = {}

    for i in range(len(results)):
        if results[i] == 0:
            winner = competitions[i][1]
            if winner in scores:
                scores[winner] += 3
            else:
                scores[winner] = 3
        else:
            winner = competitions[i][0]
            if winner in scores:
                scores[winner] += 3
            else:
                scores[winner] = 3

    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    champion = list(sorted_scores.keys())[len(sorted_scores)-1]

    return champion


# O(n) time | O(k) space
def tournament_winner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


print(tournament_winner([["HTML", "C#"],
                         ["C#", "Python"],
                         ["Python", "HTML"]], [0, 0, 1]))
