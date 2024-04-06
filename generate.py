# Given
players = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

from itertools import combinations
from copy import deepcopy

def filterByParties(ptys:list, pairs: list([tuple])) -> list([tuple]):
    # return pairs where neither player is in ptys list
    return [x for x in pairs if ptys.count(x[0]) == 0 and ptys.count(x[1]) == 0]
#  Alternative implementation without using list comprehension
#    rslt = []
#    ptr = 0
#    while ptr < len(pairs):
#        pr = pairs[ptr]
#        if ptys.count(pr[0]) == 0 and  ptys.count(pr[1]) == 0:
#            rslt.append(pr)
#        ptr += 1
#    return rslt

def dropPair(pr:list, pairings: list([tuple])) -> list([tuple]):
    # return list of parings minus pr
    return [x for x in pairings if  pr[0] != x[0] or pr[1] != x[1]]
#  Alternative implementation without using list comprehension
#    ptr = -1
#    for i, pair in enumerate(pairings):
#        if pr[0] == pair[0] and pr[1] == pair[1]:
#            ptr = i
#            break
#    if ptr >= 0:
#        pairings.pop(ptr)
#    return pairings         

def doublesTournament(players: list([str])):
    # Given list of players, produce a listing for a doubles tennis tournament
    # Where the tournament is split into rounds of play in which all players
    # play matches with the different participants
    tournament_pairings = list(combinations(players, 2))
    tournament_rounds = len(players) -1
    matches_per_round = len(players)//4
    tournament_schedule = []
    for rnd in range(tournament_rounds):
        rnd_play_list = []
        # Make true copy of parinings for assigning match play
        match_pairings = deepcopy(tournament_pairings)
        while match_pairings:
            team_one = match_pairings.pop()
            match_pairings = filterByParties(team_one, match_pairings)
            tournament_pairings = dropPair(team_one, tournament_pairings)
            team_two = match_pairings.pop()
            match_pairings = filterByParties(team_two, match_pairings)
            tournament_pairings = dropPair(team_two, tournament_pairings) 
            rnd_play_list.append((team_one, team_two))
        tournament_schedule.append(rnd_play_list)
    for r, round_play in enumerate(tournament_schedule):
        print(f'Round {r+1}')
        for m, match_play in enumerate(round_play):
            print(f'\tMatch {m+1}:  {match_play[0]} vs {match_play[1]}')  

doublesTournament(players) 
