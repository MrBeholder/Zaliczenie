import math

class Vector:
    def __init__(self, xA, yA, xB, yB):
        self.xA, self.yA = xA, yA
        self.xB, self.yB = xB, yB
    def printVector(self):
        print("[", self.xB - self.xA, ",", self.yB - self.yA, "]")
    def lenVector(self):
        return math.sqrt(pow(self.xB-self.xA,2)+pow(self.yB-self.yA,2))

# vectorAB = Vector(5,2,1,2)
# vectorAB.printVector()
# print("Długość wektora: ", vectorAB.lenVector())

file = open("vectors.txt", "r")
pointList = file.read().split("\n")
vectorList = []
for i in pointList:
    points = i.split(" ")
    points = list(map(int, points))
    vectorList.append(Vector(points[0], points[2], points[1], points[3]))

for i in vectorList:
    i.printVector()
    print("Długość wektora: ", i.lenVector())