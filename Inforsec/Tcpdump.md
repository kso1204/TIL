# tcpdump

tcpdump는 네트워크 인터페이스를 거치는 패킷의 내용을 출력해 주는 프로그램이다.

즉, 스니핑 도구의 일종으로 자신의 컴퓨터로 들어오는 모든 패킷의 내용을 도청할 수 있으며,

공격자를 추적 및 공격 유형 분석을 위한 패킷 분석 시에 활용할 수 있는 도구이다.

tcpdump는 유닉스 계열에서 설치, 활용이 가능하며 윈도우용으로는 windump가 있으며 활용 방법은 유사하다.

tcpdump의 사용 예

tcpdump -i eth0 src host 192.168.159.131 and dst port 80

eth0 인터페이스에서 출발지 IP가 192.168.159.131이고 목적지 포트가 80인 패킷들을 출력

tcpdump -i eth0 tcp port 80 and not host 192.168.159.131

eth0 인터페이스에서 출발지 또는 목적지 포트가 tcp 80이고 출발지 또는 목적지 주소가 192.168.159.131이 아닌 패킷들을 출력
