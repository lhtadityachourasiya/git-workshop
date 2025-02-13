#Find largest element in array

arr = [2, -8, 97, 12, 44]

def find_largest(arr: list) -> float:
    le = arr[0]
    for i in range(len(arr)):
        if arr[i] > le:
            le = arr[i]
    return le

print("The largest element is:", find_largest(arr))