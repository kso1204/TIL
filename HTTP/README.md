# HTTP

1. HTTP 개관

- 대부분의 URL은 세 부분으로 이루어진 표준 포맷을 따른다.
- URL의 첫 번째 부분은 스킴이라고 불리는데, 리소스에 접근하기 위해 사용되는 프로토콜을 서술한다. 보통 HTTP 프로토콜(http://)이다.
- 두 번째 부분은 서버의 인터넷 주소를 제공한다. (예: www.joes-hardware.com)
- 마지막은 웹 서버의 리소스를 가리킨다 (예: /specials/saw-blade.gif)
- 오늘날 대부분의 URI는 URL이다.
- HTTP 트랜잭션은 요청 명령(클라이언트에서 서버로 보내는)과 응답 결과(서버가 클라이언트에게 돌려주는)로 구성되어 있다.
- HTTP는 네트워크 통신의 핵심적인 세부사항에 대해서 신경 쓰지 않는다.
- 대신 대중적이고 신뢰성 있는 인터넷 전송 프로토콜인 TCP/IP에게 맡긴다.
- TCP는 다음을 제공한다.
- 오류 없는 데이터 전송
- 순서에 맞는 전달(데이터는 언제나 보낸 순서대로 도착한다.)
- 조각나지 않는 데이터 스트림(언제든 어떤 크기로든 보낼 수 있다.)

```

HTTP - 애플리케이션 계층
TCP - 전송 계층
IP - 네트워크 계층
네트워크를 위한 링크 인터페이스 - 데이터 계층
물리적인 네트워크 하드웨어 - 물리 계층

HTTP 네트워크 프로토콜 스택

```

- URL 예:

```

http://207.200.83.29:80/index.html
http://www.netscape.com:80/index.html
http://www.netscape.com/index.html

첫 번째 URL은 IP 주소 '207.200.83.29' 와 포트번호 '80'을 갖고 있다.
두 번째 URL에는 숫자로 된 IP 주소가 없다. 대신 글자로 된 도메인 이름 혹은 호스트 명 ("www.netscape.com")을 갖고 있다.
호스트 명은 IP 주소에 대한 이해하기 쉬운 형태의 별명이다.
호스트 명은 도메인 이름 서비스(Domain Name Service, DNS)라 불리는 장치를 통해 쉽게 IP로 변환될 수 있다.

```


- HTTP 클라이언트가 서버에 메시지를 전송할 수 있게 되기 전에, 인터넷 프로토콜(Internet Protocol, IP) 주소와 포트번호를 사용해 클라이언트와 서버 사이에 TCP/IP 커넥션을 맺어야 한다.
- 웹 브라우저가 어떻게 HTTP를 이용해서 멀리 떨어진 곳에 있는 서버의 단순한 HTML 리소스를 사용자에게 보여주는지? - 15Page

```

웹브라우저는 서버의 URL에서 호스트 명을 추출한다.
웹브라우저는 서버의 호스트 명을 IP로 변환한다.
웹브라우저는 URL에서 포트번호(있다면)를 추출한다.
웹브라우저는 웹 서버와 TCP 커넥션을 맺는다.
웹브라우저는 서버에 HTTP 요청을 보낸다.
서버는 웹브라우저에 HTTP 응답을 돌려준다.
커넥션이 닫히면, 웹브라우저는 문서를 보여준다.

```

- 웹의 구성요소 
- 프락시 - 클라이언트와 서버 사이에 위치한 HTTP 중개자
- 캐시 - 많이 찾는 웹페이지를 클라이언트 가까이에 보관하는 HTTP 창고
- 게이트웨이 - 다른 애플리케이션과 연결된 특별한 웹 서버
- 터널 - 단순히 HTTP 통신을 전달하기만 하는 특별한 프락시
- 에이전트 - 자동화된 HTTP 요청을 만드는 준지능적 웹클라이언트

2. URL과 리소스

- URL은 브라우저가 정보를 찾는데 필요한 리소스의 위치를 가리키며, URL을 이용해 사람과 애플리케이션이 인터넷상의 수십억 개의 리소스를 찾고 사용하며 공유 할 수 있다.
- URL은 통합 자원 식별자 (Uniform Resource Identifter, URI) 라고 불리는 더 일반화된 부류의 부분집합이다.
- 대부분의 URL은 동일하게 '스킴://서버위치/경로' 구조로 이루어져 있다.
- 상대 참조 해석하기 P39
- 기저(base)URL 과 절대 URL

3. HTTP 메시지

- 메시지는 원 서버 방향을 인바운드로 하여 송신된다.
- HTTP는 인바운드와 아웃바운드라는 용어를 트랜잭션 방향을 표현하기 위해 사용한다.
- 메시지가 원 서버로 향하는 것은 인바운드로 이동하는 것이고, 모든 처리가 끝난 뒤에 메시지가 사용자 에이전트로 돌아오는 것은 아웃바운드로 이동하는 것이다.
- 메시지는 시작줄, 헤더 블록, 본문 이렇게 세 부분으로 이루어진다.
- 시작줄과 헤더는 그냥 줄 단위로 분리된 아스키 문자열이다.
- 각 줄은 캐리지 리턴과 개행 문자로 구성된 두 글자의 줄바꿈 문자열로 끝난다.
- 이 줄바꿈 문자열은 'CRLF'라고 쓴다.
- HTTP 요청 메시지는 명령과 URL을 포함한다.
- HTTP 응답 메시지는 트랜잭션의 결과를 포함한다.
- 모든 HTTP 메시지는 시작줄로 시작한다. 요청 메시지의 시작줄은 무엇을 해야 하는지 말해준다. 응답 메시지의 시작줄은 무슨 일이 일어났는지 말해준다.
- 요청 메시지는 서버에게 리소스에 대해 무언가를 해달라고 부탁한다. 요청 메시지의 시작줄, 혹은 요청줄에는 서버에서 어떤 동작이 일어나야 하는지 설명해주는 메서드와 그 동작에 대한 대상을 지칭하는 요청 URL이 들어있다.

4. 커넥션 관리

5. 웹 서버

6. 프락시

7. 캐시

8. 통합점: 게이트웨이, 터널, 릴레이

9. 웹 로봇

10. HTTP/2.0

11. 클라이언트 식별과 쿠키

12. 기본 인증

13. 다이제스트 인증

14. 보안 HTTP

15. 엔터티와 인코딩

16. 국제화

17. 내용 협상과 트랜스코딩

18. 웹 호스팅

19. 배포 시스템

20. 리다이렉션과 부하 균형

21. 로깅과 사용 추적