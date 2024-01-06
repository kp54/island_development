import discord
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta
import matplotlib.colors as mcolors

size = 20
H = 30
W = 40

load_dotenv()
intents = discord.Intents.default()
intents.members = True # get_member に必要
client = discord.Client(intents=intents) # 接続に使用するオブジェクト
TOKEN = os.getenv('TOKEN')

facility_dict = {
    '': {"name": "空地", "cost": 0, "range": 0, "income": 0, "population": 0, "price": 0},
    '-': {"name": "解体", "cost": 0},
    '家': {"name": "住宅", "label": "house", "cost": 1000, "range": 0, "income": 15, "population": 4, "price": 1},
    'マ': {"name": "マンション", "label": "house", "cost": 50000, "range": 0, "income": 20, "population": 15, "price": 5},
    'タ': {"name": "タワーマンション", "label": "house", "cost": 1000000, "range": 0, "income": 40, "population": 50, "price": 20},
    '電': {"name": "発電所", "label": "electricity", "cost": 5000, "range": 10, "income": 10, "price": 1},
    '原': {"name": "原子力発電所", "label": "electricity", "cost": 70000, "range": 10, "income": 30, "price": 5},
    '水': {"name": "上下水道局", "label": "water", "cost": 5000, "range": 10, "income": 10, "price": 1},
    '処': {"name": "上下水道処理施設", "label": "water", "cost": 70000, "range": 10, "income": 30, "price": 5},
    '波': {"name": "電波塔", "label": "network", "cost": 50000, "range": 10, "income": 20, "price": 5},
    '東': {"name": "東京スカイツリー", "label": "network", "cost": 2000000, "range": 15, "income": 50, "price": 15},
    '駅': {"name": "駅", "label": "station", "cost": 100000, "range": 5, "income": 40, "price": 10},
    'S': {"name": "ターミナル駅", "label": "station", "cost": 1000000, "range": 7, "income": 80, "price": 20},
    'ス': {"name": "スーパー", "label": "shop", "cost": 5000, "range": 3, "income": 20, "price": 2},
    '商': {"name": "商店街", "label": "shop", "cost": 100000, "range": 5, "income": 40, "price": 5},
    'デ': {"name": "デパート", "label": "shop", "cost": 500000, "range": 5, "income": 80, "price": 10},
    '学': {"name": "小・中学校", "label": "school1", "cost": 10000, "range": 5, "income": 15, "price": 2},
    '高': {"name": "高等学校", "label": "school2", "cost": 30000, "range": 7, "income": 15, "price": 3},
    '大': {"name": "大学キャンパス", "label": "university", "cost": 100000, "range": 10, "income": 20, "price": 5},
    '畑': {"name": "畑", "label": "factory", "cost": 20000, "range": 5, "income": 20, "price": 2},
    '牧': {"name": "牧場", "label": "factory", "cost": 50000, "range": 5, "income": 20, "price": 3},
    '工': {"name": "工場", "label": "factory", "cost": 100000, "range": 7, "income": 30, "price": 5},
    'I': {"name": "ITクラスター", "label": "factory", "cost": 700000, "range": 8, "income": 70, "price": 10},
    '診': {"name": "診療所", "label": "hospital", "cost": 10000, "range": 5, "income": 15, "price": 2},
    '病': {"name": "病院", "label": "hospital", "cost": 200000, "range": 7, "income": 30, "price": 5},
    '交': {"name": "交番", "label": "police", "cost": 15000, "range": 7, "income": 15, "price": 2},
    '警': {"name": "警察本部", "label": "police", "cost": 300000, "range": 10, "income": 40, "price": 5},
    '消': {"name": "消防署", "label": "fire", "cost": 40000, "range": 5, "income": 25, "price": 3},
    '防': {"name": "消防ヘリポート", "label": "fire", "cost": 500000, "range": 8, "income": 50, "price": 7},
    'ゴ': {"name": "ゴミ埋立地", "label": "trash", "cost": 3000, "range": 8, "income": 10, "price": 1},
    '焼': {"name": "ゴミ焼却場", "label": "trash", "cost": 60000, "range": 8, "income": 20, "price": 5},
    '墓': {"name": "墓地", "label": "ceremony", "cost": 4000, "range": 10, "income": 10, "price": 1},
    '教': {"name": "教会", "label": "ceremony", "cost": 80000, "range": 10, "income": 20, "price": 5},
    '墳': {"name": "前方後円墳", "label": "ceremony", "cost": 500000, "range": 10, "income": 40, "price": 10},
    'ピ': {"name": "ピラミッド", "label": "ceremony", "cost": 2000000, "range": 10, "income": 70, "price": 20},
    '映': {"name": "映画館", "label": "entertainment", "cost": 50000, "range": 5, "income": 20, "price": 5},
    '植': {"name": "植物園", "label": "entertainment", "cost": 300000, "range": 7, "income": 30, "price": 7},
    'A': {"name": "水族館", "label": "entertainment", "cost": 1000000, "range": 10, "income": 50, "price": 10},
    'Z': {"name": "動物園", "label": "entertainment", "cost": 1000000, "range": 10, "income": 50, "price": 10},
    '遊': {"name": "遊園地", "label": "entertainment", "cost": 1000000, "range": 10, "income": 50, "price": 10},
    'D': {"name": "ディズニーランド", "label": "entertainment", "cost": 10000000, "range": 20, "income": 100, "price": 50},
    '寺': {"name": "寺", "label": "temple", "cost": 5000, "range": 5, "income": 15, "price": 1},
    '仏': {"name": "仏閣", "label": "temple", "cost": 70000, "range": 5, "income": 30, "price": 5},
    '金': {"name": "金閣寺", "label": "temple", "cost": 800000, "range": 8, "income": 50, "price": 10},
    'X': {"name": "スフィンクス", "label": "temple", "cost": 2000000, "range": 10, "income": 70, "price": 20},
    '松': {"name": "松屋", "label": "restaurant", "cost": 3000, "range": 3, "income": 15, "price": 1},
    'サ': {"name": "サイゼリヤ", "label": "restaurant", "cost": 3000, "range": 3, "income": 15, "price": 1},
    'M': {"name": "記念碑", "label": "monument", "cost": 30000000, "range": 10, "income": 10, "price": 30},
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
    with open(f"log/{dir}/owner.json", 'w') as f:
        json.dump((owner), f)
    player = dict()
    with open(f"log/{dir}/player.json", 'w') as f:
        json.dump(player, f)
    with open(f"log/save.json", 'w') as f:
        json.dump(dir, f)

def add_player(name, color_name, dir):
    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)
    try:
        color_rgb = tuple(int(c*255) for c in mcolors.to_rgb(color_name))
        color_gbr = color_rgb[::-1]
    except:
        return "入力が不正です"
    if name in player:
        player[name]["color"] = color_gbr
        with open(f"log/{dir}/player.json", 'w') as f:
            json.dump(player, f)
        return "色を変更しました"
    else:
        player[name] = {"color": color_gbr, "money": 10000, "income": 0}
        with open(f"log/{dir}/player.json", 'w') as f:
            json.dump(player, f)
        return "プレイヤーとして追加しました"

def get_stat(name, dir):
    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)
    if name not in player:
        return "まだ参加していません"
    text = f"所持金：{player[name]['money']} (+{player[name]['income']})\n行動予約："
    with open(f"log/query.json") as f:
        query, author = json.load(f)
    if name in author:
        coord = int(author[name])
        h = coord // W
        w = coord %  W
        fac = query[author[name]]
        text += f"({h}, {w}) に {facility_dict[fac]['name']} の建設"
    return text


def is_admin(message):
    if message.guild and message.author.guild_permissions.administrator:
        return True
    return False
