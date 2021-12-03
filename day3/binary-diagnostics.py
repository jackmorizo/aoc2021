import pandas as pd

############################################################################
# Parse our Dataset
#   We pass the path to the Input-File and return a INT-Array with
#   The lines of the Input-File as Entries of the Array
############################################################################
def getReadings(inputFile):
    readings = []
    with open(inputFile, 'r') as f:
        for r in [v.strip() for v in f.readlines()]:
            readings.append(list(r))
    return pd.DataFrame(readings).astype(int)


############################################################################
# Parse Gamma and Epsilon Values out of the Readings
#   gamma: most common bit on every position
#   epsilon: inverse of gamma
############################################################################
def getGammaEpsilon(readings):
    return {
        'gamma': int("".join([str(b) for b in readings.mode().values.tolist()[0]]), 2),
        'epsilon': int("".join(["0" if b == 1 else "1" for b in readings.mode().values.tolist()[0]]), 2)
    }

############################################################################
# Parse Gamma and Epsilon Values out of the Readings
#   gamma: most common bit on every position
#   epsilon: inverse of gamma
############################################################################
def getOxigenGeneratorRating( readings):
    df = readings
    for col in df.columns:
        if( len(df) == 1):
            break
        df = df.loc[df[col] == int(df.mode().max()[col]), :].reset_index(drop=True)
    return int( "".join([str(b) for b in df.values.tolist()[0]]), 2)


def getCOGeneratorRating( readings):
    df = readings
    for col in df.columns:
        if( len(df) == 1):
            break
        df = df.loc[df[col] != int(df.mode().max()[col]), :].reset_index(drop=True)
    return int( "".join([str(b) for b in df.values.tolist()[0]]), 2)

# readings = getReadings('input.test')
readings = getReadings('input')


#part one
rates = getGammaEpsilon(readings)
print("Part1: Gamma and Epsilon Rates are ", rates)
print("Solution ", rates['gamma'] * rates['epsilon'])


#part two
oxigen = getOxigenGeneratorRating(readings)
co = getCOGeneratorRating(readings)
print("Part1: Oxigen and CO2 Rates are ", (oxigen,co))
print("Solution ", oxigen * co)
