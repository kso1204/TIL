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