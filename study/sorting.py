def score_sort(arr):
    n = len(arr)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if arr[cur - 1][1] > arr[cur][1]:
                arr[cur - 1], arr[cur] = arr[cur], arr[cur - 1]
    return arr


score = [
    ["우제", 88],
    ["상혁", 99],
    ["지훈", 70],
    ["민형", 79],
    ["민석", 61],
    ["현준", 94],
]

print("정렬 전 -->", score)
score = score_sort(score)
print("정렬 후 -->", score)

print(" * 성적별 조 편성표 * ")
for i in range(len(score) // 2):
    print(score[i][0], ":", score[len(score) - 1 - i][0])
