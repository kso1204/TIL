# 프로그래머스

1. 프로그래머스 문제를 Level 1부터 Level 3까지 자바로 풀어보고 문제 정리

2. 이전에 C++로 풀었는데 자바에 익숙해지기 위해 자바로 풀기..

3. 자료구조를 사용하는 방법에 중점을 두기

4. https://coding-factory.tistory.com/602

5. https://bestalign.github.io/2015/08/31/top-10-mistakes-java-developers-make-1/

6. 뒤에 페이지가 더 쉬우니까 3레벨 부터는 뒤부터 풀기

7. https://buddev.tistory.com/21 <-- 크루스칼 VS 다익스트라

# 베스트 문제

1. 순위검색

2. 메뉴리뉴얼


# 다시 풀어볼 문제

1. 단체사진 찍기, 카카오프렌즈, 튜플, 행렬 테두리, 순위검색**, 다리를 지나는 트럭**, 배달**(다익스트라 알고리즘), 메뉴리뉴얼**(combination)

2. 가장 큰 정사각형 (DP) \*\*

3. [3차] 파일명 정렬 (정렬하는 방법) \*\*

4. N-Queen (BackTracking) \*\*

5. 하노이탑 \*\*

6. 멀리뛰기 (DP) => dp[i] = dp[i-1] + dp[i-2];

7. 스티커 모으기 (DP) => 두 개의 DP 사용 DP1, DP2

8. 거스름돈 (DP) => 2차원 배열 DP DP[i][j];

9. 스타 수열 => map value 정렬

10. 풍선 터트리기 => 양쪽의 index를 가져가면서 대소를 비교하는 방법

11. 매칭 점수 \*\* => 정규식

12. 블록 이동하기 \*\* => BFS + Vertical + Time

13. 카드 짝 맞추기 \*\*\* => BFS + 순열

14. 외벽 점검 \*\*\* => 완전탐색 + 순열 + 원형배열 만들기

15. 110 옮기기 \*\* => Stack + StringBuffer Index 선형 시간으로 해결되지 않는 문제

16. 광고 삽입 ** => 부분합 + 선형탐색

17. 징검다리 건너기 ** => 이분탐색

18. 길찾기 게임 ** => Node Connect + Priority Queue => 트리를 만든다면?

19. 섬 연결하기 ** => 크루스칼 알고리즘 => 최단 거리

20. 합승 택시 요금 ** => 다익스트라 알고리즘 => 서로 통행 가능하도록 만들 때 필요한 최소 비용 

21. 불량 사용자 ***** => HashSet에 HashSet을 삽입하여 새로운 형태로 dfs를 구축하였다.

22. 보석 쇼핑 *** => 리스트에 등장하는 최대n개의 가짓수를 다 포함하기 위한 최소 길이를 구하는 문제인데.. 이 문제를 queue와 hashMap, hashSet을 이용해 잘 풀어야 한다. 

23. 브라이언의 고민 ***

24. 표 편집 ***

# 순열 (Level - 2 소수찾기, 단체사진 찍기)

```

// 1~n자리 순열

permutation("", "123");

void permutation(String prefix, String str) {

    int n = str.length();

    if(!prefix.equals("")) System.out.println(Integer.valueOf(prefix));
    for (int i=0; i<n; i++) {
        permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
    }

}

// n자리만 순열

void permutation(String prefix, String str) {
    int n = str.length();

    if(n == 0) System.out.println(Integer.valueOf(prefix));
    for(int i=0; i<n; i++) {
        permutation(prefix + str.charAt(i), str.substring(0,i) + str.substring(i+1,n));
    }
}


```

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

# Entry를 사용한 Map Value 정렬 오름차순

```

List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(hashMap.entrySet());
entryList.sort((o1, o2) -> hashMap.get(o1.getKey()) - hashMap.get(o2.getKey()));

for(Map.Entry<Integer, Integer> entry : entryList) {
    System.out.println("key" + entry.getKey() +", value : "+ entry.getValue());

}
```

# Enrty를 사용한 Map Value 정렬 내림차순

