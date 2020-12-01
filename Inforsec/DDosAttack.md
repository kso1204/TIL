# DDos

https://blog.naver.com/stereok2/221425992055

1. Smurf 공격 원리 및 대응 방법

- 원리 : 공격자가 출발지 IP를 희생자IP로 위조(Spoofing)한 후 증폭 네트워크로 ICMP Echo request를 브로드캐스트하여,
다수의 ICMP Echo reply가 희생자에게 전달되어 서비스를 마비시키게 됨

-대응방법
1) 동일한 ICMP Echo reply 패킷이 발생하는 경우 IPS(침입차단시스템)을 통해 모두 차단(Drop)
2) 다른 네트워크로부터 자신의 네트워크로 들어오는 Directed Broadcast 패킷을 허용하지 않도록 라우터 설정(no ip directed-broadcast)
3) 브로드캐스트 주소로 전송된 ICMP Echo request 메시지에 응답하지 않도록 시스템 설정
