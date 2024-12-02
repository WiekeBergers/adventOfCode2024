input = open('input/input02', 'r')

def isSafe(listOFInts):
    dists=[]
    for i in range(len(listOFInts)-1):
        dists.append(listOFInts[i+1] - listOFInts[i])
    return all(x>0 and x <4 for x in dists) or all(x<0 and x>-4 for x in dists)

safes =0
problemsDampened=0
for line in input.readlines():
    line =  [int(x) for x in line.strip().split()]

    if isSafe(line):
        safes+=1
    else:
        for j in range(len(line)):
            if isSafe(line[:j]+line[j+1:]):
                problemsDampened+=1
                break
print("part1")
print("safes =", safes)

print("part2")
print("safes=", safes+problemsDampened)