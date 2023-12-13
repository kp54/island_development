from globals import *

def add_query(message_list, name, dir):
    with open(f"log/query.json") as f:
        query, author = json.load(f)

    if len(message_list) != 3:
        if name in author:
            del query[author[name]]
            del author[name]
            with open(f"log/query.json", 'w') as f:
                json.dump((query, author), f)
            return "行動をリセットしました"
        return "入力が不正です"
    h, w, fac = int(message_list[0]), int(message_list[1]), message_list[2]
    if not 0 < h < H or not 0 < w < W or not fac in facility_dict:
        return "入力が不正です"

    if str(h*W+w) in query and (name in author and author[name] != str(h*W+w)):
        return "その土地は既に予約済みです"

    with open(f"log/{dir}/owner.json") as f:
        owner = json.load(f)
    if owner[h][w] != "" and name != owner[h][w]:
        return "その土地は既に予約済みです"

    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)
    if player[name]["money"] < facility_dict[fac]["cost"]:
        return "所持金が足りません"

    if name in author:
        del query[author[name]]
    if fac == '-':
        fac = ''
    query[h*W+w] = fac
    author[name] = str(h*W+w)
    with open(f"log/query.json", 'w') as f:
        json.dump((query, author), f)
    if name == owner[h][w]:
        return "行動を予約しました（建設済みの施設を上書きします）"
    return "行動を予約しました"


def exec_query(dir):
    with open(f"log/{dir}/map.json") as f:
        facility = json.load(f)
    with open(f"log/{dir}/owner.json") as f:
        owner = json.load(f)
    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)

    with open(f"log/query.json") as f:
        query, author = json.load(f)
    for p in author:
        coord = int(author[p])
        h = coord // W
        w = coord %  W
        fac = query[author[p]]
        facility[h][w] = fac
        if fac == '':
            owner[h][w] = ''
        else:
            owner[h][w] = p
        player[p]["money"] -= facility_dict[fac]["cost"]

    query.clear()
    author.clear()
    with open(f"log/{dir}/map.json", 'w') as f:
        json.dump((facility), f)
    with open(f"log/query.json", 'w') as f:
        json.dump((query, author), f)
    with open(f"log/{dir}/owner.json", 'w') as f:
        json.dump((owner), f)
    with open(f"log/{dir}/player.json", 'w') as f:
        json.dump(player, f)
