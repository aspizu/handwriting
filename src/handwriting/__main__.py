from __future__ import annotations

import PIL.Image
import PIL.ImageFilter
from PIL.Image import Image

chars: dict[str, Image] = {}
for char in " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
    chars[char] = PIL.Image.open(f"chars/{char}.png")


image = PIL.Image.new("RGB", (3000, 3000), "white")


text = """
I made a python script to write   
text with my handwriting This took 
way too long to make but i think it
looks alright I could try some post
processing to make it look better
"""[1:-1]

x = 0
y = 0
for char in text:
    if char not in chars:
        char = " "
    charim = chars[char]
    if (x + charim.width) >= image.width:
        y += charim.height
        x = 0
    image.paste(charim, (x, y))
    x += charim.width


def pf(x: int) -> float:
    return x * 1.1


image = image.point(pf)
image = image.resize((image.width // 4, image.height // 4))
image.save("output.png")
