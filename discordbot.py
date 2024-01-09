import asyncio
import os
import shutil

from discord.ext import tasks

from globals import *
from query import *
from image import *
from solver import *


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print("Welcome to 孤島開発")

    # ループ処理
    time_check.start()


# 1時間ごとに実行される処理
@tasks.loop(seconds=30)
async def time_check():
    # 現在の時刻
    now = datetime.now()
    new = format(now, '%Y%m%d%H')
    with open(f"log/save.json") as f:
        dir = json.load(f)
    if new != dir:
        shutil.copytree(f"log/{dir}", f"log/{new}")
        exec_query(new)
        with open(f"log/save.json", 'w') as f:
            json.dump(new, f)
        _, income = solve(new)
        print(income)
        with open(f"log/{new}/player.json") as f:
            player = json.load(f)
        for p in income:
            player[p]["money"] += income[p]
            player[p]["income"] = income[p]
        with open(f"log/{new}/player.json", 'w') as f:
            json.dump(player, f)
    # 次の時刻
    next = now + timedelta(hours=1) - timedelta(minutes=now.minute) - timedelta(seconds=now.second)
    td = next - now
    # 1時間後まで待機
    print(next)
    await asyncio.sleep(td.total_seconds())


@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    with open(f"log/save.json") as f:
        dir = json.load(f)

    # オーナーのみ
    if is_admin(message):
        # シャットダウン
        if message.content == '!sd':
            await client.logout()
            print("Bye!!")
            return
        # 初期化コマンド
        if message.content == '!init':
            initialize_field_data()
            return
    # 参加コマンド
    if message.content.startswith('!join'):
        await message.channel.send(add_player(message.author.name, message.content.split()[1], dir))
        return
    # 状態取得コマンド
    if message.content == '!stat':
        await message.channel.send(get_stat(message.author.name, dir))
        return
    # クエリの追加
    if message.content.startswith('!q'):
        await message.channel.send(add_query(message.content.split()[1:], message.author.name, dir))
        return
    # 画像生成
    if message.content.startswith('!img'):
        if message.content == '!img':
            price, _ = solve(dir)
            await message.channel.send(file=discord.File(create_map_image(price, dir)))
        else:
            price, _ = solve(dir, pick=message.content.split()[1])
            await message.channel.send(file=discord.File(create_map_image(price, dir, pick=message.content.split()[1])))


if not os.path.exists('log'):
    os.mkdir('log')

if not os.path.exists('log/save.json'):
    initialize_field_data()

# botの接続と起動
client.run(TOKEN)
