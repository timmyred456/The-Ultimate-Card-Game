import time

def WriteLine(Line,Speed,MobTalking=False,MobName="Nil"):
    SplitLines = list(Line)

    if(MobTalking == True):
        print("{"+str(MobName) + '}: "', end='')
        SplitLines.append('"')
        SplitLines.append("\n")
    else:
        SplitLines.append("\n")

    for x in range(len(SplitLines)):
        if SplitLines[x] == ",":
            print(SplitLines[x], end='')
            time.sleep(Speed + 0.3)
        elif SplitLines[x] == ":":
            print(SplitLines[x], end='')
            time.sleep(Speed + 0.15)
        elif SplitLines[x] == "." or SplitLines[x] == "!":
            print(SplitLines[x], end='')
            time.sleep(Speed + 0.7)
        else:
            time.sleep(Speed)
            print(SplitLines[x], end='')
