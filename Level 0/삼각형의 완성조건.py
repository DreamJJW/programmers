sides = list(map(int,  input().split()))
cnt = 0
for _ in range(max(sides) - min(sides) + 1, max(sides) + 1):
    cnt += 1
for _ in range(max(sides) + 1, max(sides) + min(sides)):
    cnt += 1

print(cnt)

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# [1,2], 1개
# [3,6], 5개
# [11, 7] 13개