# Route 53

https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/welcome-dns-service.html

우리 회사는 mydirect라는 업체를 사용하는데, 4번에서 route 53 네임 서버의 이름을 사용하여 요청에 응답하는 것처럼 마이다이렉트 업체의 네임 서버의 이름을 사용하여 요청에 응답하는 것이다.

DNS 해석기는 168.126.63.1의 IP주소를 가지고 있는 KT(인터넷 서비스 제공업체) DNS를 생각하면 될듯?

Route 53을 알아야 하는 이유는?

특정 도메인에 접근하려고 했을 때의 절차에 대해서 이해하고 있는지..

여기서 AWS에서는 어떤 정책을 펼쳐서 보다 빠르게 접근할 수 있도록 해주는지? Cache사용, https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/routing-policy.html


![how-route-53-routes-traffic](https://user-images.githubusercontent.com/6989005/100700360-988cfe80-33e0-11eb-9cc3-a34f5b7d846f.png)

1. 사용자가 웹 브라우저를 열어 주소 표시줄에 www.example.com을 입력하고 Enter 키를 누릅니다.
2. www.example.com에 대한 요청은 일반적으로 케이블 인터넷 공급업체, DSL 광대역 공급업체 또는 기업 네트워크 같은
인터넷 서비스 제공업체(ISP)가 관리하는 DNS 해석기로 라우팅됩니다.
3. ISP의 DNS 해석기는 www.example.com에 대한 요청을 DNS 루트 네임 서버에 전달합니다.
4. DNS 해석기는 www.example.com에 대한 요청을 이번에는 .com 도메인의 TLD 네임 서버 중 하나에 다시 전달합니다.
.com 도메인의 네임 서버는 example.com 도메인과 연관된 4개의 Route 53 네임 서버의 이름을 사용하여 요청에 응답합니다.
DNS 해석기는 4개의 Route 53 네임 서버를 캐시에 저장합니다. 다음에 누군가 example.com을 찾아볼 때 example.com의
네임 서버가 이미 있으므로 해석기는 3단계와 4단계를 건너뜁니다. 네임 서버는 일반적으로 2일 동안 캐시에 저장됩니다.
5. DNS 해석기는 Route 53 네임 서버 하나를 선택하여 www.example.com에 대한 요청을 해당 네임 서버에 전달합니다.
6. Route 53 네임 서버는 example.com 호스팅 영역에서 www.example.com 레코드를 찾아 웹 서버의 IP 주소 192.0.2.44 등 연관된 값을 받아 이 IP 주소를 DNS 해석 프로그램에 반환합니다.
7. DNS 해석기가 마침내 사용자에게 필요한 IP 주소를 해석해 냅니다. 해석기는 이 값을 웹 브라우저로 반환합니다.
또한 DNS 해석기는 다음에 누군가가 example.com을 탐색할 때 보다 빠르게 응답할 수 있도록 사용자가 지정하는 일정 기간 동안 example.com의 IP 주소를 캐시에 저장합니다.
8. 웹 브라우저는 DNS 해석기로부터 얻은 IP 주소로 www.example.com에 대한 요청을 전송합니다. 여기가 콘텐츠가 있는 곳, 
예컨대 Amazon EC2 인스턴스 또는 웹 사이트 엔드포인트로 구성된 Amazon S3 버킷에서 실행되는 웹 서버입니다.
9. 192.0.2.44에 있는 웹 서버 또는 그 밖의 리소스는 www.example.com의 웹 페이지를 웹 브라우저에게 반환하고, 웹 브라우저는 이 페이지를 표시합니다.

10. Route53 은 DNS설정의 핵심..

11. 어떻게 주소를 가지고 와서 웹 사이트를 렌더링 해주는지.

12. SOA, A, AAAA, NS 등의 차이는 무엇인지

13. 인스턴스에 할당했을 때, 로드밸런스에 할당했을 때 차이는 무엇인지