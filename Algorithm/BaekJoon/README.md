# 백준 추천문제

1. https://www.acmicpc.net/category/17 대회 문제 풀이

2. https://globalhost.interdol.com/429 백준 문제 입력받는 부분 예제

3. https://www.acmicpc.net/workbook/codeplus/1 code.plus 문제집

4. https://sjs2215.tistory.com/93 baekjoon bufferReader활용법

# 속도를 개선하기 위한 방법

1. 스캐너 대신에 BufferReader 사용

```
package baekjoon;

import java.util.HashSet;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class p3052 {
 
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashSet<Integer> h = new HashSet<Integer>();
 
		
		for (int i = 0; i < 10; i++) {
			h.add(Integer.parseInt(br.readLine()) % 42);
		}
		
		System.out.print(h.size());
	}
}


```

2. 공백은 BufferReader br = new BufferedReader(new InputStreamReader(System.in));

3. br.readline(); 활용

4. 줄 내부에 있는 공백은 StringTokenizer st = new StringTokenizer(br.readline());

5. st.nextToken();으로 활용 