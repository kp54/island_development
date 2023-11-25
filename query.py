from globals import *

def add_query(message_list, player):
    if len(message_list) != 3:
        return "入力が不正です"
    h, w, fac = int(message_list[0]), int(message_list[1]), message_list[2]
    if not 0 < h < H or not 0 < w < W or not fac in facility_dict:
        return "入力が不正です"

    with open(f"log/query.json") as f:
        query, author = json.load(f)
    if (h, w) in query:
        return "その土地は既に予約済みです"

    with open(f"log/owner.json") as f:
        owner = json.load(f)
    if owner[h][w] != "" and player != owner[h][w]:
        return "その土地は既に予約済みです"

    if player in author:
        del query[author[player]]
    query[h*W+w] = fac
    author[player] = str(h*W+w)
    with open(f"log/query.json", 'w') as f:
        json.dump((query, author), f)
    return "行動を予約しました"


def exec_query(dir):
    with open(f"log/{dir}/map.json") as f:
        facility = json.load(f)
    with open(f"log/owner.json") as f:
        owner = json.load(f)

    with open(f"log/query.json") as f:
        query, author = json.load(f)
    for p in author:
        coord = int(author[p])
        h = coord // W
        w = coord %  W
        fac = query[author[p]]
        facility[h][w] = fac
        owner[h][w] = p

    query.clear()
    author.clear()
    with open(f"log/{dir}/map.json", 'w') as f:
        json.dump((facility), f)
    with open(f"log/query.json", 'w') as f:
        json.dump((query, author), f)
    with open(f"log/owner.json", 'w') as f:
        json.dump((owner), f)
