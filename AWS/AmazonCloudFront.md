# Amazon CloudFront

https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

Amazon CloudFront는 개발자 친화적 환경에서 짧은 지연 시간과 빠른 전송 속도로 데이터, 동영상, 애플리케이션 및 API를 전 세계 고객에게 안전하게 전송하는 고속 콘텐츠 전송 네트워크(CDN) 서비스입니다.

CloudFront는 AWS와 통합되며, AWS 글로벌 인프라와 직접 연결된 물리적 위치뿐만 아니라 다른 AWS Services와도 통합됩니다.

다양한 서비스와 원활하게 연동되는 CloudFront는 AWS Shield와 연동되어 DDoS 완화를 수행하고, 애플리케이션 오리진으로서 Amazon S3, Elastic Load Balancing 또는 Amazon EC2를 사용하고, Lambda@Edge와 연동되어 사용자지정 코드를 고객의 사용자에서 가까운 위치에서 실행하고 맞춤화된 사용자 경험을 제공합니다. 마지막으로, Amazon S3, Amazon EC2 또는 Elastic Load Balancing과 같은 AWS 오리진을 사용하는 경우, 이러한 서비스와 CloudFront 간에 전송된 데이터에 대해서는 비용을 지불하지 않습니다.

Amazon CloudFront는 .html, .css, .js 및 이미지 파일과 같은 정적 및 동적 웹 콘텐츠를 사용자에게 더 빨리 배포하도록 지원하는 웹 서비스입니다. CloudFront는 엣지 로케이션이라고 하는 데이터 센터의 전 세계 네트워크를 통해 콘텐츠를 제공합니다. CloudFront를 통해 서비스하는 콘텐츠를 사용자가 요청하면 지연 시간이 가장 낮은 엣지 로케이션으로 라우팅되므로 콘텐츠 전송 성능이 뛰어납니다.

콘텐츠가 이미 지연 시간이 가장 낮은 엣지 로케이션에 있는 경우 CloudFront가 콘텐츠를 즉시 제공합니다.

콘텐츠가 엣지 로케이션에 없는 경우 CloudFront는 콘텐츠의 최종 버전에 대한 소스로 지정된 오리진(Amazon S3 버킷, MediaPackage 채널, HTTP 서버(예: 웹 서버) 등)에서 콘텐츠를 검색합니다.

![how-you-configure-cf](https://user-images.githubusercontent.com/6989005/100704250-844cff80-33e8-11eb-89a4-13abafd7a104.png)

1. Amazon S3 버킷 또는 고유 HTTP 서버와 같은 오리진 서버를 지정하고, CloudFront는 이로부터 파일을 가져온 다음 전 세계 CloudFront 엣지 로케이션에 배포합니다. 오리진 서버는 객체의 최종 원본 버전을 저장합니다. HTTP를 통해 콘텐츠를 서비스하는 경우 오리진 서버가 Amazon S3 버킷 또는 웹 서버 같은 HTTP 서버입니다. HTTP 서버는 Amazon EC2 인스턴스나 사용자가 관리하는 서버에서 실행할 수 있습니다. 이 서버를 사용자 지정 오리진이라고 합니다.

2. 오리진 서버에 파일을 업로드합니다. 객체라고도 하는 파일에는 일반적으로 웹 페이지, 이미지 및 미디어 파일이 포함되지만,
HTTP 또는 Adobe Flash Media Server에서 사용되는 프로토콜에 해당하는 지원되는 Adobe RTMP 버전을 통해 서비스할 수 있다면
무엇이든지 포함될 수 있습니다. 
Amazon S3 버킷을 오리진 서버로 사용할 경우 버킷에 있는 객체를 공개적으로 읽을 수 있는 상태로 만들 수 있으므로 객체의 CloudFront URL을 아는 사람이라면 누구나 액세스할 수 있습니다. 객체를 비공개로 유지하고 액세스할 수 있는 사용자를 제어할 수 있는 옵션도 있습니다.

3. 사용자가 웹 사이트나 애플리케이션을 통해 파일을 요청할 경우 ??에 어떤 오리진 서버에서 파일을 가져올지 알려 주는 CloudFront 배포를 만듭니다. 동시에 CloudFront에서 모든 요청을 기록할지, 배포를 만들자마자 활성화할지 여부와 같은 세부 사항을 지정합니다.

??는.. cloudFront이려나?

4. CloudFront는 새 배포에 도메인 이름을 할당하고, 이는 CloudFront 콘솔에서 볼 수 있습니다. 또는 API 요청 등과 같은 프로그램 요청에 대한 응답으로 반환됩니다. 원하는 경우 대신 사용할 대체 도메인 이름을 추가할 수 있습니다.

5. CloudFront에서는 배포의 구성(사용자의 콘텐츠가 아님)을 모든 해당 엣지 로케이션 or CloudFront가 파일의 사본을 캐싱하는 지리적으로 분산된 데이터 센터의 POP 서버 모음으로 보냅니다.

Cache에서 유지되는 시간 최소0초 최대 100년..?

https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/Expiration.html





