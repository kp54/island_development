from globals import *

def player_dict():
    d = {}
    with open(f"log/player.json") as f:
        player = json.load(f)
    for p in player:
        d[p] = 0
    return d

def solve(facility):
    electricity = [[0]*W for i in range(H)]
    water = [[0]*W for i in range(H)]
    for h in range(H):
        for w in range(W):
            if facility[h][w] in ('p', 'w'):
                r = facility_dict[facility[h][w]]["range"]
                for i in range(r*2+1):
                    for j in range(r+1):
                        if i%2 == 1 and j == r:
                            continue
                        x, y = h-r+(i+1)//2+j, w-i//2+j
                        if 0 < x < H and 0 < y < W:
                            eval(facility_dict[facility[h][w]]["label"])[x][y] = 1

    population = [[0]*W for i in range(H)]
    for h in range(H):
        for w in range(W):
            if facility[h][w] in ('h', 'M', 'T'):
                if electricity[h][w] and water[h][w]:
                    population[h][w] = facility_dict[facility[h][w]]["population"]

    labels  = {}
    price = [[0]*W for i in range(H)]
    for h in range(H):
        for w in range(W):
            fac = facility[h][w]
            if fac == '':
                continue
            r = facility_dict[fac]["range"]
            if facility_dict[fac]["label"] not in labels:
                labels[facility_dict[fac]["label"]] = [[0]*W for i in range(H)]
            for i in range(r*2+1):
                for j in range(r+1):
                    if i%2 == 1 and j == r:
                        continue
                    x, y = h-r+(i+1)//2+j, w-i//2+j
                    if 0 < x < H and 0 < y < W:
                        price[x][y] += facility_dict[fac]["price"]
                        labels[facility_dict[fac]["label"]][x][y] += facility_dict[fac]["price"]

    with open(f"log/owner.json") as f:
        owner = json.load(f)
    income = player_dict()
    for h in range(H):
        for w in range(W):
            fac = facility[h][w]
            if fac == '':
                continue
            p = 0.0
            r = facility_dict[fac]["range"]
            for i in range(r*2+1):
                for j in range(r+1):
                    if i%2 == 1 and j == r:
                        continue
                    x, y = h-r+(i+1)//2+j, w-i//2+j
                    if 0 < x < H and 0 < y < W:
                        p += population[x][y] * facility_dict[fac]["price"] / labels[facility_dict[fac]["label"]][x][y]
            income[owner[h][w]] += int(facility_dict[fac]["income"] * p)

    return price
