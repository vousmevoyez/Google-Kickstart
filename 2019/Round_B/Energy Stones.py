MOD = 10**9+7
import functools

S,E,L = [],[],[]

def cmp(i,j):
    global S,E,L
    if S[i]*L[j]<S[j]*L[i]:
        return -1
    if S[i]*L[j]>S[j]*L[i]:
        return 1
    return 0

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(1, t + 1):
        n = int(raw_input())
        S, E, L = [], [], []
        for i in range(n):
            s,e,l = map(int, raw_input().split())
            S.append(s)
            E.append(e)
            L.append(l)
        rank = list(sorted(range(n),key=functools.cmp_to_key(cmp)))
        T = sum(S)
        f = [0]*(T+1)
        for i in range(n):
            for t in range(T,S[rank[i]]-1,-1):
                eatTime = t-S[rank[i]]
                energy = max(E[rank[i]]-L[rank[i]]*eatTime,0)
                if energy>0:
                    f[t] = max(f[t],f[t-S[rank[i]]]+energy)
        print("Case #{}: {}".format(_, max(f)))
