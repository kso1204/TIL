# CodePipeline

https://docs.aws.amazon.com/ko_kr/codepipeline/latest/userguide/welcome-introducing.html

이 예에서 개발자가 소스 리포지토리에 변경을 가하면 CodePipeline 이 자동으로 변경 내용을 감지합니다.

그러한 변경 내용을 빌드하고 테스트를 구성하는 경우에는 그 테스트를 실행합니다.

테스트를 마친 후 테스트를 위해 빌드된 코드를 스테이징 서버로 배포합니다.

Stading 서버에서 CodePipeline 은 통합 또는 로드 테스트와 같은 추가 테스트를 실행합니다.

테스트가 성공적으로 끝나고 파이프라인에 추가한 수동 승인 작업이 승인되면 CodePipeline 은 테스트되고 승인된 코드를 프로덕션 인스턴스에 배포합니다.

CodePipeline 은 코드 배포, AWS 엘라스틱 빈줄크 또는 AWS OpsWorks Stacks 을 사용하여 애플리케이션을 EC2 인스턴스에 배포할 수 있습니다.

또한 CodePipeline 은 Amazon ECS를 사용하여 컨테이너 기반 애플리케이션을 서비스에 배포할 수 있습니다.

CodePipeline 과 함께 제공되는 통합 포인트를 이용해 빌드 서비스, 테스트 제공자, 다른 배포 대상이나 시스템 같은 다른 도구나 서비스를 플러그인할 수 있습니다.

파이프라인은 릴리스 프로세스가 요구하는 대로 단순하거나 복잡해집니다.

# CodePipeline 입력 및 출력 아티팩트

https://docs.aws.amazon.com/ko_kr/codepipeline/latest/userguide/welcome-introducing-artifacts.html

CodePipeline 은 개발 도구에 통합되어 코드 변경을 확인한 후 지속적 제공 프로세스의 모든 단계를 통해 빌드 및 배포합니다.

단계에서는 파이프라인을 만들 때 선택한 Amazon S3 아티팩트 버킷에 저장된 입력 및 출력 아티팩트가 단계에서 사용됩니다.

CodePipeline은 해당 단계의 작업 유형에 적합하게 입력 또는 출력 아티팩트 파일을 압축하고 전송합니다.

예:

CodePipeline Pipeline은 소스 리포지토리에 대한 커밋이 있을 때 파이프라인이 실행되도록 트리거하여소스단계를 따릅니다.

이전 단계의 출력 아티팩트(빌드되는 모든 파일)는 빌드 단계에 대한 입력 아티팩트로서 수집됩니다.

빌드 단계의 출력 아티팩트(빌드된 애플리케이션)는 컨테이너에 빌드되는 업데이트 도커 이미지 또는 업데이트 애플리케이션일 수 있습니다.

이전 단계의 출력 아티팩트(빌드된 애플리케이션)는 배포 단계에 대한 입력 아티팩트로서 수집됩니다(예: AWS 클라우드의 스테이징 또는 프로덕션 환경).

배포 플릿에 애플리케이션을 배포하거나, ECS 클러스터에서 실행되는 작업에 컨테이너 기반 애플리케이션을 배포할 수 있습니다.

작업을 생성하거나 편집할 때 작업의 입력 및 출력 아티팩트(들)를 지정합니다.

이 예제에서와 같이 소스 및 배포 단계가 있는 2단계 파이프라인의 경우에는 작업 편집에서 배포 작업의 입력 아티팩트를 위한 소스 작업의 아티팩트 이름을 선택합니다.

# 파이프라인 시작하기

https://docs.aws.amazon.com/ko_kr/codepipeline/latest/userguide/getting-started-codepipeline.html




1. 파이프라인

2. Source -> Build -> Deploy

# Source

1. BranchName 설정하는 부분

2. FullRposirotyId

3. 

# Build

1. build에 환경변수 설정하는 부분

2. CodeBuild -> 프로젝트 빌드 -> 프로젝트 빌드 -> 빌드세부정보-> 아래로 내리면 환경변수

