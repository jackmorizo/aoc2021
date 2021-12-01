############################################################################
# Parse our Dataset
#   We pass the path to the Input-File and return a INT-Array with
#   The lines of the Input-File as Entries of the Array
############################################################################
def getReadings(inputFile):
    readings = []
    with open(inputFile, 'r') as f:
        readings = [int(v.strip()) for v in f.readlines()]
    return readings

############################################################################
# Count the Increases of our Data-Set
#   We pass an INT-Array and count how many times an Entry is bigger as
#   the previous entry in the INT-Array
############################################################################
def countIncreases(readings, debug=False):
    prev = None
    increases = 0
    for measurement in readings:
        if debug:
            print(measurement, end=" ")
        
        if prev is None:
            prev = measurement
            if debug:
                print("(N/A - no previous measurement)")
        elif measurement > prev:
            increases += 1
            prev = measurement
            if debug:
                print("(increased)")
        elif measurement == prev:
            if debug:
                print("(no change)")
        else:
            prev = measurement
            if debug:
                print("(decreased)")
    
    return increases

############################################################################
# Create a Sliding-Window of an INT-Array
#   https://en.wikibooks.org/wiki/Digital_Signal_Processing/Windowing
#
# P.S.: Thank you FH-Prof. DI Dr. Gerhard Jöchtl for teaching me this
#       at the University of Applied Sciences in Salzburg :D
############################################################################
def createSlidingWindow(readings, windowSize):
    window = []
    results = []
    for measurement in readings:
        # add to the window
        window.append(measurement)

        # remove the first entry of the window if it gets to big
        if len(window) > 3:
            window.pop(0)

        # sum the Window
        summed = None
        if len(window) == 3:
            summed = sum(window)

        # skip if we cannot calculate the sum
        #   window needs length of 3 !!!
        if summed is None:
            continue

        # add our Value
        results.append(summed)

    return results


# Part one
readings = getReadings('input')
# readings = getReadings('input.test')
increases = countIncreases(readings)
print("Part1: Measurement-Increases", increases)

# Part Two
windowed_readings = createSlidingWindow(readings, 3)
increases = countIncreases(windowed_readings)
print("Part2: Measurement-Increases", increases)
