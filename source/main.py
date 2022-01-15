from Heavy import Stack, Commands

stack = Stack()
command = Commands()
COLOURS  = {'RED', 'BLUE', 'PURPLE', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', 'WHITE', 'BROWN', 'LIME', 'PINK', 'ORANGE'}
COMMANDS = {'VENTED', 'SUSSY', 'ELECTRICAL'}
with open(r'path', 'r') as f:
    TEXT = f.read()
TOKENS:list = []
temp:str = None 

for a in TEXT.split():
    if a == 'SUS' and temp in COLOURS:
        for a in COLOURS:
            if temp == a:
                TOKENS.append(f'COL_{a}')
                break

    elif a in COMMANDS:
        temp = None
        TOKENS.append(f'CMD_{a}')

    elif a in COLOURS:
        temp = a
        continue

    else: continue