3. IAM에 연결된 코드빌드관련 서비스롤이 있는데, 사용자가 직접 json으로 정책 설정하는 부분이 있다.

4. 기존에 연결된 정책에서 json코드 복사한다음 새로 만드는 곳에 붙여넣기? 인라인 정책으로

5. 다시 빌드 시작

6. 새로운 오류발생.. docker push가 안됐다고 나오는데

7. ecr-리포지토리-해당리포지토리 들어가면 이미지가 0개로 나와있었다.

8. 우측에 푸시 명령 보기를 누르면 aws-cli를 사용하여 로컬에서 띄운 도커를 만들어서 이미지와 이미지 태그를 설정하는 부분이 있다.

9. 해당 명령어를 그대로 복사하여 붙여넣기

10. 하면 해당 이미지에 대해 생성된 것을 확인할 수 있다. 다시 빌드 시작

11. 그니까 빌드하기전에 필요한 과정이 있는데 이 부분을 빼먹고 빌드한 것

12. 빌드 설정할 때 도커로 빌드할거면 권한을 주는 부분이 있는데 빌드 세부정보 -> 환경 -> 도커 이미지를 빌드하거나 빌드의 권한을 승격하려면 이 플래그를 활성화합니다.

13. 이 부분이 false로 되어 있어서 true로 변경했다.

14. 드디어 성공 처음에 빌드할 때 필요한 부분들을 잘 설정하기

15. 파이프라인에서 실패한 빌드 부분에 대해 다시 재시도를 해보면

16. 빌드 부분에 정상적으로 초록불 들어오고 deploy쪽 실패한 것 확인

# Deploy

1. Exception while trying to read the task definition artifact file from: BuildArtifact

2. 배포(codedeploy) -> 애플리케이션 -> 애플리케이션-> 배포그룹

3. 배포그룹에 프로덕션 리스너 포트를 80 -> 443으로 변경

4. 배포구성을 10percent 15minute -> ecsAllAtOnce로 변경

5. 이 부분이랑 상관이 없었다.

6. 우선.. 작업 세부정보 아티팩트 이름 이 부분 확인하고

7. ECS -> broadcast-center-dev -> 로드밸런싱 -> 대상 그룹 이름, 컨테이너 이름, 컨테이너 포트 확인

8. 운영되고 있는 Amazon ECS 클러스트 -> 작업 정의 -> 작업 실행 역할에 나오는 네임확인 (ecs-parteners-dev-role)

```

.dkr.ecr.ap-northeast-2.amazonaws.com/new-biz-backend:dev

```

9. 컨테이너 정의에 있는 컨테이너 이름 확인

10. 작업 역할 ecsTaskExecutionRole

11. 작업 실행 역할 ecs-parteners-dev-role

12. 컨테이너 정의 web

13. appspec.yaml

```

 LoadBalancerInfo: 
ContainerName: "web" 
ContainerPort: 80
PlatformVersion: "LATEST"
AssignPublicIp: "DISABLED"
```

14. taskdef.develop.json

```
"executionRoleArn": "role/ecs-partners-dev-role",

"image": "/new-biz-backend:dev",

"taskRoleArn": "role/ecsTaskExecutionRole",
"taskDefinitionArn": "task-definition/new-biz-dev:4",

```

20. 이미지 - 

15. 다른 부분 찾기

16. 작업역할 broadcast-center-dev-role -> ecsTaskExecutionRole로 변경

17. 작업 실행 역할ecsTaskExecutionRole -> broadcast-center-dev-role로 변경

18. 컨테이너 이름 broadcast-center-dev

19. 이미지..repository-url/Image:tag -> 도커 푸쉬했을 때 명령어 입력한 부분 -> 밑에 이미지 URI로 변경

20. 이 부분은 어디있냐? ECR에 레포지토리 -> 이미지 태그선택 -> 이미지 상세정보 -> 이미지 URI

21. 이 이미지 푸쉬하는 부분이 선행되어야 하는 작업이라는 것을 알 수 있다.

22. 그러고 나서 ECS를 생성하는 것

