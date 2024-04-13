import random
import json


def round_robin(player_list, num_rotate):
    return player_list[num_rotate:] + player_list[:num_rotate]


def create_round_robin(player_list, courts, rounds):
    _results = []
    num_playing = len(courts) * 4
    num_sitting = len(player_list) % num_playing
    for _round in range(rounds):
        players = player_list[:num_playing]
        sitting = [player for player in player_list if player not in players]
        result = {"Round": _round + 1, "Playing": players, "Sitting": sitting}
        _results.append(result)
        player_list = round_robin(player_list, num_sitting)
    return _results


def create_matches(rr_results: list, courts: list):
    _results = []
    for result in rr_results:
        sitting = ", ".join(result["Sitting"])
        for i, court in enumerate(courts):
            match = {
                "Round": result["Round"],
                "Court": court,
                "Match": {
                    "Team1": f"{result['Playing'][i * 2]}, {result['Playing'][i * 2 + 1]}",
                    "Team2": f"{result['Playing'][i * 2 + 2]}, {result['Playing'][i * 2 + 3]}",
                    "Sitting": sitting,
                },
            }
            _results.append(match)
    return _results


if __name__ == "__main__":
    ROUNDS = 10
    COURTS = ["5", "6"]
    PLAYERS = [
        "Michael",
        "Cavan",
        "Jason J",
        "Jason G",
        "Timothy",
        "Marc",
        "Bryce",
        "JD",
        "Daniel",
    ]
    random.shuffle(PLAYERS)
    # generate_matches(PLAYERS, COURTS, ROUNDS)
    results = create_round_robin(PLAYERS, COURTS, ROUNDS)
    print(json.dumps(create_matches(results, COURTS), indent=4))
    # print(create_teams(results, COURTS))
