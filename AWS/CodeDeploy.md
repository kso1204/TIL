# Code Deploy

1. https://jojoldu.tistory.com/281

2. AWS CodeDeploy는 이 appspec.yml을 통해서 어떤 파일들을, 어느 위치로 배포하고, 이후 어떤 스크립트를 실행시킬것인지를 모두 관리합니다.

3. 여기서 서비스 역할을 보시면, IAM Role을 선택해야하는데요.

4. 1-5-1에서 생성한 Code Deploy용 Role을 선택합니다.

5. (EC2 Role이 아닙니다.)

6. 1-5-1. Code Deploy용 Role 생성

7. 1-1.에서 생성한 Role은 EC2를 위한 Role입니다.

8. 이번엔 Code Deploy가 EC2에 접근할 수 있도록 Role을 생성하겠습니다.