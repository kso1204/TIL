# 문자열 내 p와 y의 개수

# 문제 설명

1. 대문자와 소문자가 섞여있는 문자열 s

2. s에서 'p'의 개수와 'y'의 개수를 비교해 같으면 true, 다르면 false를 return

3. 'p', 'y'가 하나도 없으면 true를 리턴, 단 개수를 비교할 때 대문자와 소문자를 구별하지 않는다.

# 제한 사항

1. 문자열s의 길이 50이하

# 해결 방안

1. 기본은 true, count비교해서 다르면 false

2. 소문자나 대문자로 해당 string 변경

# 풀이

- 좋은 풀이

```

람다형태로 구현한 풀이

s = s.toUpperCase();

return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();

```

- 나의 풀이

```


s = s.toLowerCase();
        
int cnt = 0;

for (int i = 0; i < s.length(); i++) {
    if(s.charAt(i) == 'p') {
        cnt++;
    } else if (s.charAt(i) == 'y') {
        cnt--;
    }
}

if(cnt != 0) {
    return false;
}

return answer;

```
