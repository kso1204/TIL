# CodeBuill

1. AWS CLI를 사용하여 AWS CodeBuild 시작하기

```

단계 1: 소스 코드 생성

단계 2: buildspec 파일 생성

단계 3: 두 개의 S3 버킷 생성

단계 4: 소스 코드 및 buildspec 파일 업로드

단계 5: 빌드 프로젝트 생성

단계 6: 빌드를 실행합니다.

단계 7: 요약된 빌드 정보 보기

8단계: 자세한 빌드 정보 보기

단계 9 빌드 출력 아티팩트 가져오기

단계 10 S3 버킷 삭제

```


- https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/getting-started-cli.html

2. 이 자습서에서는 AWS CodeBuild ild를 사용하여 샘플 소스 코드 입력 파일 (입력 아티팩트 작성또는빌드 입력) 를 배포 가능한 버전의 소스 코드 (빌드 출력 아티팩트또는빌드 출력).

3.  특히, 가 일반적인 CodeBuild 도구인 Apache Maven을 사용하여 Java 클래스 파일 세트를 Java Archive (JAR) 파일에 빌드하도록 명령을 지정합니다.

4. 이 자습서는 Apache Maven이나 Java에 익숙하지 않아도 완료할 수 있습니다.

5. CodeBuild 콘솔, AWS CodePipeline, AWS CLI 또는 AWS SDK를 통해 코드 빌드를 사용할 수 있습니다.

6. 이 자습서는 AWS CLI와 함께 CodeBuild 를 사용하는 방법을 설명합니다. 

7. CodePipeline 을 사용하는 방법에 대한 자세한 내용은코드 빌드와 함께 코드 파이프 라인 사용을 선택합니다.

9. AWS CodePipeline 을 사용하여 코드 테스트 및 빌드 실행

- https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/how-to-create-pipeline.html

10. AWS CodePipeline 을 사용하여 코드를 테스트하고 빌드를 실행할 수 있습니다.

11. 다음 표에는 작업 및 작업을 수행하는 데 사용할 수 있는 방법이 나열되어 있습니다. 이러한 작업을 수행하기 위해 AWS SDK를 사용하는 것은 이 주제와 관련되지 않습니다.

12. CodeCodeBuild ild를 사용하여 빌드를 자동화하는 CodePipeline을 사용하여 CD (연속 전달) 파이프

# 단계 1: 소스 코드 생성

1. 이 단계에서는 CodeBuild가 출력 버킷에 빌드하도록 할 소스 코드를 생성합니다. 

2. 이 소스 코드는 두 개의 Java 클래스 파일 및 Apache Maven Project Object Model(POM) 파일로 구성됩니다.

3. 로컬 컴퓨터나 인스턴스의 빈 디렉터리에 다음 디렉터리 구조를 생성합니다.

4. (root directory name)
    `-- src
         |-- main
         |     `-- java
         `-- test
               `-- java


#  단계 2: buildspec 파일 생성

1. 이 단계에서는 빌드 사양 파일을 생성합니다. buildspec는 가 빌드를 실행하는 데 사용하는 YAML 형식의 CodeBuild 및 관련 설정의 모음입니다. 

2. 빌드 사양 없이는 CodeBuild 가 빌드 입력을 빌드 출력으로 성공적으로 변환하거나 빌드 환경의 빌드 출력 결과물을 찾아 출력 버킷에 업로드할 수 없습니다.

3. 다음 파일을 생성하고 이름을 buildspec.yml로 지정한 다음 이를 루트(최상위) 디렉터리에 저장합니다.

```

version: 0.2

phases:
  install:
    runtime-versions:
      java: corretto11
  pre_build:
    commands:
      - echo Nothing to do in the pre_build phase...
  build:
    commands:
      - echo Build started on `date`
      - mvn install
  post_build:
    commands:
      - echo Build completed on `date`
artifacts:
  files:
    - target/messageUtil-1.0.jar


이 빌드 사양 선언에서:

version은 사용 중인 빌드 사양 표준의 버전을 나타냅니다. 이 빌드 사양 선언은 최신 버전인 0.2을 사용합니다.

phases는 가 명령을 실행하도록 CodeBuild를 지시할 수 있는 빌드 단계를 나타냅니다. 

여기에서는 이 빌드 단계가 install, pre_build, build 및 post_build로 나열되어 있습니다. 

이 빌드 단계 이름의 철자는 변경할 수 없으며 추가로 빌드 단계 이름을 생성할 수도 없습니다.

이 예제에서build단계에서 CodeBuild 는mvn install명령을 사용합니다. 

이 명령은 Apache Maven이 Java 클래스 파일을 컴파일 및 테스트하고 컴파일된 Java 클래스 파일을 빌드 출력 결과물에 패키지하도록 지시합니다. 

그리고 몇 가지 echo 명령을 각 빌드 단계에 추가하여 이 연습을 마치게 됩니다.

이 자습서의 뒷부분에서 자세한 빌드 정보를 확인할 때 이러한echo명령을 사용하면 CodeBuild 가 명령을 실행하는 방법 및 명령 실행 순서를 이해하는 데 많은 도움이 됩니다. 

(이 예에는 모든 빌드 단계가 포함되어 있지만, 해당 단계에서 아무 명령도 실행하지 않으려면 빌드 단계를 포함하지 않아도 됩니다.)

각 빌드 단계마다, CodeBuild 는 지정된 각 명령을 나열된 순서대로 처음부터 끝까지 한 번에 하나씩 실행합니다.

artifacts는 CodeBuild가 출력 버킷에 업로드하는 빌드 출력 아티팩트 집합을 나타냅니다. 

files는 빌드 출력에 포함시킬 파일을 나타냅니다. 

CodeBuild 는 단일messageUtil-1.0.jar파일에서 찾을 수 있습니다.

target상대 디렉토리를 빌드합니다.

파일 이름 messageUtil-1.0.jar 및 디렉터리 이름 target은 Apache Maven이 이 예제에서만 빌드 출력 결과물을 생성 및 저장하는 방식에 따라 달라집니다.

사용자 자체 빌드에서는 이러한 파일 이름과 디렉터리가 다릅니다.

자세한 내용은 buildspec 참조 단원을 참조하십시오.


```

