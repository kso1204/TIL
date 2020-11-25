# IPSec

참고 : https://m.blog.naver.com/PostView.nhn?blogId=sdug12051205&logNo=221537706305&proxyReferer=https:%2F%2Fwww.google.com%2F

스샷으로만 공부하니까 눈으로만 보고 넘어간다.. 꼭 그려보거나 써보길

나중에 생각이 애매하게 난다.

IPSec의 AH, ESP 보안 헤더에 대하여 전송모드/터널 모드로 운영 시 인증 구간, 암호화 구간을 설명하고, 키 교환 프로토콜명을 기술하시오.

특징

기밀성, 비연결형 무결성, 데이터 원천 인증, 재전송 공격 방지, 접근제어, 제한된 트래픽 흐름의 기밀성

1. AH 전송모드

- 인증구간 : IP 헤더에서 전송 중 변경가능 필드(TTL, Checksum 등)을 제외한 IP패킷 전체를 인증
- 암호화구간 : (암호화 미지원)

IP Header AH Header IP Payload


2. AH 터널모드

- 인증구간 : New IP 헤더에서 전송 중 변경가능 필드를 제외한 New IP 패킷 전체를 인증
- 암호화구간 : (암호화 미지원)

New IP Header AH Header IP Header AH Auth

3. ESP 전송모드

- 인증구간 : ESP 헤더와 암호화된 데이터(IP Payload + ESP 트레일러)를 인증
- 암호화구간 : IP Payload와 ESP 트레일러를 암호화

IP Header ESP Header IP Payload ESP Trailer ESP Auth 

인증은 ESP Header부터 ESP Trailer까지
암호화는 IP Payload부터 ESP Trailer까지 

4. ESP 터널모드

- 인증구간 : ESP 헤더와 암호화된 데이터(Original IP 헤드 + IP payload + ESP 트레일러)를 인증
- 암호화구간 : Original IP 패킷 전체(Oiriginal IP 헤드 + IP Payload) + ESP트레일러를 암호화

New IP Header ESP Header Original IP Header IP Payload ESP Trailer ESP Auth

인증은 ESP Heaer부터 ESP Trailer까지
암호화는 Original IP Header부터 ESP Trailer까지

5. IPSec 전송모드

- 보호구간 : IP패킷의 페이로드를 보호

IP Header IPSec Header IP Payload IPsec Trailer

6. IPSec 터널모드

- 보호구간 : Original IP 패킷 전체(Original IP 헤드 + IP Payload)를 보호

New IP Header IPsec Header Original IP Header IP Payload IPSec Trailer