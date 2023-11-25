import cv2
import numpy as np

from globals import *

def create_map_image(land, facility):
    with open(f"log/owner.json") as f:
        owner = json.load(f)
    with open(f"log/player.json") as f:
        player = json.load(f)
    img = np.zeros((H*size, W*size, 3))
    for h in range(1, H):
        for w in range(1, W):
            color = (max(0, 200-land[h][w]), 255, max(0, 200-land[h][w]))
            for i in range(size):
                for j in range(size):
                    img[h*size+i][w*size+j] = color
    for h in range(1, H):
        for w in range(1, W):
            if owner[h][w] != "":
                cv2.putText(img, f"{facility[h][w]}", (size*w+2, size*(h+1)-2), cv2.FONT_HERSHEY_DUPLEX, 0.5, player[owner[h][w]]["color"])

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
