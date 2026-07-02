def generate_subsets(index, arr, current, result):
    result.append(current[:])  # store copy
    print("Current:",current)

    for i in range(index, len(arr)):
        current.append(arr[i])                 # include element
        generate_subsets(i + 1, arr, current, result)
        current.pop()                          # backtrack


arr = [1,2,3]
result = []

generate_subsets(0, arr, [], result)

# Print subsets
print(len(result))
