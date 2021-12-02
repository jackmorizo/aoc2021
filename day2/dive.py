############################################################################
# Parse our Dataset
#   We pass the path to the Input-File and return a INT-Array with
#   The lines of the Input-File as Entries of the Array
############################################################################
def getReadings(inputFile):
    readings = []
    with open(inputFile, 'r') as f:
        for r in [v.strip().split(' ') for v in f.readlines()]:
            readings.append({
                'direction': r[0],
                'value': int(r[1])
            })
    return readings

############################################################################
# Calculation for Part 1
############################################################################
def calculateFinalPosition(readungs, debug=False):
    pos = {'x': 0, 'y': 0}
    for r in readings:
        if debug:
            print("reading:", r, end=" ")

        if r['direction'] == 'forward':
            pos['x'] += r['value']
        elif r['direction'] == 'up':
            pos['y'] -= r['value']
        elif r['direction'] == 'down':
            pos['y'] += r['value']

        if debug:
            print("position:", pos)

    return pos

############################################################################
# Calculation for Part 2
############################################################################
def calculateFinalPositionWithAim(readungs, debug=False):
    pos = {'x': 0, 'y': 0, 'aim': 0}
    for r in readings:
        if debug:
            print(r['direction'], r['value'], end=" ")

        if r['direction'] == 'forward':
            pos['x'] += r['value']
            pos['y'] += r['value']*pos['aim']
        elif r['direction'] == 'up':
            pos['aim'] -= r['value']
        elif r['direction'] == 'down':
            pos['aim'] += r['value']

        if debug:
            print("position:", pos)

    return pos


# readings = getReadings('input.test')
readings = getReadings('input')

# Part one
pos = calculateFinalPosition(readings, False)
print("Part1: Your final Position is ", pos)
print("Solution ", pos['x'] * pos['y'])


# Part Two
# readings = getReadings('input.test')
pos = calculateFinalPositionWithAim(readings)
print("Part2: Your final Position is ", pos)
print("Solution ", pos['x'] * pos['y'])
