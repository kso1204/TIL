# PortScan

https://blog.naver.com/PostView.nhn?blogId=stereok2&logNo=221855660006&parentCategoryNo=25&categoryNo=29&viewDate=&isShowPopularPosts=false&from=postView

문제가 기억이 잘 안 나는데 방화벽 룰셋 검증인지 포트 오픈여부인지 확인을 해야한다.

자신있게 포트 오픈여부라고 했다가 틀렸..

1. TCP Connect(Open) 스캔

열린 상태 - SYN + ACK 응답을 수신한 후 ACK 패킷을 전송하여 TCP 연결을 완료한다 (3-way handshake)

닫힌 상태 - RST + ACK 응답을 수신한다.

nmap -T4 -sT -p 23,80 192.168.56.100 

2. TCP SYN(Half-Open) 스캔

스텔스 스캔 방식 - TCP 세션이 완전히 성립되지 않은 상태에서 (TCP 연결 설정 미완료 상태) 대상 시스템의 포트 활성화(오픈) 여부를 알아내는 스캔 방식으로 TCP 연결 설정이 완전히 이루어지지 않기 때문에 스캔 대상 시스템에 로그가 남지 않아 공격자는 자신의 IP를 노출시키지 않으면서 스캔할 수 있는데 이렇게 흔적을 남기지 않는다는 의미에서 스텔스 스캔이라 한다.

스텔스 스캔 - TCP SYN Scan, TCP FIN Scan, TCP Xmas Scan, TCP Null Scan

열린 상태 - SYN + ACK 응답을 수신한다. 열린 상태라는 것을 확인한 다음 ACK를 보내지 않고 RST를 보내 연결을 종료

닫힌 상태 - RST + ACK 응답을 수신한다.

nmap -T4 -sS -p 23,80 192.168.56.100

3. TCP FIN/NULL/XMas 스캔

TCP FIN - FIN 제어비트만 설정 연결 종료 패킷은 FIN+ACK

TCP NULL - 제어비트 설정하지 않고 스캔

TCP Xmas - URG, PSH, FIN 제어비트를 설정

열린 상태 - 폐기하고 응답 X

닫힌 상태 - RST + ACK 응답

응답없으면 Filter 됐을 수도 있어서 Open | Filtered 상태로 처리한다.

nmap -T4 -sF -p 23,80 192.168.56.100

nmap -T4 -sN -p 23,80 192.168.56.100

nmap -T4 -sX -p 23,80 192.168.56.100

TCP ACK 스캔 - 방화벽의 룰셋 검증을 위한 목적

포트의 오픈 여부 판단이 아닌 방화벽과 같은 보안 장비의 필터링 수행 여부를 판별하기 위한 목적임

방화벽에서 필터링 되고 있으면 응답이 없거나 ICMP 메시지를 받고, 필터링 되고 있지 않다면 RST 응답을 받음


4. TCP ACK 스캔

TCP ACK 스캔 - 방화벽의 룰셋 검증을 위한 목적

포트의 오픈 여부 판단이 아닌 방화벽과 같은 보안 장비의 필터링 수행 여부를 판별하기 위한 목적임

방화벽에서 필터링 되고 있으면 응답이 없거나 ICMP 메시지를 받고, 필터링 되고 있지 않다면 RST 응답을 받음

대상 포트로 SYN을 보내는 게 아니고 ACK를 보낸다.

열린 상태 - RST 응답

닫힌 상태 - 응답 없음 or ICMP 메시지

nmap -T4 -sA -p 23,80 192.168.56.100

5. UDP 스캔

열린 상태 - UDP 응답 or 응답 X

닫힌 상태 - ICMP 에러 메시지 응답 수신

nmap -T4 -sU -p 53,123 192.168.56.100

