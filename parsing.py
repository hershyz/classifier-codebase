filepath = "wab.csv"
f = open(filepath, "r")
lines = []

for x in f:
    line = x.replace("\n", "")
    lines.append(line)

data = []

i = 1
while i < len(lines):
    l = lines[i].split(",")
    data.append(l)
    i+=1


# Access values in first row (example):
j = 0
while j < len(data):
    k = 0
    sum = 0
    while k < len(data[j]):
        sum += float(data[j][k])
        k+=1
    print("sum of row " + str(j) +": " + str(sum))
    j+=1



'''
Traditional for loop with indexes (refactor nested while loop):
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(str(i) + ": " + colors[i])
'''
