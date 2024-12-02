input = open('input/input01', 'r')

#create holders
list1 = []
list2 =[]

#get input in chosen structures
for line in input.readlines():
    ints=line.strip().split()

    list1.append(int(ints[0]))
    list2.append(int(ints[1]))

list1.sort()
list2.sort()

#calculate
distsum=0

j=0
for int in list1:
    distsum+=abs(int-list2[j])
    j+=1


print("part1")
print("distsum =", distsum)

#calculate part 2
simscore=0
for int in list1:
    occs=list2.count(int)
    simscore += int*occs

print("part2")
print("simscore =", simscore)