import re

def loadFile():
    allMults = []
    with open("day3/input.txt") as file:
        for l in file:
            mults = re.findall("(mul\([0-9]+,[0-9]+\))", l)
            allMults.extend(mults)
    return allMults

def loadFileWithCommands():
    allCommands = []
    with open("day3/input.txt") as file:
        for l in file:
            commands = re.findall("(?:mul\([0-9]+,[0-9]+\))|(?:do\(\))|(?:don't\(\))", l)
            allCommands.extend(commands)
    return allCommands

if __name__ == "__main__":
    print("Santa what the fuck is a regex")
    allMults = loadFile()
    total = 0
    for mult in allMults:
        left = mult.split(",")[0].split("(")[1]
        right = mult.split(",")[1].split(")")[0]
        print("Mult: " + mult + " contains left " + left + " and right " + right)
        total += int(left) * int(right)
    print("total mult: {0}".format(total))

    add = True
    totalWithCommands = 0
    allCommands = loadFileWithCommands()
    for command in allCommands:
        if command == "do()":
            print("Setting addition to on")
            add = True
            continue
        if command == "don't()":
            print("Turning addition off")
            add = False
            continue
        # not a do or don't, must be mult
        left = command.split(",")[0].split("(")[1]
        right = command.split(",")[1].split(")")[0]
        print("Mult: " + command + " contains left " + left + " and right " + right)
        if add:
            print("Add is on, adding mult")
            totalWithCommands += int(left) * int(right)
    print("total with commands: {0}".format(totalWithCommands))
        

