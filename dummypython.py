
topFiveList = []
topReadingSession = open("dummytopPlayers.txt", "r")
for eachLine in topReadingSession.readlines():
    score = eachLine[0:9].rstrip()
    name = eachLine[10:40].rstrip()
    topFiveList.append([score, name])

topFiveList.sort(key=lambda x: (int(x[0]), x[1]))
print(topFiveList)
topReadingSession.close()

topFiveList.pop(0)
print(topFiveList)

for eachLine in topFiveList:
    [score, name] = eachLine
    newScore = str(score) + extraspace
    newScore = newScore[0:9]
    newName = name + extraspace
    newName = newName[0:25]
    eachLine = [newScore, newName]
    fiveOutList.append(eachLine)

with open("dummytopPlayers.txt", mode="w") as sendingOut:
    for sublist in fiveOutList:
        sendingOut.write("".join(sublist) + "\n")

sendingOut.closed
