from Heavy import Stack, Commands

stack = Stack()
command = Commands()
temp:str = None
loop_starter:int = None
TOKENS:list = []
COLOURS  = {'RED', 'BLUE', 'PURPLE', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', 'WHITE', 'BROWN', 'LIME', 'PINK', 'ORANGE'}
COMMANDS = {'VENTED', 'SUSSY', 'ELECTRICAL'}
with open(r'C:\Users\Nan\Documents\Among-us-interpreter-py\Among-us-interpreter-py\source\_filename.sus', 'r') as f:
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
            pos += 1
            continue
        elif colour_command == 'BLUE':
            command.blue()
            pos += 1
            continue
        elif colour_command == 'PURPLE':
            command.purple()
            pos += 1
            continue
        elif colour_command == 'GREEN':
            command.green()
            pos += 1
            continue
        elif colour_command == 'YELLOW':
            command.yellow()
            pos += 1
            continue
        elif colour_command == 'CYAN':
            command.cyan()
            pos += 1
            continue
        elif colour_command == 'BLACK':
            command.black()
            pos += 1
            continue
        elif colour_command == 'WHITE':
            command.white()
            pos += 1
            continue
        elif colour_command == 'BROWN':
            command.brown()
            pos += 1
            continue
        elif colour_command == 'LIME':
            command.lime()
            pos += 1
            continue
        elif colour_command == 'PINK':
            command.pink()
            pos += 1
            continue
        elif colour_command == 'ORANGE':
            command.orange()
            pos += 1
            continue
        else:
            print(f'Unexpected error at TOKENS[{pos}] trying to execute {current}. \n\tCommand type: COL')
            exit()
    
    elif current.startswith('CMD'):
        cmd_command = current.replace('CMD_', '')
        if cmd_command == 'VENTED':
            command.vented()
            pos += 1
            continue
        elif cmd_command == 'SUSSY':
            command.sussy()
            pos += 1
            continue
        elif cmd_command == 'ELECTRICAL':
            command.electrical()
            pos += 1
            continue
        else:
            print(f'Unexpected error at TOKENS[{pos}] trying to execute {current}. \n\tCommand type: CMD')
            exit()
    
    elif current.startswith('START_'):
        loop_starter = pos
        pos += 1
        continue
    
    elif current.startswith('END_'):
        if stack.get_first() != command.acc2:
            try:
                pos = loop_starter
                continue
            except:
                if loop_starter == None:
                    print(f'Unexpected error at TOKENS[{pos}] trying to execute {current}. \n\tWho/Where loop was attempted but there was no loop opener.')
        else:
            pos += 1

    else:
        pos += 1

