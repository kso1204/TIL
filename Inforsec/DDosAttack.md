# DDos

https://blog.naver.com/stereok2/221425992055

1. Smurf 공격 원리 및 대응 방법

- 원리 : 공격자가 출발지 IP를 희생자IP로 위조(Spoofing)한 후 증폭 네트워크로 ICMP Echo request를 브로드캐스트하여,
다수의 ICMP Echo reply가 희생자에게 전달되어 서비스를 마비시키게 됨

-대응방법
1) 동일한 ICMP Echo reply 패킷이 발생하는 경우 IPS(침입차단시스템)을 통해 모두 차단(Drop)
2) 다른 네트워크로부터 자신의 네트워크로 들어오는 Directed Broadcast 패킷을 허용하지 않도록 라우터 설정(no ip directed-broadcast)
3) 브로드캐스트 주소로 전송된 ICMP Echo request 메시지에 응답하지 않도록 시스템 설정

2. Ping of Death 공격

Ethernet의 경우 1500 bytes, 즉 IP 패킷의 최대 크기가 1500 bytes이기 때문에 IP 헤더부(기본 20bytes)를 제외하면 ICMP 패킷은 최대 1480 bytes의 크기로 생성된다. 

Ping 패킷의 데이터 크기를 매우 크게 하여 패킷을 몇 개만 보내도 수십 개로 분할하여 목적지로 송신되는 것이다.
보통의 ICMP 패킷은 분할하지 않으므로 패킷 중 분할이 일어난 패킷을 공격으로 의심하여 탐지하는 방식을 사용한다.

현재는 일정 수 이상의 ICMP 패킷을 받으면 무시하게 설정

3. Land Attack

출발지 IP와 목적지 IP가 같은 패킷을 만들어 보냄으로써 수신자가 자기 자신에게 응답을 보내게 하여 시스템의 가용성을 침해하는 공격

방화벽에서는 출발지 IP와 목적지 IP가 같으면 무조건 DROP시킨다.

4. Teardrop Attack

IP 패킷의 재조합 과정에서 잘못된 fragment offset 정보로 인해 수신시스템이 문제를 발생하도록 만드는 DoS 공격을 말한다.

공격자는 IP fragment offset값을 서로 중첩되도록 조작하여 전송하고 이를 수신한 시스템이 재조합하는 과정에서 오류가 발생, 시스템의 기능을 마비시키는 공격

비슷한 공격은 bonk, boink가 있다.

IP fragmentaion 취약점을 이용한 IDS 우회 공격도 있는데 이건 DoS 공격이 아니다.
Tiny Fragment - ip헤더 보다 작은 fragment를 만들어서 내부 시스템에 침입하는 공격
Fragment Overlap - ip fragment의 offset값을 조작해 서비스 포트 필드를 중첩시켜서 재조합이 되고 나면 침입차단시스템(방화벽)에서 허용하지 않는 서비스에 접근 가능하게 만드는 공겨기법

OS의 보안패치를 모두 설치하여 OS의 취약점 해소
