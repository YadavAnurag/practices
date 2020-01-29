def seive():
    high = 10**7
    primes = [False for i in range(high+1)]

    p = 2
    while p*p<high:
        if primes[p] == False:
            for i in range(p*p, high+1, p):
                primes[i] = True
        p += 1

    return primes

def solve():
    primes = seive()
    for idx,prime in enumerate(primes[1:]):
        if idx == 0: continue
        try:
            if primes[idx]==True and primes[idx+n] == True:
                return idx+n,idx
        except IndexError as IE:
            print('No solutions', IE)
            return 0,0
    a,b = 0,0
    return a,b

n = int(input())

#either use these two lines but will work upto 10**7
# a,b = solve()
# print(a,b)
# or use below god line
print(9*n, 8*n)






