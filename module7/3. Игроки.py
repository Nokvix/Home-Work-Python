def merge_data(players_dict):
    players_list = [full_name + scores for full_name, scores in players_dict.items()]
    return players_list


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
print(merge_data(players))
