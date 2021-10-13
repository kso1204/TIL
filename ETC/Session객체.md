# Session 객체란? Redis Session?

1. https://hyuntaeknote.tistory.com/8

2. https://hyuntaeknote.tistory.com/3?category=867120

3. https://hyuntaeknote.tistory.com/4?category=867120

# KEY 

1. 무상태 (stateless)

- 비연결적인 특성으로 연결이 해제됨과 동시에 서버와 클라이언트는 클라이언트가 이전에 요청한 결과에 대해서 잊어버리게 됩니다.

- 즉, 클라이언트가 이전 요청과 같은 데이터를 원한다고 하더라도 다시 서버에 연결을 하여 동일한 요청을 시도해야만 합니다.

2. 비연결성 (Connectionless)

- 비연결성이란 클라이언트가 요청(request)을 하고, 서버가 해당 요청에 적합한 응답(response)를 하게 되면 바로 연결을 끊는 성질을 의미합니다. 

# 개념

2. 세션 객체는 Key에 해당하는 SESSION ID와 이에 대응하는 Value로 구성됩니다.

3. Value에는 세션 생성 시간, 마지막 접근 시간 및 User가 저장한 속성 등 이 Map 형태로 저장됩니다.

4. 세션 객체가 저장되는 방식과 유사하게 Key-Value 형태로 데이터를 저장하는 데이터베이스가 있습니다.

5. 이를 Key-Value 데이터베이스 혹은 Key-Value Model NoSQL이라고 합니다.

6. 이러한 데이터베이스의 특징은 저장구조가 Key-Value 형태로 단순하다는 점입니다.

7. 이로 인해 관계형 데이터베이스와 같이 복잡한 조회 연산을 지원하지 않지만,

8. 단일 키 처리만을 지원하기 때문에 고속 읽기와 쓰기에 최적화된 경우가 많습니다.

9. 특히, 세션에 저장되는 데이터의 경우에는 대부분 비교적 간단한 연산을 통해 처리를 할 수 있습니다.

10. 이러한 점에서 Key-Value 형태의 데이터베이스가 세션 저장소로써 적합하다고 볼 수 있습니다.

