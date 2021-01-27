import debuglib

unqiueOutputs = []

def run(inputs, outputs):
    
    # finds unique output values:
    for x in outputs:
        if not debuglib.contains(unqiueOutputs, x):
            unqiueOutputs.append(x)
    
    print("")
    print("unique outputs")
    print(unqiueOutputs)
