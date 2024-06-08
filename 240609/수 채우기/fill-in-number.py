n = int(input())

# 그리디 알고리즘을 사용해서 5원을 최대한 사용하는 방법을 사용할 때 사용하는 동전의 수를 구한다.
# ans는 n을 5로 나는 몫으로 초기화하고 n은 초기화한 ans * 5를 한 값을 뺀다.
ans = n // 5
n -= ans * 5

# n이 0이 되지 않을때
    # n이 짝수인 경우
        # n을 2로 나눈 몫을 ans에 더한다.
    # n이 홀수인 경우
        # n에 5를 더한 후 2로 나눈 몫을 ans에 더한다.
        # 5원 동전 하나를 뺏으므로 ans에 1을 뺀다.
        # 만일 ans가 0일 경우에는 위 규칙을 따를 수 없으므로 ans = -1이 된다.
if n != 0:
    if n > 0 and n % 2 == 0:
        ans += n // 2
    elif n > 0 and n % 2 != 0:
        if ans > 0:
            ans += (n + 5) // 2 - 1
        else:
            ans = -1

print(ans)