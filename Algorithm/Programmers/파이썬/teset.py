from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

list4 = [i*j for i in range(1, 10) for j in range(1, 10)]



def solution2(s):
    temp = ["",s[0]]

    print(temp)
    
    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    print(temp)

    return 1 if len(temp)==1 else 0


print(solution2("aabbaa"))