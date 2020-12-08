# Crontab

https://m.blog.naver.com/PostView.nhn?blogId=stereok2&logNo=221689408210&targetKeyword=&targetRecommendationCode=1

해킹 관련 내용이 자주 출제 되는데, 해킹할 때 중요한 것은..

로그, 패스워드, 크론탭, 프로세스, 소유자 권한(setGid, setUid), chown, chgrp 등이 중요하다고 생각된다

crontab -e 명령어로 수정

crontab -l 로 등록된 내용 확인 가능

0 1 * * 1-5 /batch/restart.sh

매월 매일 월~금요일 오전1시에 /batch/restart.sh 실행

분 시 일 월 요일 작업

특정 사용자의 crontab 편집 crontab -u 유저명 -e

# chmod

chmod 777 test.sh (owner, group, other에 rwx 권한 부여)

# umask

chmod가 이미 존재하는 파일 및 디렉토리에 대한 권한을 변경하는 것이라면,

umask는 파일이 생성될 때 기본적으로 부여하는 권한을 제어합니다.

umask 022 설정 시 파일은 666 - 022 = 644 권한이 부여됩니다.
umask 022 설정 시 디렉토리는 777 - 022 = 755 권한이 부여됩니다.

즉, 파일과 디렉토리는 기준이 되는 full 권한에 차이가 있습니다.

chown 소유주.그룹명 파일명 : 특정 파일의 소유주 및 그룹 변경
chown -R 소유주.그룹명 디렉토리명 : 특정 디렉토리 하위의 모든 파일 및 디렉토리의 소유주 및 그룹 변경

SetUID : 실행 중인 프로세스의 EUID를 소유주의 ID로 변경 (chmod 4xxx or chomd u+s)

SetGID : 실행 중인 프로세스의 EGID를 소유주의 Group ID로 변경 (chmod 2xxx or chmod g+s)

Sticky Bit : 시스템의 모든 사용자가 파일이나 하위 디렉토리 생성 가능 (삭제는 불가) (chmod 1xxx or chmod o+t)

perm -4000과 perm 4000의 차이

마이너스가 붙어 있으면 setuid 비트를 포함하는 파일 검색, 마이너스가 없으면 setuid 비트만 설정된 파일 검색

파일의 수정일이 n일 미만(-) or 초과(+) 파일 검색

find -type -f -mtime -1 -exec ls -al {} \;

파일의 크기가 n미만(-) or 초과(+) 파일 검색

find -type f -size +3M -exec ls -al {} \;