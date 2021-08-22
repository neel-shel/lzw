s = input("Enter text: ")
arr = list(s)
print(arr)
p = 0
i = 1
j = 0
for j in arr:
    Dict = {int(j): arr[j]}
for p in arr:
    c = p+1
    if arr[p]+arr[c] in Dict:
        arr[p] += arr[c]
        compressDict = {i: arr[p]}
    else:
        compressDict[i] = arr[p]+arr[c]
    Dict.append(arr[p])
    i += 1
    p += 1
for x in compressDict:
    print(compressDict[x])
