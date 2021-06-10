# N개의 최소공배수

# 문제 설명

1. 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.

2. 예를 들어 2와 7의 최소공배수는 14가 됩니다.

3. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.

4. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항

1. arr은 길이 1이상, 15이하인 배열입니다.

2. arr의 원소는 100 이하인 자연수입니다.

```

arr	result

[2,6,8,14]	168

[1,2,3]	6

```

# 해결 방안

1. 1과 2의 최소공배수 와 그 수와 8의 최소공배수.. 와 14의 최소공배수?

# 풀이

- 나의 풀이

```

class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        for (int i=1;i<arr.length;i++) {
            answer = lcb(answer, arr[i]);
        } 
        
        return answer;
    }
    
    public int gcd(int a, int b) {
        
        return b%a == 0 ? a : gcd(b%a,a);
        
    }
    
    public int lcb(int a, int b)
    {
        return (a*b) / gcd(a,b);
    }
}

```