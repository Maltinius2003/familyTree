import json
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open("test.txt", "w") as fp:
    json.dump(l, fp)

with open("test.txt", "r") as fp:
    b = json.load(fp)

print(b)
