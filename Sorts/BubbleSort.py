# bubble sort
print("BUBBLE SORT")
arr = [8,3,4,6,2]
print(f"OG ARRAY: {arr}")
counter = 1
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]= arr[j+1],arr[j]
    print(f"iteration no. {counter} : {arr}")
    counter+=1
print(arr)
print('---------------------------------------------------------')