# a-n : Sekúndur með gelti
# a-1 : Fyrsta sekúndan sem hann heyrir gelt
# a-pi : Síðasta sekúndan sem hann heyrir gelt
# k    : Sekúndur sem hundarnir anda á milli gelta
from collections import deque

n, k = map(int, input().split(" "))
A = deque((map(int, input().split(" "))))

teljari = 0
while(sum(A)):
    anda = 0
    for i in range(0, len(A)):
        if(anda <= A[i] and A[i]):
            anda = A[i] + k
            A[i] = 0 
    teljari += 1
print(teljari)