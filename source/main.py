import sys

from classes import TheSkeld

COLOURS = {"red", "blue", "purple", "green", "yellow", "cyan", "black", "white", "brown", "lime", "pink", "orange"}
COMMANDS = {"sus", "vented", "sussy", "electrical", "who", "who?", "where", "where?"}

if __name__ == "__main__":
    skeld: TheSkeld = TheSkeld()
    file: str = sys.argv[-1]
    tokens: list = []

    print(f"{file}\n")

    if not file or not file.endswith(".sus"):
        raise SyntaxError("Expected file path to a valid .sus file")

    # open file
    with open(file, 'r') as f:
        file = f.read()

    # parse & crunch into tokens
    temp: str = ""
    for t in file.split():
        t = t.lower()

        if not (t in COLOURS or t in COMMANDS):
            raise SyntaxError(f"Invalid token: '{t}'")

        if t.lower() == "sus":
            if temp in COLOURS:
                tokens.append(temp.lower())
                continue
        else:
            temp = t
            if t in COLOURS:
                continue

            if '?' in t:
                tokens.append(t.replace('?', ""))
            else:
                tokens.append(t)

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

    input("\nPress enter to close...")
