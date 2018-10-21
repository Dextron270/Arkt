from commands import rchoice
from commands.vocab import Vocab


def run(arg):
    if arg in Vocab.dice():
        out = rchoice.dice()

    if arg in Vocab.flip():
        out = rchoice.flip()

    return out
