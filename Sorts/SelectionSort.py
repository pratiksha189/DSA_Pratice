# SELECTION SORT
print("SELECTION SORT")
arr = [29, 10, 14, 37, 13]
print(f"OG ARRAY: {arr}")
counter = 1
for i in range(len(arr)):
    minm = i
    for j in range(i+1,len(arr)):
        if arr[minm]>arr[j]:
            minm = j
    arr[minm],arr[i]=arr[i],arr[minm]
    print(f"iteration no: {counter}: {arr}")
    counter+=1
print(arr)
print('---------------------------------------------------------')