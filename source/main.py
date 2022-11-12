import sys

from classes import TheSkeld
from utils import *


if __name__ == "__main__":
    skeld: TheSkeld = TheSkeld()
    file: str = sys.argv[-1]
    tokens: list = []

    print(file)

    if not file:
        raise SyntaxError("Expected file path")

    # open file
    with open(file, 'r') as f:
        file = f.read()

    # parse & crunch into tokens
    temp: str = ""
    for t in file.split():
        if not is_valid(t):
            raise SyntaxError(f"Invalid token: '{t}'")

        if is_sus(t) and is_colour(temp):
            tokens.append(t.lower())
        else:
            if '?' in t:
                tokens.append(t.replace('?', "").lower())
                continue
            tokens.append(t.lower())

    # do the tokens
    # this first pass just checks for unclosed loops
    i = 0
    # 8 morbillion iq move re-using the i = 0 for the interpreter

    for t in tokens:
        if t == "who":
            i += 1
        elif t == "where":
            i -= 1

    if i != 0:
        raise SyntaxError("Invalid syntax: unclosed who/where in file")

    # And so begins the interpreter
    # I didn't make it check for overflow/underflow bc lazy and the thingy right
    # above should've taken care of that already
    while i < len(tokens):
        if tokens[i] == "who":
            skeld.call_stack.push(i)

        elif tokens[i] == "where":
            if skeld.acc2 != skeld.stack.first:
                i = skeld.call_stack.first
                continue
            else:
                skeld.call_stack.pop()
        else:
            skeld.interpret(tokens[i])
        i += 1

    input("Press any key to close...")
