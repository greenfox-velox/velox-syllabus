import csv
from prettytable import PrettyTable

lottery_file = open("otos.csv")
lottery_reader = csv.reader(lottery_file, delimiter = ";")

history = []
for row in lottery_reader:
    drawn = row[-5:]
    drawn_numbers = []
    for elem in drawn:
        drawn_numbers.append(int(elem))

    history.append(drawn_numbers)

frequency = {}

for draw in history:
    for number in draw:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1


table = PrettyTable(["number", "frequency"])
for key in frequency:
    table.add_row([key, frequency[key]])

print(table.get_string(sortby="frequency", reversesort=True))
