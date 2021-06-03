# Docker 기본 사항 Amazon ECS

1. https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/docker-basics.html

2. Amazon ECR은 관리형 AWS 도커 레지스트리 서비스입니다. Docker CLI를 사용하여 Amazon ECR 리포지토리에서 이미지를 푸시, 가져오기 및 관리할 수 있습니다. 

3. Amazon ECR 제품 세부 정보, 주요 고객 사례 연구 및 FAQ에 대해서는 Amazon Elastic Container Registry 제품 세부 정보 페이지.를 참조하십시오.

4. 이미지를 태그 지정하고 에 푸시하려면Amazon ECR

5. Amazon ECR 이미지를 저장할 hello-world 리포지토리를 생성합니다. 출력의 repositoryUri를 참고합니다.

6. aws ecr create-repository --repository-name hello-repository --region region

```

{
    "repository": {
        "registryId": "aws_account_id",
        "repositoryName": "hello-repository",
        "repositoryArn": "arn:aws:ecr:region:aws_account_id:repository/hello-repository",
        "createdAt": 1505337806.0,
        "repositoryUri": "aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository"
    }

```



6. AWS Docker 컨테이너 배포 

- https://aws.amazon.com/ko/getting-started/hands-on/deploy-docker-containers/



7. Amazon ECS 첫 실행 설정

- Amazon ECS 첫 실행 마법사는 클러스터를 생성하고 샘플 웹 애플리케이션을 시작하는 방법을 안내합니다. 이 단계에서는 Amazon ECS 콘솔을 열고 마법사를 시작합니다.

8. 작업 정의 생성

- 작업 정의는 애플리케이션에 대한 청사진과 같습니다. 이 단계에서 Amazon ECS가 컨테이너에 어떤 Docker 이미지를 사용하고, 작업에 몇 개의 컨테이너를 사용하며, 각 컨테이너에 대한 리소스 할당은 어떻게 되는지 알 수 있도록 작업 정의를 지정합니다.

9. 서비스 구성

- 작업 정의를 생성하였으니 이제 Amazon ECS 서비스를 구성하겠습니다. 서비스는 클러스터에서 작업 정의 사본을 시작 및 유지 관리합니다. 예를 들어 애플리케이션을 서비스로 실행하면 Amazon ECS에서 중단된 작업을 복구하고 지정한 사본 수를 유지 관리합니다.

10. 클러스터 구성

- Amazon ECS 작업은 Amazon ECS 컨테이너 에이전트를 실행하는 컨테이너 인스턴스 집합인 클러스터에서 실행됩니다. 이 단계에서는 클러스터를 구성하고, 보안 설정을 검토하며, IAM 역할을 설정합니다

11. 리소스 시작 및 확인

- 이전 단계에서 작업 정의(애플리케이션 청사진과 비슷), Amazon ECS 서비스(작업 정의 사본을 시작 및 유지 관리) 및 클러스터(컨테이너 에이전트를 실행하는 컨테이너 인스턴스 집합)를 구성했습니다. 이 단계에서는 생성한 리소스를 검토, 시작 및 확인합니다.

12. 샘플 애플리케이션 열기

- 이 단계에서는 브라우저가 로드 밸런서 DNS 이름을 가리키도록 하여 샘플 애플리케이션이 실행되고 있는지 확인합니다.

13. 리소스 삭제

- 본 자습서에서는 3개의 리소스, 즉 Amazon ECS 클러스터, Amazon EC2 인스턴스 및 로드 밸런서를 시작했습니다. 이 단계에서는 원하지 않는 비용이 발생하지 않도록 모든 리소스를 정리합니다.

14. Amazon Elastic Container Registry 란 무엇입니까?

- https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html

15. Amazon Elastic Container Registry (Amazon ECR)는 안전하고 확장 가능하며 안정적인 AWS 관리 형 컨테이너 이미지 레지스트리 서비스입니다. 

16. Amazon ECR은 AWS IAM을 사용하여 리소스 기반 권한이있는 프라이빗 컨테이너 이미지 리포지토리를 지원합니다. 

17. 이를 통해 지정된 사용자 또는 Amazon EC2 인스턴스가 컨테이너 리포지토리 및 이미지에 액세스 할 수 있습니다.

18. 선호하는 CLI를 사용하여 Docker 이미지, OCI (Open Container Initiative) 이미지 및 OCI 호환 아티팩트를 푸시, 풀 및 관리 할 수 ​​있습니다.

```
Amazon ECR의 기능

수명주기 정책은 리포지토리에서 이미지의 수명주기를 관리하는 데 도움이됩니다. 

사용하지 않는 이미지를 정리하는 규칙을 정의합니다. 

규칙을 저장소에 적용하기 전에 테스트 할 수 있습니다. 

자세한 내용은 수명주기 정책을 참조하십시오 .

이미지 스캐닝은 컨테이너 이미지의 소프트웨어 취약성을 식별하는 데 도움이됩니다. 

푸시시 스캔 하도록 각 저장소를 구성 할 수 있습니다 . 

이렇게하면 저장소로 푸시 된 각각의 새 이미지가 스캔됩니다.

그런 다음 이미지 스캔 결과를 검색 할 수 있습니다. 

자세한 내용은 이미지 스캔을 참조하십시오 .

교차 리전 및 교차 계정 복제를 사용하면 필요한 곳에 이미지를 더 쉽게 저장할 수 있습니다. 

이는 레지스트리 설정으로 구성되며 지역별로 설정됩니다. 

자세한 내용은 개인 레지스트리 설정을 참조하십시오 .

```

# ECS
