# 스크립트

1. https://docs.aws.amazon.com/ko_kr/opsworks/latest/userguide/cookbooks-101-basics-commands.html

2. https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-services-ec2-instance-type-script.html

3. https://woowabros.github.io/tools/2017/08/17/ost_bash.html

- http://www.dreamy.pe.kr/zbxe/CodeClip/3765734

```



이 글에서 해볼 것
이 글에서는 두 가지 쉘 스크립트를 작성할건데요.

첫 번째,

PATH에 Working Directory 추가하기.
AWS CLI, AWS ElasticBeanstalk CLI 설치하기.
AWS Credential 추가하기.
보너스로 PHP Codeigniter를 AWS ElasticBeanstalk에 Deploy 해보기.

두 번째,

로컬 환경에서 Docker에 웹서버(PHP Codeigniter) 올려보기.
이 말인즉슨, 신규 입사자는 첫 번째 쉘 스크립트로 기본적인 AWS 기반의 개발 환경이 갖춰지고, 두 번째 쉘 스크립트로 로컬 환경에서 개발이 바로 가능해진다는 것이죠!

하지만 이 글에서는 쉘 스크립트의 문법에 대해서는 다루지 않습니다! 이곳을 참고해주세요! 이 글에서는 쉘 스크립트로 꽤 많은 것을 편하게 할 수 있다는 것을 알려드리는데에 초점이 맞춰져 있습니다.


```

4. https://aws.amazon.com/ko/getting-started/hands-on/backup-to-s3-cli/

로컬에서 aws s3로 파일 옮기기?

5. https://gobetty.tistory.com/17

서버에서 S3로 AWS CLI를 사용하여 특정 파일 복사하기

6. https://blog.algopie.com/aws/aws-cli%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-ec2%EC%97%90%EC%84%9C-s3%EB%A1%9C-%EC%97%85%EB%A1%9C%EB%93%9C%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%ED%95%98%EA%B8%B0-%EC%9A%B0%EB%B6%84%ED%88%AC/

AWS CLI를 사용하여 ec2에서 s3로 업로드/다운로드 하기 (우분투 Ubuntu)

7. 

# 스크립트를 이용해 s3에 파일 올리고 로컬에 있는 파일 삭제하기 (example.sh)

1. https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-services-s3-commands.html 이거로 안되나?

```

sh xxx.sh

laravel-cli-2020-01-17.tar.gz

```

1. 해당 서버 or 로컬에  s에 올리고자 하는 파일이 이미 존재 하고 있음.

```

cd ${BashDuseApiFile};

BashFile="laravel-cli-${BashTwoFileDate}.tar.gz"

if [ -f "${BashFile}" ]; then

```

2. shell script에 AWS s3 업로드 하는 프로세스를 만들어야함. (aws s3 putobject ? getobject ? )

```

for file in "$path"/*; do
    putS3 "$path" "${file##*/}" "/path/on/s3/to/files/"
done

```

3. 이때 현재 압축된 파일이 년 월 일 로 되어있는데, 해당 압축 파일 전부 s3에 올리는 프로세스 

4. 3번이 검증이 되면 해당 1번에 있는 파일을 지운다.

```
 sudo rm -rf "${BashDuseApiFile}/${BashFile}"
```