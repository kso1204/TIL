# Rootkit

점검 도구 chkrootkit

루트킷은 지속적으로 자신의 존재가 탐지되지 않도록 숨기면서 관리자 권한의 획득과 백도어 등의 기능을 수행하는 코드와 프로그램의 집합을 말한다.

루트킷이라는 이름은 공격자가 루트 권한을 획득하기 위한 공격에서 유래된 표현으로 초기에는 주로 서버 장비에 설치되어 telnet, ftp 등의 패킷을 스니핑하여 대상 시스템의 아이디와 패스워드를 획득하여 루트 권한을 탈취하는 방식이었다.

chkrootkit -q 감염된/변조된 파일만 보여준다.

검사결과 숨겨진 파일은 실제 공격자가 의도적으로 숨긴 파일인지 확인이 필요하다.

/proc 파일 시스템

유닉스/리눅스 커널이 메모리상에 사용하고 있는 모든 자원들에 대한 정보들을 파일 형식으로 보관하는 파일시스템이다.

커널이 관리하는 프로세스 등의 자원, 커널 파라미터 등에 대한 상태정보를 파일명으로 보관하고 있으며 물리적 디스크 영역이 아닌 메모리 영역에 존재하는 파일 시스템으로 매 부팅시마다 새롭게 생성된다.


일반적으로 루트킷은 공격자가 숨기고자 하는 프로세스가 출력되는 부분만 제거하고 출력하도록 ps 프로그램을 만들어 타겟 시스템에 있는 정상적인 ps 프로그램과 교체하는 방식으로 동작한다.

루트킷 탐지 프로그램은 ps 실행 결과와 /proc 디렉터리에 있는 프로세스 정보를 비교하여 /proc 디렉터리에는 프로세스가 있지만 ps 실행 시 보이지 않는 프로세스를 히든 프로세스로 탐지한다.

rpm 명령을 이용하여 변조된 파일 확인

rpm -V 패키지이름 (무결성을 검사한다)

S : 파일 크기 변경, M : 파일 퍼미션 변경, 5 : MD5 체크섬 변경, T : 파일 수정 시간 변경
U : 소유자 정보 변경, G : 소유 그룹 정보 변경, D : 장치 정보 변경, L : 심볼릭 링크 정보 변경

패키지 재설치

패키지 재설치 시 오류 발생

lsattr 명령을 통해 파일 속성 정보를 확인하면 i 속성이 설정되어 설치 시 삭제가 되지 않은 것을 알 수 있다.

chattr -i 로 i속성 제거

변조/감염이 확인된 파일만 교체하는 것은 임시방편이고 최선의 방법은 해당 시스템을 다시 설치하는 것이다.

chattr +iaA

i 읽기 전용 모드 a 해당 파일에 내용 추가만 허용 A 해당 파일의 Access Time을 변경하지 않는다.
