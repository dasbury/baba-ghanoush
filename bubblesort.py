import csv

def bubbleSort(integerList):
    i = len(integerList) - 1
    while(i > 0):
        j = 0
        while(j < i):
            if int(integerList[j]) > int(integerList[j + 1]):
                #swap the integers if they are not correctly ordered
                temp = integerList[j]
                integerList[j] = integerList[j + 1]
                integerList[j + 1] = temp
            j += 1
        i -= 1

def bubbleSortList(sortlist):
    i = len(sortlist) - 1
    while(i > 0):
        j = 0
        while(j < i):
            if int(sortlist[j][0]) > int(sortlist[j + 1][0]):
                #swap the integers if they are not correctly ordered
                temp = sortlist[j]
                sortlist[j] = sortlist[j + 1]
                sortlist[j + 1] = temp
            j += 1
        i -= 1


keys = []
rows = []
with open("redditSubmissions.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    for row in readCSV:
        keys.append(row[0])
        rows.append(row)
bubbleSort(keys)
bubbleSortList(rows)
print(keys)
print(rows)
