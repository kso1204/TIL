# K진수에서 소수 개수 구하기

# 문제 설명

# 해결 방안

1. K진수로 변환

3. 숫자 쪼개기

2. 소수인지 판별

# 풀이

```

def solution(n, k):
    answer = 0
    temp = ""
    
    while n > 0:
        n, mod = divmod(n, k)
        temp += str(mod)
        
    temp = temp[::-1]
    
    list = temp.split('0')
    
    for l in list:
        if  l and isPrime(int(l)) :
            answer += 1
    
    
    return answer

def isPrime(v):
    if v <= 1: return False
    for i in range(2, int(v ** 0.5)+1):
        if v % i == 0:
            return False
    return True

```


```

import math
def solution(n, k):
    answer = 0
    temp = ""
    
    while n > 0:
        n, mod = divmod(n, k)
        temp += str(mod)
        
    temp = temp[::-1]
    
    list = temp.split('0')
    
    for l in list:
        if  l.isdigit() and isPrime(int(l)) :
            answer += 1
    
    
    return answer

def isPrime(v):
    if v <= 1: return False
    for i in range(2, int(math.sqrt(v) + 1)):
        if v % i == 0:
            return False
    return True

```

```

def jinsu(n, k) :
    jinsu = ''
    while n > 0 :
        n, mod = divmod(n, k)
        jinsu += str(mod)
    return jinsu[::-1]

def isprime(i) :
    if i == 1:
        return False
    elif i == 2 :
        return True
    for n in range(2, i) :
        if i%n == 0 :
            return False
    return True

def solution(n, k) :
    clu = jinsu(n, k).split('0')
    prime = []
    for c in clu :
        if c.isdigit() and isprime(int(c)) :
            prime.append(int(c))
    return len(prime)

```

```

import re
def solution(n, k):
    answer = 0
    temp = ""
    
    while n:
        temp = str(n%k) + temp
        n = n // k
        
    p = re.compile("[0]+[1-9]+[0]+")
    result = p.findall(temp)
    
    p1 = re.compile("^[1-9]+[0]+")
    result.extend(p1.findall(temp))
    
    p2 = re.compile("[0]+[1-9]+$")
    result.extend(p2.findall(temp))
    
    p3 = temp.replace("0", "")
    
    if len(p3) == len(temp):
        result.extend(p3)
    
    list = []
    
    for r in result:
        list.append(r.replace("0", ""))
    
    
    for l in list:
        if isPrime(l):
            answer += 1
    
    
    return answer

def isPrime(val):
    v = int(val)
    if v <= 1: return False
    for i in range(2, v):
        if v % i == 0:
            return False
    return True
    

```