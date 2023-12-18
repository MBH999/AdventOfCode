inputs = open("inputs.txt", "r")

data = inputs.read()

data_list = data.split("\n")

raw_numbers = []
stripped_numbers = []
calculation = ""

number_translations = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e",
}

modified_list = []

for item in data_list:
    for key, value in number_translations.items():
        item = item.replace(key, value)
    modified_list.append(item)

print(modified_list)

for coordinates in modified_list:
    items = list(coordinates)
    listNums = []
    for l in items:
        try:
            int(l)
            listNums.append(l)
        except ValueError:
            flag = False
    raw_numbers.append(listNums)

print(raw_numbers)

for n in raw_numbers:
    newNumber = str(n[0]) + str(n[-1])
    stripped_numbers.append(newNumber)

print(stripped_numbers)

integers = []

for n in stripped_numbers:
    nInt = int(n)
    #print(type(nInt))
    integers.append(nInt)

print(sum(integers))

inputs.close()