23. 컨테이너 이름이랑 이미지 설정하고 저장..

24. 이 다음에 taskdef.develop.json 생성한다음 필요한 내용 수정하는 것인데, 순서가 엉망이라 데이터에 뭐 넣어야 하는지도 잘 몰랐던 것 이 부분 따로 순서 정리

25. 이 부분을 하고 난 다음 다시 파이프라인으로 가보면 아티팩트쪽에 생긴 문제는 해결되지 않은 것을 알 수 있다.

26. 작업 구성

기존 

```

AppSpecTemplateArtifact

SourceArtifact

TaskDefinitionTemplateArtifact

SourceArtifact

TaskDefinitionTemplatePath

taskdef.develop.json

```

새로 생성한 것 

```

AppSpecTemplateArtifact

BuildArtifact

AppSpecTemplatePath

appspec.yaml

TaskDefinitionTemplateArtifact

BuildArtifact

TaskDefinitionTemplatePath

taskdef.develop.json

기존에 저장된 아티팩트를 까서 압축을 풀어보면

해당 내용의 컨테이너와 이미지 이름이 잘못들어간 것 확인

[{"name":"web","imageUri":"~/broadcast-dev:latest"}]

https://docs.aws.amazon.com/ko_kr/codepipeline/latest/userguide/file-reference.html

이미지 정의 파일을 buildspec.yml 출력 아티팩트로 포함시킨다고 했으니.. 그리고 블루그린일 경우

imageDetail.json 으로 생성하라고 했다.

해당 부분을 보고 buildspec쪽 수정해봤다.

  - echo --env ${OAUTH_SERVER}
      - ContainerName="web"
      - ImageURI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
      - printf '[{"name":"CONTAINER_NAME","imageUri":"IMAGE_URI"}]' > imagedefinitions.json
      - sed -i -e "s|CONTAINER_NAME|$ContainerName|g" imagedefinitions.json
      - sed -i -e "s|IMAGE_URI|$ImageURI|g" imagedefinitions.json
      - cat imagedefinitions.json
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
artifacts:
  files:
    - imagedefinitions.json


해당 내용 수정

      - echo --env ${OAUTH_SERVER}
      - ImageURI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
      - printf '[{"imageUri":"IMAGE_URI"}]' > imageDetail.json
      - sed -i -e "s|IMAGE_URI|$ImageURI|g" imageDetail.json
      - cat imageDetail.json
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
artifacts:
  files:
    - imageDetail.json


```

27. ECS 작업정의에서 기존에 적용된 이미지 레포네임 뒤에 이미지 태그를 추가했다.

28. taskDef.json 을 https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html

29. 위 링크에 나온 tutorial 형태로 수정하고 다시 재배포..

# SourceArtifact <-> BuildArtifact

1. 이 부분을 변경하기 위해서는 파이프라인 - 파이프라인 - 스테이지 편집에서 해당 내용 들어가서 변경하면 되는데,

2. 이 부분에 대한 문제를 찾기 위해 ecs설정 로드밸런스, route53, 서브넷, ecr기타 등등 다뒤졌다..

3. https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecs-ecr-codedeploy.html

4. 이 튜토리얼을 너무 늦게 보고.. 이미 배포 부분이 빌드아티팩트로 설정되어 있었는데, 이 부분을 내가 만든게 아니여서 찾는데 너무 오래걸렸다 ㅠㅠ

```

아마존 ECS (블루/그린)일 때 소스아티팩트로 !!

5. 소스 아티팩트를 배포 작업에 연결하려면

선택 편집 하여 배포 단계에와 편집 할 수있는 아이콘을 선택 아마존 ECS (블루 / 그린) 조치를.

창 하단으로 스크롤합니다. 에서 입력 유물 , 선택 추가 . 새 Amazon ECR 리포지토리 (예 :)에서 소스 아티팩트를 추가합니다 MyImage.

에서 작업 정의 를 선택 SourceArtifact을 한 다음 확인 taskdef.json입력됩니다.

에서 AWS CodeDeploy AppSpec 파일 을 선택 SourceArtifact을 한 다음 확인 appspec.yaml입력됩니다.

에서 동적으로 업데이트 작업 정의 이미지 에서 이미지 URI를 입력 아티팩트 선택 myimage을을 한 다음에 사용되는 자리 표시 자 텍스트 입력 taskdef.json파일 : IMAGE1_NAME. 저장을 선택합니다 .

```

