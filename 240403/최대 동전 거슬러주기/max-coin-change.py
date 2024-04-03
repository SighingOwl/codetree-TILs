N, M = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

# 현재 동전의 합을 coin의 값만큼 이전의 값에 1을 더한 값 중 최대값을 dp[i]에 저장
dp = [0 for _ in range(M + 1)]
for i in range(M + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = max(dp[i], dp[i - coin] + 1)

print(dp[-1])