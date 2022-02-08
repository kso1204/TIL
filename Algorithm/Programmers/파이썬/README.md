# 신고 결과 받기

```

answer = [0] * len(id_list)

리스트를 0으로 초기화 하는 방법

reports = {x : 0 for x in id_list}

딕셔너리를 0으로 초기화 하는 방법

answer[id_list.index(r.split()[0])] += 1

++은 사용이 되지 않는 것 같았는데 += 1은 작동됨

r.split()[0]

스플릿하면서 특정 값 바로 사용하기

list.index로 해당 위치 찾기

```

# K진수에서 소수 개수 구하기

```

while n > 0:
    temp = str(n%k) + temp
    n = n // k

while n:
    temp += str(n%k)
    n //= k

temp[::-1] // reverse

while n:
    n, mod = divmod(n, k)
    temp += str(mod)

temp[::-1]


isPrime(val)

if val < 2:
    return False

for i in range(2, int(val ** 0.5) + 1):
    if val % i == 0:
        return False

return True


소수 판별하는 조건문

for i in range(2, int(math.sqrt(val)+1)):

리스트 내부에 숫자인지 판별하는 조건문

l.isdigit() 

l 

```

# DFS OR BFS

```


from collections import deque
def bfs(graph, start_node):
    visited = []
    need_visited = deque()

    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited

def dfs(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    
    return visited

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))


```