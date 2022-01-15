from Heavy import Stack, Commands

stack = Stack()
command = Commands()
temp:str = None
TOKENS:list = []
COLOURS  = {'RED', 'BLUE', 'PURPLE', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', 'WHITE', 'BROWN', 'LIME', 'PINK', 'ORANGE'}
COMMANDS = {'VENTED', 'SUSSY', 'ELECTRICAL'}
with open(fileaaa, 'r') as f:
    TEXT = f.read()

for a in TEXT.split():
    if a == 'SUS' and temp in COLOURS:
        for a in COLOURS:
            if temp == a:
                TOKENS.append(f'COL_{a}')
                break

    elif a in COMMANDS:
        temp = None
        TOKENS.append(f'CMD_{a}')
    
    elif a in 'WHO?':
        temp = None
        TOKENS.append('START_WHO')
    
    elif a in 'WHERE?':
        temp = None
        TOKENS.append('END_WHERE')

    elif a in COLOURS:
        temp = a
        continue

    else: continue
pos:int = 0

while pos < len(TOKENS):
    current = str(TOKENS[pos])
    if current.startswith('COL'):
        colour_command = current.replace('COL_', '')
        if colour_command == 'RED':
            command.red()
            continue
        elif colour_command == 'BLUE':
            command.blue()
            continue
        elif colour_command == 'PURPLE':
            command.purple()
            continue
        elif colour_command == 'GREEN':
            command.green()
            continue
        elif colour_command == 'YELLOW':
            command.yellow()
            continue
        elif colour_command == 'CYAN':
            command.cyan()
            continue
        elif colour_command == 'BLACK':
            command.black()
            continue
        elif colour_command == 'WHITE':
            command.white()
            continue
        elif colour_command == 'BROWN':
            command.brown()
            continue
        elif colour_command == 'LIME':
            command.lime()
            continue
        elif colour_command == 'PINK':
            command.pink()
            continue
        elif colour_command == 'ORANGE':
            command.orange()
            continue
        else:
            print(f'Unexpected error at TOKENS[{pos}] trying to execute {current}. \n\tCommand type: COL')
            exit()
    
    elif current.startswith('CMD'):
        cmd_command = current.replace('CMD_', '')
        if cmd_command == 'VENTED':
            command.vented()
            continue
        elif cmd_command == 'SUSSY':
            command.sussy()
            continue
        elif cmd_command == 'ELECTRICAL':
            command.electrical()
            continue
        else:
            print(f'Unexpected error at TOKENS[{pos}] trying to execute {current}. \n\tCommand type: CMD')
            exit()
    
    elif current.startswith('START_'):
        loop_starter = pos
        continue

    pos += 1
