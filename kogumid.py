
sone = "abcdef"
loik = sone[3:5]
print(loik)

loend = [3, 5, 1, 6, 4, 7]
loend[3] = 8   # loend == [3, 5, 1, 8, 4, 7]
print(loend[2:])

hulk = {1, 2, 3, 1, 2}.union({1, 6})   # hulk == {1, 2, 3, 6}
print(hulk)

ennik = (1, 2) + (1, 4, 5)
print(ennik)
list1 = list(ennik)
print(list1)
set1 = set(ennik)
print(set1)
print(list(set1))

map1 = {1: "yks", 2: "kaks", 3: "kolm"}
for i in map1:
    print(map1[i])

print(map1)

map2 = {1: "yks", 2: "kaks"}
print(map2)
