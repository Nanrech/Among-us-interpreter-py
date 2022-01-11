from Stack import Stack
from Commands import Colours
import sys

f = open(sys.argv[1], 'r')

prg = f.read()
prg = prg.split()
f.close()
op = Colours()
#print(len(prg))
stack = Stack()
prgPos:int = 0
tempb:int = 0
brcC:int = 0
loopc:bool = False
posBSet:set = {}

while prgPos < len(prg):
    # Regular colours; need a 'SUS' after them to execute
    if prg[prgPos] == 'RED':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._red()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'BLUE':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._blue()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'PURPLE':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._purple()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'GREEN':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._green()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'YELLOW':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._yellow()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'CYAN':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._cyan()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'BLACK':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._black()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'WHITE':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._white()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'BROWN':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._brown()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'LIME':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._lime()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'PINK':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._pink()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'ORANGE':
        prgPos += 1
        if prg[prgPos] == 'SUS':
            op._orange()
            prgPos += 1
        else:
            raise ValueError('Missing a "SUS"')
        continue
    elif prg[prgPos] == 'SUS':
        raise ValueError(""""SUS"' needs to go after a colour""")
    # "Special commands"; no need for a 'SUS' after them so they get a pass
    elif prg[prgPos] == 'VENTED':
        op._vented()
        prgPos += 1
        continue
    elif prg[prgPos] == 'SUSSY':
        op._sussy()
        prgPos += 1
        continue
    elif prg[prgPos] == 'ELECTRICAL':
        op._electrical()
        prgPos += 1
        continue

    elif prg[prgPos] == "WHO" or prg[prgPos] == 'WHO?':
        if prgPos == tempb:
            prgPos += 1
        elif prgPos != tempb:
            loopc = True
            brcC = 0
            tempb = prgPos
            while prgPos > len(prg):
                if prg[prgPos] == 'WHO' or prg[prgPos] == 'WHO?':
                    brcC += 1
                    prgPos +=1
                    
                elif prg[prgPos] == 'WHERE' or prg[prgPos] == 'WHERE?':
                    brcC -= 1
                    posBSet.add(prgPos)
                    prgPos += 1
                    
                if brcC == 0:
                    prgPos = tempb
                    break
            continue
    
    elif prg[prgPos] == 'WHERE?' or prg[prgPos] == 'WHERE?':
        if loopc == False:
            if prgPos in posBSet:
                prgPos += 1
                continue
            else:
                raise ValueError('Stray where found')
        else:
            if op.acc2 == stack.get_first():
                prgPos += 1
                continue
            else:
                prgPos = tempb
                continue

    else:
        prgPos +=1
