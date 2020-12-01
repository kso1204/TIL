# IPTables

https://blog.naver.com/PostView.nhn?blogId=stereok2&logNo=222082203853&parentCategoryNo=25&categoryNo=29&viewDate=&isShowPopularPosts=false&from=postView

IPtable에 정책을 등록하는 옵션은 3가지가 있습니다.

- A : Append. 맨 마지막에 추가

- I : Insert. 맨 위에 추가. (Rule number  지정 가능)

iptable 정책에 대해 알아보기

첫 번째 실습은, 특정 IP에 대하여 제한된 포트로의 접속을 허용/차단하는 정책 등록입니다.

1) 소스 IP (172.30.1.55) 에서 목적지 IP (192.160.137.80) 의 80번 포트로의 접속을 허용하는 정책은 다음과 같습니다.

iptables -A INPUT -p tcp -s 172.30.1.55 -d 192.160.137.80 --dport 80 -j ACCEPT

2) 소스 IP (172.30.1.55)에서 목적지 포트(21번, ftp)로 접속을 차단하는 정책은 다음과 같습니다.

iptables -A INPUT -p tcp -s 172.30.1.55 -dport 21 -j DROP

두 번째 실습은, 세션의 연결 상태를 체크(Statefull inspection)하여 정상적인 패킷은 최초 접속 허용 후 룰 재검사를 하지 않도록 하고, 비정상적인 패킷은 Drop시키는 정책 등록입니다.

1) 최초 접속 허용 후 ESTABLISHED 또는 RELATED 상태 패킷은 룰 검사 없이 접속을 허용하는 정책은 다음과 같습니다. 룰 재검사를 하지 않아 방화벽의 성능이 향상됩니다. 

iptables -A INPUT -m state --state ESTABLISHED, RELATED -j ACCEPT

2) 최초 연결 시 SYN flag가 설정되지 않은 비정상 패킷을 차단하는 정책은 다음과 같습니다. TCP 세션을 처음 맺을 때, SYN flag가 없다면 포트 스캔과 같은 공격 행위일 가능성이 매우 높습니다.

iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP

세 번째 실습은, connlimit 모듈을 이용하여 DDoS 공격을 탐지하는 정책 등록입니다.

1) 동일 출발지 IP에서 목적지의 80번 포트로 동시 연결 개수가 5개 초과 시 [CONNLIMIT] 를 접두어로 하여 로그에 남기는 정책은 다음과 같습니다

iptables -A INPUT -p tcp --syn --dport 80 -m connlimit --conlimit-above 5 -j LOG --log-prefix "[CONNLIMIT]"

네 번째 실습은, limit 모듈을 이용하여 로깅을 최소화하는 정책 등록입니다.

1) TCP  패킷의 플래그를 검사해서, SYN, FIN 플래그만 설정된 패킷을 분당 최대 5개까지만 로그 접두어([LIMIT]를 사용하여 로그에 남기는 정책은 다음과 같습니다.

iptables -A INPUT -p tcp --tcp-flags ALL SYN,FIN -m limit --limit 5/minute -j LOG --log-prefix "[LIMIT]"



