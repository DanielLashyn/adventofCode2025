from classes.rotation import rotation
from classes.dial import dial

data_file = "input_real.txt"
print("Day 1:")
print("Using Data from " + data_file)

# Gets the raw data from the text file
with open(data_file, "r") as file:
    rawData = file.read().splitlines()


instructions = []
dial = dial()
# Converts the raw data into the rotation class
for data in rawData:
    rotationData = rotation(data)
    instructions.append(rotationData)


for rotationData in instructions:
    dial.updatePostion(rotationData)
#    rotationData.printValues()
    dial.printValues()
#    input()

dial.printValues()
