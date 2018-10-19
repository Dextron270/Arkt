import random


def dado():
    faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    out = random.choice(faces)
    return out


def flip():
    faces = ["cara", "coroa"]
    out = random.choice(faces)
    return out
