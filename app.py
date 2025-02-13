#Find largest element in array

# Method 2
arr = [2, -8, 97, 12, 44]

def find_largest(arr: list) -> float:
    le = arr[0]
    for i in arr:
        if i > le:
            le = i
    return le

print("The largest element is:", find_largest(arr))