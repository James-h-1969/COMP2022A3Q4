import fileinput

def getTMCommands(line):
    tokens = line.strip().split()
    if len(line) == 0 or line[0] == ";" or len(tokens) < 5:
        return []
    else:
        return tokens[:5]

"""
Parses TM/PTM (from stdin)
- Return: list of line in the TM.
- Each line is list of strings (length 5): [stateIn, read, write, direction, stateOut]
  (as with Morphitt syntax)
"""
def parseInput():
    lines = list(fileinput.input())
    lines = map(lambda x: x.strip(), lines)
    lines = map(getTMCommands, lines)
    lines = [line for line in lines if len(line) > 0]
    return lines

