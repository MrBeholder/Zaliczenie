setA = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}
setB = {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576}

print("Suma", setA.union(setB))
print(sorted(setA | setB))
print("Iloczyn", setA.intersection(setB))
print(sorted(setA & setB))
print("Różnica 1:", setA.difference(setB))
print("Różnica 2:", setB.difference(setA))