import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw

from globals import *

def create_map_image(land, dir, pick="all"):
    with open(f"log/{dir}/map.json") as f:
        facility = json.load(f)
    with open(f"log/{dir}/owner.json") as f:
        owner = json.load(f)
    with open(f"log/{dir}/player.json") as f:
        player = json.load(f)
    img = np.zeros((H*size, W*size, 3))
    mx = max(list(map(lambda x: max(x), land)))
    for h in range(1, H):
        for w in range(1, W):
            if pick == "all":
                color = (max(0, 200-land[h][w]), 255, max(0, 200-land[h][w]))
            else:
                color = (255-255*land[h][w]//mx, 255, 255-255*land[h][w]//mx)
            img[h*size:(h+1)*size, w*size:(w+1)*size] = color

    font_path = 'C:\Windows\Fonts\meiryo.ttc'
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)
    img = Image.fromarray((img).astype(np.uint8))
    draw = ImageDraw.Draw(img)
    for h in range(1, H):
        for w in range(1, W):
            if owner[h][w] != "":
                draw.text((size*w+2, size*h), f"{facility[h][w]}", font=font, fill=tuple(player[owner[h][w]]["color"]))

    img = np.array(img)
    for h in range(1, H):
        cv2.putText(img, f"{h}", (0, size*(h+1)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255))
    for w in range(1, W):
        cv2.putText(img, f"{w}", (size*w, size), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255))
    for h in range(0, H, 5):
        for w in range(W*size):
            img[(h+1)*size-1][w] = (0, 0, 0)
    for w in range(0, W, 5):
        for h in range(H*size):
            img[h][(w+1)*size-1] = (0, 0, 0)
    cv2.imwrite("log/test.png", img)
    return "log/test.png"
