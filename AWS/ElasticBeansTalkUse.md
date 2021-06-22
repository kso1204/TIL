# ElasticBeansTalkUse

1. https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html

2. Amazon Web Services(AWS)는 100개 이상의 서비스로 구성되어 있으며 각 서비스는 기능 영역을 나타냅니다.

3. 다양한 서비스는 AWS 인프라 관리 방법의 유연성을 제공하는 반면에 어떤 서비스를 사용해야 하고 해당 서비스를 프로비저닝하는 방법을 파악하는 것이 까다로울 수 있습니다.

4. Elastic Beanstalk를 사용하면 애플리케이션을 실행하는 인프라에 대해 자세히 알지 못해도 AWS 클라우드에서 애플리케이션을 신속하게 배포하고 관리할 수 있습니다.

5. Elastic Beanstalk를 사용하면 선택 또는 제어에 대한 제한 없이 관리 복잡성을 줄일 수 있습니다.

6. 애플리케이션을 업로드하기만 하면 Elastic Beanstalk에서 용량 프로비저닝, 로드 밸런싱, 조정, 애플리케이션 상태 모니터링에 대한 세부 정보를 자동으로 처리합니다.

7. Elastic Beanstalk는 Go, Java, .NET, Node.js, PHP, Python 및 Ruby에서 개발된 애플리케이션을 지원합니다.

8. 애플리케이션을 배포할 때, AWS Elastic Beanstalk가 선택된 지원 가능 플랫폼 버전을 구축하고 Amazon EC2 등의 AWS 리소스를 하나 이상 프로비저닝하여 애플리케이션을 실행합니다.

9. Elastic Beanstalk 콘솔, AWS 명령줄 인터페이스(AWS CLI) 또는 Elastic Beanstalk를 위해 특별히 설계된 고급 CLI인 eb를 이용해 Elastic Beanstalk와 상호 작용할 수 있습니다.

10. Elastic Beanstalk를 사용하여 샘플 웹 애플리케이션을 배포하는 방법에 대해 자세히 알아보려면 AWS 시작: 웹 애플리케이션 배포를 참조하십시오.

11. 또한 Elastic Beanstalk 웹 인터페이스(콘솔)에서 직접 Amazon EC2 인스턴스의 플릿 크기 변경 또는 애플리케이션 모니터링 등과 같은 대부분의 배포 작업을 수행할 수 있습니다.

12. Elastic Beanstalk를 사용하려면 애플리케이션을 생성하고, 애플리케이션 소스 번들의 형태(예: Java .war 파일)로 애플리케이션 버전을 Elastic Beanstalk에 업로드하고, 애플리케이션에 대한 몇 가지 정보를 제공합니다. 

13. Elastic Beanstalk가 자동으로 환경을 실행하고 코드 실행에 필요한 AWS 리소스를 생성 및 구성합니다. 환경 실행 후에는 환경을 직접 관리하고 새로운 앱 버전을 배포할 수 있습니다.

14. 다음 다이어그램은 Elastic Beanstalk의 워크플로를 보여 줍니다.

# 예제 생성

1. 이 단계에서는 기존 예제 애플리케이션에서 시작하는 새 애플리케이션을 생성합니다.

2. Elastic Beanstalk는 다양한 프로그래밍 언어, 애플리케이션 서버 및 Docker 컨테이너를 위한 플랫폼을 지원합니다. 애플리케이션을 만들 때 플랫폼을 선택합니다.

3. AWS Elastic Beanstalk 애플리케이션의 리소스에 태그를 적용 할 수 있습니다.

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html?icmpid=docs_elasticbeanstalk_console

4. 태그는 AWS 리소스와 관련된 키-값 쌍입니다.

5. 태그는 리소스를 분류하는 데 도움이 될 수 있습니다.

6. 여러 AWS 애플리케이션의 일부로 많은 리소스를 관리하는 경우 특히 유용합니다.

7. 