from commands import rchoice
from commands.vocab import Vocab


def run(arg):
    if arg in Vocab.dado():
        out = rchoice.dado()

    if arg in Vocab.flip():
        out = rchoice.flip()

    return out