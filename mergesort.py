import csv

def merge(list1, list2):
    mergedlist = []
    totalsize = len(list1) + len(list2)
    j = 0
    k = 0
    for i in range(totalsize):
        if(k >= len(list2)):
            mergedlist = mergedlist + list1[j:]
            return mergedlist
        if(j >= len(list1)):
            mergedlist = mergedlist + list2[k:]
            return mergedlist
        if int(list1[j]) < int(list2[k]):
            mergedlist.append(list1[j])
            j += 1
        else:
            mergedlist.append(list2[k])
            k += 1
    return mergedlist

def merge2(list1, list2):
    mergedlist = []
    totalsize = len(list1) + len(list2)
    j = 0
    k = 0
    for i in range(totalsize):
        if(k >= len(list2)):
            mergedlist = mergedlist + list1[j:]
            return mergedlist
        if(j >= len(list1)):
            mergedlist = mergedlist + list2[k:]
            return mergedlist
        if int(list1[j][0]) < int(list2[k][0]):
            mergedlist.append(list1[j])
            j += 1
        else:
            mergedlist.append(list2[k])
            k += 1
    return mergedlist

def mergeSort(integerList):
    if len(integerList) < 2:
        return integerList
    midpoint = len(integerList)//2
    list1 = mergeSort(integerList[:midpoint])
    list2 = mergeSort(integerList[midpoint:])
    return merge(list1, list2)

def mergeSortList(integerList):
    if len(integerList) < 2:
        return integerList
    midpoint = len(integerList)//2
    list1 = mergeSortList(integerList[:midpoint])
    list2 = mergeSortList(integerList[midpoint:])
    return merge2(list1, list2)

keys = []
rows = []
with open("redditSubmissions.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    for row in readCSV:
        keys.append(row[0])
        rows.append(row)
keys = mergeSort(keys)
rows = mergeSortList(rows)
print(keys)
print(rows)