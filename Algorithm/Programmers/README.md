# 프로그래머스

1. 프로그래머스 문제를 Level 1부터 Level 3까지 자바로 풀어보고 문제 정리

2. 이전에 C++로 풀었는데 자바에 익숙해지기 위해 자바로 풀기..

3. 자료구조를 사용하는 방법에 중점을 두기

4. https://coding-factory.tistory.com/602

5. https://bestalign.github.io/2015/08/31/top-10-mistakes-java-developers-make-1/

# 다시 풀어볼 문제

1. 단체사진 찍기, 카카오프렌즈, 튜플, 행렬 테두리, 순위검색**, 다리를 지나는 트럭**, 배달**(다익스트라 알고리즘), 메뉴리뉴얼**(combination)

2. 가장 큰 정사각형 (DP) **

3. [3차] 파일명 정렬 (정렬하는 방법) **

4. 

# 순열 (Level - 2 소수찾기, 단체사진 찍기)

// 1~n자리 순열

permutation("", "123");

void permutation(String prefix, String str) {
    
    int n = str.length();

    if(!prefix.equals("")) System.out.println(Integer.valueOf(str));
    for (int i=0; i<n; i++) {
        permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
    }

}

// n자리만 순열

void permutation(String prefix, String str) {
    int n = str.length();

    if(n == 0) System.out.println(Integer.valueOf(str));
    for(int i=0; i<n; i++) {
        permutation(prefix + str.charAt(i), str.substring(0,i) + str.substring(i+1,n));
    }
}

# HashMap Value 정렬

```
HashMap<String, Integer> hashMap = new HashMap<>();

hashMap.put("사과",1);
hashMap.put("배",3);
hashMap.put("오렌지",5);
hashMap.put("귤",4);

ArrayList<String> sortList = new ArrayList<>(hashMap.keySet());

//앞에가 크면 앞이랑 뒤랑 바꿔 -> 점점 작아짐 -> 내림차순
Collections.sort(sortList, (o1, o2) -> hashMap.get(o1).compareTo(hashMap.get(o2)));

//뒤에가 크면 바꿔 앞이랑 뒤랑 바꿔 -> 점점 커짐 -> 오름차순
Collections.sort(sortList, (o1, o2) -> hashMap.get(o2).compareTo(hashMap.get(o1)));

for(String key : sortList) {
    System.out.println("key" + key + "value" + hashMap.get(key));
}

엄밀히 말하면 hashMap 자체를 정렬시키는 것은 아니지만 정렬된 데이터를 가져올 수 있다.

```

# GCD, LCM

```



```

# 에라토스테네스의 체

```

boolean[] prime = new boolean[n+1];

for (int i = 2; i*i<=n ; i++) {
    if(!prime[i]) {
        for(int j = i*i; j <= n; j+=i) {
            prime[j] = true;
        }
    }
}

for (int i = 2 ; i<=n ;i++) {
    if(!prime[i]) {
        answer++;
    }
}

```


# BFS 인접 행렬 (큐)

```

Queue<Integer> queue = new LinkedList();

visited[1] = true;

queue.offer(1);

while(!queue.isEmpty()) {

    int x = queue.poll();

    System.out.println(x);

    for (int i=0; i<= N; i++) {

        if(graph[x][i] == 1 && !visited[i]) {
            
            visited[i] = true;
            
            queue.offer(i);

        }

    }

}

```

# BFS 인접 리스트 (큐)

```

Queue<Integer> queue = new LinkedList();

visited[1] = true;

queue.offer(1);

while(!queue.isEmpty()) {

    int x = queue.poll();

    System.out.println(x);

    for (int i=0; i<=N; i++) {

        int y = graph[x][i];

        if(!visited[y]) {
            
            visited[y] = true;

            queue.offer(y);

        }
    }

}

```

# DFS 인접 행렬 (재귀)

```

void dfs(int x) {
        
    visited[x] = true;
    
    System.out.println(x);
    
    for (int i=0; i<= N; i++) {
        
        if(graph[x][i] == 1 && !visited[i]) {
            dfs(i);
        }
        
    }
}

```

# DFS 인접 리스트 (재귀)

```

void dfs(int x) {
    
    visited[x] = true;

    System.out.println(x);

    for (int i=0; i<= N; i++) {
        
        int y = graph[x][i];

        if(!visited[y]) {
            dfs(y);
        }

    }

}

```

# 최하위비트 구하기

```

1의 최하위 비트는 A & ( -A )

왜 이게 최하위 비트를 구하는지 예시로 살펴보면, let, A = 101100 이라 하면, -A(A의 2의 보수) = 010100이고 이를 & 연산하면 000100 이다.

2의 보수가 A를 Not한 다음 + 1을 한 결과이므로 최하위 비트를 알 수 있다.

0의 최하위 비트는 ~A & A

10001111이라고 하면 0의 최하위비트의 위치는 

00010000 해당 숫자를 구하는 방법이 lastBit

long lastBit = ~number & (number + 1); 

number = (number | lastBit) & ~(lastBit >> 1);

lastBit와 number를 or연산하면 10011111 

에서 lastBit를 한칸 오른쪽으로 민건 00001000 해당 1을 반대로 뒤집으면 0111이랑 10011111 & 연산하면

10010111
        

```