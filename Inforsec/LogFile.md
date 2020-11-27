# LogFile

utmp 현재 시스템에 로그인한 사용자의 상태가 출력되는 로그 w, who, users, finger

wtmp 사용자의 로그인, 로그아웃, 시스템 재부팅 정보가 출력되는 로그 last

btmp 5번 이상 로그인 실패 시 로그인 실패 정보가 기록되는 로그 lastb, loginlog(solaris)

paact 시스템에 로그인한 모든 사용자가 수행한 프로그램에 대한 정보 기록 acctcom, lastcomm

su su권한 변경 성공 실패 로그 /var/adm/sulog

history 명령어 수행 기록 history

lastlog 각 사용자의 최근 로그인 시각, 접근한 소스 호스트 정보 기록 lastlog

xferlog ftp서비스를 이용하여 파일 업/다운로드 이력 /var/log/xferlog

secure 사용자의 원격로그인 정보를 기록 /var/log/secure

messages 시스템 운영에 대한 전반적인 메시지, 시스템 데몬들의 실행 내역, 사용자들에 대한 접속 정보, Tcpwrapper에 대한 접근 제어정보

