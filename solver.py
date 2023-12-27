from globals import *

def solve(dir, pick="all"):
    with open(f"log/{dir}/map.json") as f:
        facility = json.load(f)
    population = [[0]*W for i in range(H)]
    for h in range(H):
        for w in range(W):
            if facility[h][w] in ('家', 'マ', 'タ'):
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
                        if pick == "all" or pick == facility_dict[fac]["label"]:
                            price[x][y] += facility_dict[fac]["price"]
                        labels[facility_dict[fac]["label"]][x][y] += facility_dict[fac]["price"]

    with open(f"log/{dir}/owner.json") as f:
        owner = json.load(f)
    income = dict()
    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)
    for p in player:
        income[p] = 0
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

    return price, income
