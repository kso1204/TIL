# K번째 수

# 문제 설명

1. array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, K번째에 있는 수 구하기

2. 해당 수를 새로운 array에 삽입해서 리턴

# 제한 사항

1. array의 길이 1 ~ 100

2. array의 각 원소 1 ~ 100

3. commands의 길이는 1이상 50이하

4. commands의 각 원소는 길이가 3

# 해결 방안

1. arrays의 sort 기능 사용해서 새로운 array에 삽입하기

# 풀이

1. 배열 복사 참고자료

- https://coding-factory.tistory.com/548


2. 깊은 복사 방법
```

 int a[] = {1, 2, 3, 4};

 깊은 복사 방법 
 
 Object.clone, Arrays.copyOf(a, a.length), Arrays.copyOfRange(a, 1, 3);

```

- 좋은 풀이

- 문제에서 소트한 배열만 따로 계산하기 때문에 전체 배열이 아닌 i~j 까지의 데이터로 새로운 temp 배열을 만들고, 해당 배열을 sort한다.

- 그리고 answer[i]에 해당 데이터 값을 저장한다.

```

int[] answer = new int[commands.length];

    for(int i=0; i<commands.length; i++){
        int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
        Arrays.sort(temp);
        answer[i] = temp[commands[i][2]-1];
    }

return answer;

```

- 나의 풀이

- a에서 b까지의 소트를 구한다음 해당 번째의 값을 가져오기 위해 전체 Array를 이용했는데 좋은 풀이에서는 해당 범위만 복사해서 사용했다.

- answer[i]를 사용하기 위해 초기 배열의 크기를 지정해줬다. new int[commands.length];

- 저렇게 초기 배열 크기를 사용해주지 않기 위해 리스트로 변환해서 사용할까 했었는데 return 할 때 데이터 형태가 달라짐

- i에서 j번째 까지의 데이터를 잘르고 그 중 K 번째의 데이터를 가져오기 위해 숫자 값을 지정하는 데 애를 먹었다.

```

int[] answer = new int[commands.length];
        
    for (int i=0; i<commands.length; i++) {
        
            int[] tempArray = Arrays.copyOf(array, array.length);
        
            Arrays.sort(tempArray, commands[i][0] - 1, commands[i][1] );
            
            answer[i] = tempArray[commands[i][0] - 2 + commands[i][2]];
        
    }
        
return answer;


```
