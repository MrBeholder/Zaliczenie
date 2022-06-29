# list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
#
# for value in list:
#     print(value, end=" ")
# print("\n")
#
# for index, value in enumerate(list):
#     print("list[", index, "] -> ", value)
#
# string = "My text"
#
# for letter in string:
#     print(letter, end=" ")
# print("\n")
#
# for index, value in enumerate(string):
#     print("list[", index, "] -> ", value)

for value in range(10):
    print(value, end=" ")
print("\n")
for value in range(1, 5):
    print(value, end=" ")
print("\n")
for value in range(10, 101, 5):
    print(value, end=" ")
print("\n")
for value in range(10, -11, -1):
    print(value, end=" ")

print("\n\n")
i = 10
while i >= 0:
    print(i)
    i = i-1

while True:
    a = int(input("Podaj liczbę od 1 do 10:"))
    if (a >= 1) and (a <= 10):
        break
print(a)