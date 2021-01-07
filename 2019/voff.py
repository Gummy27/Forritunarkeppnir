# a-n : Sekúndur með gelti
# a-1 : Fyrsta sekúndan sem hann heyrir gelt
# a-pi : Síðasta sekúndan sem hann heyrir gelt
# k    : Sekúndur sem hundarnir anda á milli gelta
n, k = map(int, input().split())
B = sorted(map(int, input().split()))
from collections import deque, defaultdict
A = defaultdict(int)
for x in B:
    A[x] += 1
keys = sorted(A.keys())
cur = 0
mx = 0
last = deque()
for i in keys:
    cur += A[i]
    last.append(i)
    while True:
        first = last.popleft()
        if first + k > i:
            last.appendleft(first)
            break
        else:
            cur -= A[first]
    mx = max(mx, cur)
print(mx)


