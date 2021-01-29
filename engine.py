import debuglib

unqiueOutputs = []
mins = []
maxes = []
means = []
medians = []

def run(inputs, outputs):
    
    # finds unique output values:
    for x in outputs:
        if not debuglib.contains(unqiueOutputs, x):
            unqiueOutputs.append(x)
    
    print("")
    print("unique outputs")
    print(unqiueOutputs)

    # prints the columns of inputs out (use this code to find min and max values):
    print("")
    print("columns:")

    col = 0
    while col < len(inputs[0]):
        row = 0
        while row < len(inputs):
            print(inputs[row][col])
            row+=1
        print("\n")
        col+=1
