# 우아한 테크코스 테코톡 유튜브 영상 보고 좋은 내용 정리? 

1. https://www.youtube.com/playlist?list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH

2. 한 번 더 다시보기 or 추천 *, **

3. 메모리, CPU(Register, Cache), 프로세스, 프로그램, disk에서 가장 헷갈리는 것은

4. 언제 레지스터의 값을 사용하고 캐시의 값을 사용하는지? 프로그램이 프로세스 형태로 올라가면 메인 메모리와 cpu가 값을 주고 받는데, 이 과정에서

```

처음은 메모리에서 가져와서 처리하고 그 내용에 대한 지시사항을 레지스터에 저장한 다음, 같은 주소에 대한 참조는 레지스터에서 반환해준다 정도로 이해하면 될까?


```

# 하루의 실행 컨텍스트 **

1. https://www.youtube.com/watch?v=EWfujNzSUmw&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=3

# 수리의 TCP/IP *

1. https://www.youtube.com/watch?v=BEK354TRgZ8&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=13

2. TCP/IP Layer에서 Application <-> Transport <-> Intenet <-> Network Access 과정을 이해하기 쉽게 설명했다.

# 배럴의 가상 메모리 **

1. http://www.yes24.com/Product/Goods/89496122 공룡책? 

2. https://www.youtube.com/watch?v=5pEDL6c--_k&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=17

1. main memory = physical memory = 물리 메모리 = 메모리

2. 외부저장장치 = 보조저장장치 = disk

3. 운영체제 = os = operating system = 커널?

4. io 작업 = 입출력 작업

1. CPU가 연산을 하려면 메모리의 값을 참조해야 한다. 

2. CPU는 연산할 때 레지스터 값을 참조한다. 레지스터는 자료를 보관하는 매우 빠른 기억 장소 하지만 용량이 매우 작다.

3. CPU는 메인 메모리까지의 값만 참조할 수 있기 때문에, 보조저장장치의 값을 참조하려면 OS의 도움을 받아서 입출력 작업을 진행한다.

4. 프로그램이 실행되는 것이란 CPU가 일을 하는 것 (프로그램의 정보가 메모리에 올라와 있어야 함)

5. 일반적으로 프로그램은 디스크에 이진 실행 파일 형식으로 존재한다.

6. CPU가 바라보는 프로세스가 있는 공간은 논리 주소이다.

7. 논리 주소(logical Address): CPU가 생성하는 주소

8. 물리 주소(physical address): 메모리가 취급하는 주소

9. CPU가 일을 하기 위해서는 논리 주소가 메인 메모리상에 올라와 있어야 한다.

10. 논리 주소가 물리 주소로 매핑되는 작업을 주소 바인딩이라고 한다.

11. 주소 바인딩 방식은 물리적 메모리 주소가 결정되는 시기에 따라 세 가지로 나뉜다.?

```

- 컴파일 타임 바인딩

- 로드 타임 바인딩

- 실행 시간 바인딩

```

12. 가상 메모리를 사용하기 위해서는 실행시간 바인딩이 지원 돼야 한다.

# 제이미의 Forward Porxy, Reverse Proxy, Load Balancer *

1. https://www.youtube.com/watch?v=YxwYhenZ3BE&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=128

# 현구막의 리눅스 메모리 관리 **

1. https://www.youtube.com/watch?v=qxmdX449z1U&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=54

# 조엘의 GC **

1. https://www.youtube.com/watch?v=FMUpVA0Vvjw&list=PLgXGHBqgT2TvpJ_p9L_yZKPifgdBOzdVH&index=24

# 쿨라임의 HTTP/1.1, HTTP/2, 그리고 QUIC **

1. https://www.youtube.com/watch?v=xcrjamphIp4

```

HTTP 1.1

Persistent Connection - 지정한 Timeout 동안 커넥션을 닫지 않는 방식

Pipelining - 하나의 커넥션에서 응답을 기디리지 않고 순차적인 여러 요청을 연속적으로 보내, 그 순서에 맞춰 응답을 받는 방식으로 지연 시간을 줄이는 방법

문제점 ? HTTP의 Head of Line Blocking, Header 중복

HTTP 2

HTTP 메시지 전송 방식의 변화 (Binary, 프레이밍)

요청과 응답의 다중화

리소스간 우선 순위 설정

Server Push (html만 요청해도 js, css 보내주기)

Header 압축 (Dynamic static Table? 허프만 압축 코딩)

문제점 ? TCP의 Head of Line Blocking

HTTP 3 (Quic)

TCP의 한계(지연 불가피(3-way handshake))를 극복하려는 전송 프로토콜

전송 속도 향상

Connection UUID로 서버와 연결

TLS 기본 적용

독립 스트림 사용




```

# 에단의 TLS

1. https://www.youtube.com/watch?v=EPcQqkqqouk

# 럿고의 CORS 

1. 노이즈가 너무 심함 ㅠㅠ

1. https://www.youtube.com/watch?v=7iGIfcEsc2g

# 동글 & 라면의 DNS

1. https://www.youtube.com/watch?v=5rBzHoR4F2A

# 라테의 도메인 주도 설계 DDD

1. https://www.youtube.com/watch?v=VIfNipL5KkU

# 히로의 웹 요청과 응답

1. 

# 인비의 DTO vs VO

1. https://www.youtube.com/watch?v=z5fUkck_RZM

2. DTO = 데이터 전달용, VO = 값 표현용

3. DTO

- Data Transfer Object

- 데이터를 전달하기 위해 사용하는 객체

- 데이터를 담아서 전달하는 바구니

- "계층 간" 데이터를 전달하기 위한 객체

- Controller <-> DTO <-> Service

- 오직 getter / setter 메서드 만을 갖는다.

- 다른 로직을 갖지 않는다.

- 보내는 쪽에서 setter 로 DTO 생성, 받는 쪽에서 getter 로 DTO 받아옴 

4. Entity Class를 분리하라

- Entity 클래스를 기준으로 테이블이 생성되고 스키마가 변경된다.

- Entity 클래스를 요청이나 응답 값을 전달하는 클래스로 사용한다면 뷰가 변경될 때마다 Entity 클래스를 매번 같이 변경해야 한다.

- Entity 클래스를 변경하면 무수히 많은 클래스 들에게 영향을 끼친다.

- 따라서 요청이나 응답 값을 전달하는 클래스로는 반드시 뷰에 변경에ㄷ 따라 다른 클래스들에게 영향을 끼치지 않고 자유롭게 변경할 수 있는 DTO를 사용해야 한다.

5. VO

- Value Object

- 값 그 자체를 표현하는 객체

- DTO가 getter, setter 외에 로직을 포함하지 않는 것과 달리 VO는 로직을 가진다.

- VO는 Hashcode와 Eqauls를 모두 오버라이드 해줘야 한다. => 완전한 VO가 되기 위해?

```

DTO

용도 - 레이어 간 데이터 전달

동등 결정 - 속성값이 모두 같다고 해서 같은 객체가 아니다.

가변 / 불변 - setter 존재 시 가변, setter 비 존재 시 불변

로직 - getter/setter외의 로직을 갖지 않는다.

VO

용도 - 값 자체 표현

동등 결정 - 속성값이 모두 같으면 같은 객체다

가변 / 불변 - 불변

로직 - getter / setter 외의 로직을 가질 수 있다.

```

https://dev2.peterpanz.kr/agency/list/overlap_addr