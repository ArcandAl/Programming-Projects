import csv
dict = {}

with open("inventory.csv", "r") as data:
    for line in csv.reader(data):
        dict[line[0]] = line[1]
data.close()
print(dict)
print()
print("Press x anytime to quit \n")

while True:
    key = input("Enter item name: ")
    if key.lower() == "x":
        break
    value = input("Enter amount of item: ")
    if value.lower() == "x":
        break

    dict[key] = value
    print()

file = open("inventory.csv", "w", newline="")
writer = csv.writer(file)
for i, j in dict.items():
    writer.writerow([i, j])
file.close()
