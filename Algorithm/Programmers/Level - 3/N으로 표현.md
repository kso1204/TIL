# N으로 표현

# 문제 설명

1. 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

2. 12 = 5 + 5 + (5 / 5) + (5 / 5)

3. 12 = 55 / 5 + 5 / 5

4. 12 = (55 + 5) / 5

5. 5를 사용한 횟수는 각각 6,5,4 입니다.

6. 그리고 이중 가장 작은 경우는 4입니다.

7. 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한 사항

# 해결 방안

# 풀이

- DP 풀이

```

public int solution(int N, int number) {
        int answer = -1;

        Set<Integer>[] set = new Set[8];

        int target = 0;

        for (int i = 0; i < 8; i++){
            set[i] = new HashSet<>();
            target = target * 10 + N;
            set[i].add(target);
        }

        for (int i = 2; i <= 8; i++){
            for (int j = 1; j < i; j++){
                for (int n : set[j - 1]){
                    for (int m : set[i - j - 1]){
                        set[i - 1].add(n + m);
                        set[i - 1].add(n * m);
                        set[i - 1].add(n - m);
                        if (m != 0) set[i - 1].add(n / m);
                    }
                }
            }
        }

        for (int i = 0; i < 8; i++){
            if (set[i].contains(number)) {
                answer = i + 1;
                break;
            }
        }

        return answer;
    }

```

- DFS 풀이

```

일반적인 DFS와 다르게 depth가 1부터 8-depth까지 진행하는 이유는

숫자를 이어붙이는 개념인 n*10 + n을 사칙연산하기 위함이다.

class Solution {
    
    int number = 0;
    int n = 0;
    int answer = 9;
    
    public int solution(int N, int number) {
        
        this.number = number;
        this.n = N;
        
        dfs(1,n);
        
        return answer<= 8? answer: -1;
    }

    
    public void dfs (int depth, int num)
    {
        if(depth > 8) {
    		return;    		
    	}
    	
        if(num == number) {
            answer = Math.min(depth, answer); 
            return;
        }
        
        int temp = n;
        
        
        for (int i=1; i<=8-depth; i++) {
            
            dfs(depth+i, num + temp);
            dfs(depth+i, num - temp);
            dfs(depth+i, num / temp);
            dfs(depth+i, num * temp);
            temp*=10;
            temp+=n;
            
        }
    }
}

```