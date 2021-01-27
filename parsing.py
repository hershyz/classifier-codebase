import debuglib

# reads the file
filepath = "wab.csv"
f = open(filepath, "r")
lines = []

for x in f:
    line = x.replace("\n", "")
    lines.append(line)

# transfers split lines into data:
rawData = []

i = 1
while i < len(lines):
    l = lines[i].split(",")
    rawData.append(l)
    i+=1

print("raw data:")
debuglib.print2dArr(rawData)

# gets rid of labels and creates output data:
outputs = []
data = []

i = 0
while i < len(rawData):
    outputs.append(rawData[i][len(rawData[i]) - 1])
    
    j = 0
    arr = []
    while j < (len(rawData[i]) - 1):
        arr.append(rawData[i][j])
        j+=1
    
    data.append(arr)

    i+=1

print("")
print("outputs: ")
print(outputs)

print("")
print("data:")
debuglib.print2dArr(data)