```

List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(hashMap.entrySet());
entryList.sort((o1, o2) -> hashMap.get(o2.getKey()) - hashMap.get(o1.getKey()));

for(Map.Entry<Integer, Integer> entry : entryList) {
    System.out.println("key" + entry.getKey() +", value : "+ entry.getValue());
}

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

void dfs(int vertex)
    {
        visited[vertex] = true;

        for (int edge : graph[vertex]) {
            if (!visited[edge]) {
                dfs(edge);
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

# 2진수 비트의 1의 개수 세기

```

- Integer.bitCount(n);

```

# Rotate

```

n;
int[][] rotate;
int[] weak;

public void setRotate() {
    int len = weak.length;
    rotate = new int[len][len];

    for (int i=0; i<len; i++) {
        rotate[i] = rotate(weak, i);
    }
}

public int[] rotate(int[] weak, int idx)
{
    int len = weak.length;
    int[] result = new int[len];
    for (int i=0; i<len; i++) {
        if (i+idx<len) {
            result[i] = weak[i+idx];
        } else {
            result[i] = weak[i+idx-len] + n;
        }
    }
    return result;
}

```

# Edge 그래프

```


class Edge
{

    int vertex;
    int distance;

    Edge (int vertex, int distance)
    {
        this.vertex = vertex;
        this.distance = distance;
    }

}

ArrayList<Edge> graph[];

for(int i=0; i<=N; i++){
    graph[i] = new ArrayList<>();
}

for (int i=0; i<road.length; i++) {

    graph[road[i][0]].add(new Edge(road[i][1], road[i][2]));
    graph[road[i][1]].add(new Edge(road[i][0], road[i][2]));

}


```

# 시간차 구하기

```

import java.time.*;

public int getTime(String a, String b)
{
    String[] start = a.split(":");
    String[] end = b.split(":");
    
    LocalTime startTime = LocalTime.of(Integer.valueOf(start[0]),Integer.valueOf(start[1]));  // LocalTime.of("시", "분");
    LocalTime endTime = LocalTime.of(Integer.valueOf(end[0]),Integer.valueOf(end[1]));
    
    Duration duration = Duration.between(startTime, endTime);
    
    return (int) (duration.getSeconds() / 60);
    
}


```


# 부분합 구하기

```

subSum[startIndex]++;
subSum[lastIndex]--;

for (int i = 1; i<subSum.length; i++) {
    subSum[i] += subSum[i - 1];
}

for (int i = 1; i<subSum.length; i++) {
    subSum[i] += subSum[i - 1];
}


```

# 다익스트라 알고리즘

```

import java.util.*;

class Solution {
    
    class Edge implements Comparable<Edge>{
        int vertex;
        int distance;
        
        Edge (int vertex, int distance)
        {
            this.vertex = vertex;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Edge edge)
        {
            return this.distance - edge.distance;
        }
    }
    
    boolean[] visited;
    int[] distance;
    
    public int solution(int n, int[][] costs) {
        
        int answer = 0;
        
        ArrayList<Edge> graph[] = new ArrayList[n+1];
        visited = new boolean[n+1];
        distance = new int[n+1];
        
        Arrays.fill(distance, Integer.MAX_VALUE);
        
        for (int i=0; i<n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i=0; i<costs.length; i++) {
            graph[costs[i][0]].add(new Edge(costs[i][1], costs[i][2]));
            graph[costs[i][1]].add(new Edge(costs[i][0], costs[i][2]));
        }
        
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        
        pq.offer(new Edge(1, 0));
        
        while (!pq.isEmpty()) {
            
            Edge current = pq.poll();

            if(visited[current.vertex]) continue;
            
            visited[current.vertex] = true;
            
            distance[current.vertex] = Math.min(distance[current.vertex], current.distance);
            
            for (Edge next : graph[current.vertex]) {
                
                if (!visited[next.vertex]) {
                    
                    pq.offer(new Edge(next.vertex, current.distance + next.distance));
                    
                }
                
            }
        }
        
        
        
        return answer;
    }
}

```

# 플로이드 와샬 알고리즘 (최단 거리)

```

class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        
        int answer = 20000001;
        
        int[][] graph = new int[n+1][n+1];
        
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                graph[i][j] = 20000001;
            }
            graph[i][i] = 0;
        }
        
        for (int i=0; i<fares.length; i++) {
            graph[fares[i][0]][fares[i][1]] = fares[i][2];
            graph[fares[i][1]][fares[i][0]] = fares[i][2];
        }
        
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
        
        for (int i=1; i<=n; i++) {
            answer = Math.min(answer, graph[s][i] + graph[i][a] + graph[i][b]);
        }
        
        return answer;
    }
}

