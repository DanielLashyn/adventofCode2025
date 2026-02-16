from classes.ids import ids


idList = []
data_file = "input_real.txt"

print("Day 1:")
print("Using Data from " + data_file)

# Gets the raw data from the text file
with open(data_file, "r") as file:
    rawData = file.readline().rstrip("\n")
    rawData = rawData.split(',')

idList = [ids(data) for data in rawData]
total = sum(ids.sumIDs() for ids in idList)

print("Total valid IDS: "+ str(total))