# AWS :: ECS :: TaskDefinition

- https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html

1. AWS::ECS::TaskDefinition리소스는 Amazon Elastic Container Service (Amazon ECS) 작업의 컨테이너 및 볼륨 정의를 설명합니다.

2. 사용할 Docker 이미지, 필요한 리소스 및 Amazon ECS 서비스 또는 작업을 통한 작업 정의 시작과 관련된 기타 구성을 지정할 수 있습니다.

# ExecutionRoleArn

3. Amazon ECS 컨테이너 에이전트에 사용자를 대신하여 AWS API를 호출 할 수있는 권한을 부여하는 작업 실행 역할의 Amazon 리소스 이름 (ARN)입니다.

4.  작업 요구 사항에 따라 작업 실행 IAM 역할이 필요합니다. 자세한 내용 은 Amazon Elastic Container Service 개발자 안내서의 Amazon ECS 작업 실행 IAM 역할 을 참조하십시오 .

5. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html

6. 작업 실행 역할은 Amazon ECS 컨테이너 및 Fargate 에이전트에 사용자를 대신하여 AWS API를 호출 할 수있는 권한을 부여합니다.

7.  작업 요구 사항에 따라 작업 실행 IAM 역할이 필요합니다. 계정과 관련된 다양한 목적 및 서비스에 대해 여러 작업 실행 역할을 가질 수 있습니다.

# ContainerDefinitions

1. 작업을 구성하는 다양한 컨테이너를 설명하는 JSON 형식의 컨테이너 정의 목록입니다. 컨테이너 정의 파라미터 및 기본값에 대한 자세한 내용은 Amazon Elastic Container Service 개발자 안내서의 Amazon ECS 작업 정의 를 참조하십시오 .

2. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html

```

Amazon ECS에서 Docker 컨테이너를 실행하려면 작업 정의가 필요합니다. 다음은 작업 정의에서 지정할 수있는 몇 가지 매개 변수입니다.

작업의 각 컨테이너와 함께 사용할 Docker 이미지

각 작업 또는 작업 내의 각 컨테이너에 사용할 CPU 및 메모리 양

작업이 호스팅되는 인프라를 결정하는 사용할 시작 유형

작업의 컨테이너에 사용할 Docker 네트워킹 모드

작업에 사용할 로깅 구성

컨테이너가 완료되거나 실패한 경우 작업을 계속 실행해야하는지 여부

컨테이너가 시작될 때 실행해야하는 명령

작업에서 컨테이너와 함께 사용해야하는 모든 데이터 볼륨

작업에서 사용해야하는 IAM 역할

작업 정의에 여러 컨테이너를 정의 할 수 있습니다. 

사용하는 매개 변수는 작업에 대해 선택한 시작 유형에 따라 다릅니다. 모든 매개 변수가 유효하지는 않습니다.

사용 가능한 매개 변수 및 작업 정의에서 유효한 시작 유형에 대한 자세한 내용은 작업 정의 매개 변수를 참조하십시오 .

```

1. buildspce 참조 단원

- https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/build-spec-ref.html

```

buildspec 파일 이름 및 스토리지 위치

buildspec을 소스 코드의 일부로 포함하는 경우, 기본적으로 buildspec 파일에 buildspec.yml이라는 이름을 지정해야 하며 이 파일을 소스 디렉터리의 루트에 배치해야 합니다.

기본 buildspec 파일 이름과 위치를 재정의할 수 있습니다. 예를 들어 다음을 수행할 수 있습니다.

동일한 리포지토리의 다른 빌드에 대해 buildspec_debug.yml 및 buildspec_release.yml과 같은 다른 buildspec 파일을 사용합니다.

buildspec 파일을 config/buildspec.yml과 같은 소스 디렉터리의 루트가 아닌 다른 위치 또는 S3 버킷에 저장합니다.

S3 버킷은 빌드 프로젝트와 동일한 AWS 리전에 있어야 합니다.
 
ARN을 사용하여 buildspec 파일을 지정합니다(예: arn:aws:s3:::my-codebuild-sample2/buildspec.yml).

```

1. 코드빌드 고급 설정

- https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/getting-started-cli-create-source-code.html

- https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/setting-up.html

2. 단원의 단계를 따르는 경우콘솔을 사용하여 시작하기가 처음으로 AWS CodeBuild 에 액세스하는 경우 이 주제의 정보가 거의 필요 없습니다.

3.  그러나, CodeBuild 를 계속하여 조직의 IAM 그룹 및 사용자에게 CodeBuild에 대한 액세스 권한 부여,

4.  CodeBuild 에 액세스할 수 있도록 AWS KMS 의 고객 마스터 키 수정, 에 액세스할 수 있도록 조직 워크스테이션 전반의 기존 서비스 역할 또는 고객 마스터 키 수정,

5.  액세스할 수 있도록 조직 워크스테이션 전반의 설정 등과 같은 작업이 필요할 수 있습니다.

6. CodeBuild 이 주제에서는 관련 설치 단계를 완료하는 방법을 설명합니다.

7. IAM 그룹 또는 IAM 사용자 (콘솔) 에 CodeBuild 액세스 권한을 추가하려면

8. https://console.aws.amazon.com/iam/에서 IAM 콘솔을 엽니다.