```

# 크루스칼 알고리즘

```

import java.util.*;

class Solution {
    
    class Edge implements Comparable<Edge>{
        int currentVertex;
        int nextVertex;
        int distance;
        
        Edge (int currentVertex, int nextVertex, int distance)
        {
            this.currentVertex = currentVertex;
            this.nextVertex = nextVertex;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Edge edge) 
        {
            return this.distance - edge.distance;
        }
    }
    
    int[] parent;
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        parent = new int[n];
        
        for (int i=0; i<n; i++) {
            parent[i] = i;
        }
        
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        
        for (int i=0; i<costs.length; i++) {
            pq.offer(new Edge(costs[i][0], costs[i][1], costs[i][2]));
        }

        
        while(!pq.isEmpty()) {
            
            Edge current = pq.poll();
            
            if(find(current.currentVertex) != find(current.nextVertex)) {
                union(current.currentVertex, current.nextVertex);
                answer += current.distance;
            }
            
        }
        
        return answer;
    }
    
    public int find(int x)
    {
        if (parent[x] == x) {
            return x;
        } else {
            return find(parent[x]);
        }
    }
    
    public void union(int x, int y)
    {
        parent[find(x)] = find(y);
    }
}

```

# Node Connect + Priority Queue (트리 형태)

```

class Node implements Comparable<Node>{
        
    int x;
    int y;
    int num;
    Node left;
    Node right;
    
    
    Node (int x, int y, int num) {
        this.x = x;
        this.y = y;
        this.num = num;
    }
    
    @Override
    public int compareTo(Node node) {
        return node.y - this.y;
    }
}

PriorityQueue<Node> pq = new PriorityQueue<>();
        
for (int i=0; i<n; i++) {
    pq.offer(new Node(nodeinfo[i][0], nodeinfo[i][1], i+1));
}

Node root = pq.poll();


public void connectNode(Node parent, Node child)
    {
        if (parent.x > child.x) {
            
            if (parent.left == null) {
                parent.left = child;
            } else {
                connectNode(parent.left, child);
            }
            
        } else {
            
            if (parent.right == null) {
                parent.right = child;
            } else {
                connectNode(parent.right, child);
            }
                
        }
    }

```

# DFS (문자열)
 
```

import java.util.*;

class Solution {
    
    String[][] copyTickets;
    
    int n;
    
    ArrayList<String> answerList = new ArrayList<>();
    
    boolean[] visited;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        
        n = tickets.length;
        
        visited = new boolean[n];
        
        copyTickets = tickets;
        
        dfs("ICN", "ICN", 0);
        
        Collections.sort(answerList);
        
        return answerList.get(0).split(" ");
    }
    
    public void dfs(String before, String str, int depth)
    {
        if (depth == n) {
            answerList.add(str);
            return;
        }
        
        for (int i=0; i<n; i++) {
            if(before.equals(copyTickets[i][0]) && !visited[i]) {
                visited[i] = true;
                dfs(copyTickets[i][1], str + " " + copyTickets[i][1], depth+1);
                visited[i] = false;
            }
        }
    }
}

```

# DFS

```


// depth 와 배열로 순열 만들기

void dfs(String str, int depth, int[] card)
{
    if(card.length == depth) {
        list.add(str);
        return;
    }

    for(int i=0;i<card.length;i++) {
        int num = card[i];
        if(!comb.contains(""+num)) {
            dfs(str+num, depth+1, card);
        }
    }
}


void dfs(boolean[] visited, int[] dist, int idx)
    {
        if (idx == dist.length) {
            list.add(dist); // dist Array를 arrayList에 넣는 상황
            return;
            for(int[] weak_case : weak_cases) {
                check(dist, weak_case); // dist Array를 그대로 활용하는 상황
            }
        }

        for(int i=0; i<dist.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                dist[idx] = dist[i];
                dfs(visited, dist, idx+1);
                dist[idx] = 0;
                visited[i] = false;
            }
        }
    }

```