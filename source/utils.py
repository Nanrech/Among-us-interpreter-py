COLOURS = {"red", "blue", "purple", "green", "yellow", "cyan", "black", "white", "brown", "lime", "pink", "orange"}
COMMANDS = {"sus", "vented", "sussy", "electrical", "who", "who?", "where", "where?"}


def is_valid(token: str):
    if token.lower() in COLOURS or token.lower() in COMMANDS:
        return True
    else:
        return False


def is_colour(token: str):
    if token.lower() in COLOURS:
        return True
    else:
        return False


def is_sus(token: str):
    if token.lower() == "sus":
        return True
    else:
        return False


__all__ = ["is_valid", "is_colour", "is_sus"]
