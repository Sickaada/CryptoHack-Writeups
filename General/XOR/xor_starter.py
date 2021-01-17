# type in string you want to convert to binary
string = "label"
arr1 = []
arr5 = []
for i in string:
    arr1.append(ord(i))


# converts any number with given base to binary


def convertToB(numb, base):
    arr = []
    while numb > 0:
        rem = numb % base
        arr.insert(0, rem)
        numb = numb//base

    return arr


arr2 = convertToB(13, 2)

for j in range(3):
    j += 1
    arr2.insert(0, 0)

for i in range(5):
    arr5 = arr5+arr2


arr3 = []
arr4 = []

for i in arr1:
    arr3.append(convertToB(i, 2))

for i in range(len(arr3)):
    for j in range(7):
        arr4.append(arr3[i][j] ^ arr5[j])
print(arr5)
print(arr3)
print(arr4)
