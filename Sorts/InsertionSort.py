arr = [9, 5, 1, 4, 3]
counter = 1

print("INSERTION SORT")
print(f"OG ARRAY: {arr}")

# Start from the second element (index 1)
for i in range(1, len(arr)):
    key = arr[i]  # The element to be inserted
    j = i - 1

    # Shift elements of the sorted part that are greater than 'key'
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    # Place 'key' in its correct position
    arr[j + 1] = key

    print(f"iteration no. {counter} : {arr}")
    counter += 1

print(arr)

