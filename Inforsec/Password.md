# Password 

비밀번호 작성 규칙에 대해 기술적 관리적 보호 조치 사항 3가지를 기술

1. 패스워드 복잡도 및 길이 : 영문, 숫자, 특수 문자 중 2종류 이상 조합시는 10자리 이상, 3종류 이상 조합시는 최소 8자리 이상의 길이로 구성

2. 유추하기 어려운 비밀번호 사용 : 연속적인 숫자나 생일, 전화번호 등 추측하기 쉬운 개인정보 및 아이디와 비슷한 비밀번호는 사용하지 않을 것을 권고

3. 패스워드 유효기간 설정 : 비밀번호에 유효기간을 설정하여 최소 반기별 1회 이상 변경


/etc/passwd : 리눅스 시스템에 등록된 사용자 계정 정보가 담겨 있음.

/etc/shadow : 암호화된 패스워드가 저장되어 있음.

/etc/shadow 파일의 두 번째 필드는 암호화된 패스워드입니다.

$6$XgdBQotI$9aWVZ.8iotPu0pZfUiXagWLF1AGSPjshsDrEOq.........

[출처] [보안기사 합격 방법] 실기 시험 대비 실습 - #2.리눅스 사용자 관리하기 (패스워드, PAM(장착형 인증모듈))|작성자 온계절

첫 번째 필드는 암호화에 사용된 해시 알고리즘을 의미합니다.

 - 1은 MD5, 5는 SHA-256, 6은 SHA-512

두 번째 필드는 Salt입니다. 

 - 해시 알고리즘으로 암호화를 수행할 때 Salt값을 추가함으로써 rainbow테이블(평문과 대응되는 해시값을 저장해 놓은 파일)을 사용한 패스워드 추측 공격으로부터 방어할 수 있습니다. Salt는 패스워드를 생성하거나 변경할 때 OS에서 랜덤하게 생성됩니다.

 세 번째 필드는 Hash알고리즘으로 암호화된 값 입니다.


리눅스에서 패스워드 정책 설정은 크게 3가지로 분류되며, PAM을 이용하여 관리됩니다.

1. 패스워드 복잡도 설정(/etc/security/pwquaility.conf) (미출제;)

password requisite pam_cracklib.so try_first_pass retry=3 minlen=8 lcredit=-1 ucredit=-1 dcredit=-1 ocredit=-1 difok=8

retry = 3 (3번까지 패스워드 재입력 가능)
minlen = 8 (최소 8자리 이상 설정)
lcredit = -1 (소문자 최소 1개 이상 요구)
ucredit = -1 (대문자 최소 1개 이상 요구)
dcredit = -1 (숫자 최소 1개 이상 요구)
ocredit = -1 (특수문자 최소 1개 이상 요구)
difok = 8 (기존 패스워드와의 일치율 비교, 기본값은 10 (50%))
​


2. 패스워드 사용기간 설정 (/etc/login.defs) (출제)

PASS_MAX_DAYS 60 (최대 60일간 패스워드 사용 가능)
PASS_MIN_DAYS 1 (최소 1일 경과 후 패스워드 변경 가능)
PASS_WARN_AGE 7 (만료일 7일이 남은 시점부터 패스워드 변경 알림)

3. 패스워드 잠금 임계값 설정(/etc/pam.d/system-auth) (출제)

auth required /lib/security/pam_tally.so deny=5 unlock_time=120 no_magic root reset

deny = 5 (5회 입력 실패 시 패스워드 잠금)
unlock_time = 120 (계정이 잠긴 이후 설정 시간 경과 후 잠김 해제(초))
no_magic_root (root는 패스워드 잠금 설정 예외)
reset (인증 성공 시 실패 횟수 초기화)