# 단계

# 1 단계 : 이미지 생성 및 Amazon ECR 리포지토리로 푸시

# 2 단계 : 작업 정의 및 AppSpec 소스 파일을 생성하고 CodeCommit 리포지토리로 푸시

# 3 단계 : Application Load Balancer 및 대상 그룹 생성

# 4 단계 : Amazon ECS 클러스터 및 서비스 생성

# 5 단계 : CodeDeploy 애플리케이션 및 배포 그룹 생성 (ECS 컴퓨팅 플랫폼)

# 6 단계 : 파이프 라인 생성

# 7 단계 : 파이프 라인 변경 및 배포 확인

# 알아야 했던 것

1. Route53 호스팅영역 - 도메인 이름 - 레코드 생성

- Route53

- 사용자를 인터넷 애플리케이션으로 라우팅하는 안정적인 방법

- 도메인 이름 - 도메인은 사용자가 애플리케이션에 액세스하는 데 사용하는 이름

- 호스팅 영역 - Route 53에서 example.com과 같은 도메인의 DNS 쿼리에 응답하는 방법을 지정

- 상태 확인 - 애플리케이션과 웹 리소스를 모니터링하고 DNS 쿼리를 정상 리소스로 전달

- 트래픽 흐름 - 복잡한 구성에서의 여러 엔드포인트에 대해 정책을 만들 수 있는 시각적 도구를 사용

- 확인자 - VPC와 네트워크 간의 DNS 쿼리를 라우팅한다.

2. Amazon Elastic Container Service(ECS)는 클러스트에서 컨테이너를 손쉽게 실행, 중지 및 관리할 수 있는 확장성이 뛰어나고 빠른 컨테이너 관리 서비스이다.

- 클러스트 - 클러스트 생성

- 생성 된 클러스트 -> 서비스 생성

- 서비스 -> 작업 정의 -> 개정 생성 -> 컨테이너 정의 -> 이미지 정의 -> 포트 정의

- 작업 역할 연결 -> 작업 역할은 IAM에서 생성 -> 권한 -> 정책 연결

- 작업 역할과 작업 실행 역할에 따른 정책 설정 -> 인라인 정책 or AWS 관리형 정책

- AmazonECSTaskExecutionRolePolicy (AWS 관리형)

- KMS (AWS Key Management Service) 인라인 정책 (읽기 쓰기 목록), System Manager(목록, 읽기) -> 인라인 정책

- AWS Key Management Service (AWS KMS)는 암호화 및 키 관리 웹 서비스입니다. TLS 1.2

```

요청은 액세스 키 ID와 보안 액세스 키를 사용하여 서명해야합니다.

AWS KMS를 사용하는 일상적인 작업에는 AWS 계정 (루트) 액세스 키 ID 및 보안 키를 사용 하지 않는 것이 좋습니다 .

대신 IAM 사용자의 액세스 키 ID와 보안 액세스 키를 사용하십시오.

AWS Security Token Service를 사용하여 요청에 서명하는 데 사용할 수있는 임시 보안 자격 증명을 생성 할 수도 있습니다.

```

3. Amazon Elastic Container Registry(ECR) - 컨테이너 소프트웨어를 공개적으로 또는 비공개로 공유 및 배포합니다.

- 레포지토리 생성 - 이미지 - 푸시 명령 보기 - 따라하기

- 로컬에서 사용한 빌드파일을 aws에 이미지 태그를 포함하여 push한다.

- 해당 리포지토리와 이미지 태그는 Buildspec.yml에서 쓰인다. 

- BuildSpec의 나머지 데이터는 CodeBuild할 때 프로젝트 빌드 설정에서 환경변수, 그리고 배포할 때 사용하는 아티팩트 설정 파일 등..