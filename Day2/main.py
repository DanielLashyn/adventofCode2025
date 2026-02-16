from classes.ids import ids


idList = []
data_file = "input_example.txt"

print("Day 1:")
print("Using Data from " + data_file)

# Gets the raw data from the text file
with open(data_file, "r") as file:
    rawData = file.read().splitlines()

for data in rawData:
    idList.append(ids(data))

for ids in idList:
    ids.display(False)
