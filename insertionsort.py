import csv

#possible optimization: use python array splicing to shift instead of doing it by element
def insertionSort(intList):
    key = 0
    i = 0
    for j in range(1, len(intList), 1):
        key = intList[j]
        i = j - 1
        while i >= 0 and int(intList[i]) > int(key):
            intList[i + 1] = intList[i]
            i = i - 1
        intList[i + 1] = key

def insertionSortList(sortList):
    key = 0
    i = 0
    for j in range(1, len(sortList), 1):
        key = sortList[j]
        i = j - 1
        while i >= 0 and int(sortList[i][0]) > int(key[0]):
            sortList[i + 1] = sortList[i]
            i = i - 1
        sortList[i + 1] = key


keys = []
rows = []
with open("redditSubmissions.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    for row in readCSV:
        keys.append(row[0])
        rows.append(row)
insertionSort(keys)
insertionSortList(rows)
print(keys)
print(rows)