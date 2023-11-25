import asyncio
import random
import string
from discord.ext import tasks
# from docs import *
from globals import *
from query import *
from image import *
from solver import *



# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print("testplaying")


# 19時に実行される処理
# @tasks.loop(seconds=30)
# async def time_check():
#     # 現在の時刻
#     now = datetime.now()
#     if now.hour == 19:
#         # 19時なら自動ツイート
#         channel = client.get_channel(KABITTER)
#         await channel.send(generator.generate())
#     # 次の時刻
#     if now.hour < 19:
#         tomorrow = now
#     else:
#         tomorrow = now + timedelta(days=1)
#     tomorrow = tomorrow - timedelta(hours=(now.hour-19))
#     tomorrow = tomorrow - timedelta(minutes=now.minute)
#     tomorrow = tomorrow - timedelta(seconds=now.second)
#     td = tomorrow - now
#     # 翌19時まで待機
#     print(tomorrow)
#     await asyncio.sleep(td.total_seconds())


@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # ヘルプ
    # if message.content.startswith(('!help')):
    #     text = emithelp(message)
    #     await message.channel.send(text)
    #     return
    # if message.content.startswith(('!log')):
    #     text = change_log(message)
    #     await message.channel.send(text)
    #     return

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
        # 初期化コマンド
        if message.content.startswith('!join'):
            await message.channel.send(add_player(message.author.name, message.content.split()[1]))
            return
        # クエリの追加
        if message.content.startswith('!query'):
            await message.channel.send(add_query(message.content.split()[1:], message.author.name))
            return
        # クエリの実行
        if message.content.startswith('!exec'):
            exec_query(message.content.split()[1])
            return
        # 画像生成テスト
        if message.content.startswith('!img'):
            dir = message.content.split()[1]
            with open(f"log/{dir}/map.json") as f:
                facility = json.load(f)
            price = solve(facility)
            await message.channel.send(file=discord.File(create_map_image(price, facility)))


# ループ処理
# time_check.start()
# botの接続と起動
client.run(TOKEN)
