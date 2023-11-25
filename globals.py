import discord
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta
import matplotlib.colors as mcolors

size = 20
H = 40
W = 60

load_dotenv()
intents = discord.Intents.default()
intents.members = True # get_member に必要
client = discord.Client(intents=intents) # 接続に使用するオブジェクト
TOKEN = os.getenv('TOKEN')

facility_dict = {
    '': {"name": "空地", "cost": 0, "range": 0, "income": 0, "population": 0, "price": 0},
    '-': {"name": "解体", "cost": 0},
    'h': {"name": "住宅", "label": "house", "cost": 1000, "range": 0, "income": 10, "population": 3, "price": 1},
    'M': {"name": "マンション", "label": "house", "cost": 50000, "range": 0, "income": 10, "population": 50, "price": 5},
    'T': {"name": "タワーマンション", "label": "house", "cost": 1000000, "range": 0, "income": 50, "population": 200, "price": 20},
    'p': {"name": "発電所", "label": "electricity", "cost": 5000, "range": 10, "income": 10, "price": 1},
    'w': {"name": "上下水道局", "label": "water", "cost": 5000, "range": 10, "income": 10, "price": 1},
    'r': {"name": "電波塔", "label": "network", "cost": 50000, "range": 10, "income": 100, "price": 5},
    's': {"name": "駅", "label": "station", "cost": 100000, "range": 5, "income": 100, "price": 10},
}

def initialize_field_data():
    facility = [['']*W for i in range(H)]
    dir = format(datetime.now(), '%Y%m%d%H')
    os.makedirs(f"log/{dir}", exist_ok=True)
    with open(f"log/{dir}/map.json", 'w') as f:
        json.dump(facility, f)
    query = dict()
    author = dict()
    with open(f"log/query.json", 'w') as f:
        json.dump((query, author), f)
    owner = [['']*W for i in range(H)]
    with open(f"log/owner.json", 'w') as f:
        json.dump((owner), f)
    player = dict()
    with open(f"log/player.json", 'w') as f:
        json.dump(player, f)

def add_player(name, color_name):
    with open(f"log/player.json") as f:
        player = json.load(f)
    try:
        color_rgb = tuple(int(c*255) for c in mcolors.to_rgb(color_name))
        color_gbr = color_rgb[::-1]
    except:
        return "入力が不正です"
    if name in player:
        player[name]["color"] = color_gbr
        with open(f"log/player.json", 'w') as f:
            json.dump(player, f)
        return "色を変更しました"
    else:
        player[name] = {"color": color_gbr, "money": 10000}
        with open(f"log/player.json", 'w') as f:
            json.dump(player, f)
        return "プレイヤーとして追加しました"

def is_admin(message):
    if message.guild and message.author.guild_permissions.administrator:
        return True
    return False
