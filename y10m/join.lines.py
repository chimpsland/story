
#inputFile = 'sand.407'
inputFile = 'sand.407'
outputFile= 'sand.out'


def joinLine():
    pass


with open(inputFile) as OF:
    lines = OF.readlines()
    print(lines[0:3])


