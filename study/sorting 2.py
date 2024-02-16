def select_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp
    return arr


arr1 = [[55, 33, 250, 44], [88, 1, 76, 23], [199, 222, 38, 47], [155, 145, 20, 99]]

arr2 = []

for i in range(len(arr1)):
    for j in range(len(arr1)):
        arr2.append(arr1[i][j])

arr2 = select_sort(arr2)
print("정렬 후 --> ", arr2)
print("중앙값 : ", arr2[len(arr2) // 2])
