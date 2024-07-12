# Create and initialize an array
N = int(input(
    "Enter the number of elements: "
))
array = [0] * N
for i in range(N):
    array[i] = int(input(
        "Enter element {0}: "
        .format(i+1)
    ))
# Remove duplicate elements
for i in range(N):
    for j in range(i+1, N):
        if array[i] == array[j]:
            for k in range(j, N-1):
                array[k] = array[k + 1]
            N -= 1
            j -= 1
# Display the array without duplicates
for i in range(N):
    print(array[i])
    





