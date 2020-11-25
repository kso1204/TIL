# Snort

alert tcp any any -> any 80 (msg:"경고메세지"; content:/"GET \ HTTP\ 1./"; nocase; offset:0; sid:10000001; threshold:type
treshold, track_src, count 10, seconds 1;)

1. snort의 action 중 차단과 로그를 남기는 action 두 가지
2. 해당 content를 처음 위치에서 13byte만 확인하여 매칭하는 옵션 작성
3. 해당 rule에서의 threshold 동작은 어떻게 이뤄지는가

1) Drop, Reject
2) Depth 13;
3) 동일한 출발지에 1초에 10번오는 패킷을 탐지하여 10번째마다 alert 함

HeartBleed 취약점 탐지위한 Snort Rule 설정 의미

alert tcp any any <> any 1.[443, 465, 523] (2.content:"\18 03 00\"; depth:3; 3.content:"\01\", distance: 2, within:1;
 4.content:!"\00\"; within: 1; 5.msg: "SSLv3 Malicious Heartbleed Request V2"; 6.sid: 1;

 1. 탐지 대상 포트 번호를 443, 465, 523으로 지정
 2. content에서 첫 3바이트를 검사하여 바이너리 값으로 "18 03 00"이 있는지 검사
 3. 2번이 끝난 위치에서 2바이트 떨어진 위치에서 1바이트를 검사하여 바이너리 값으로 "01"이 있는지 검사
 4. 3번이 끝난 위치에서 바로 1바이트를 검사하여 바이너리 값으로 "00"이 포함되지 않은지 여부를 검사
 5. 1~4의 탐지룰에 모두 매칭이 되는 경우 로그에 "SSLv3 Malicious HeartBleed Request V2"로 기록
 6. 해당 룰의 식별자를 1로 지정

와.. 4번에 !가 포함되어 있지 않다는 것을 잘 봐야 한다고 했는데, 이 문제를 직접 풀고 풀이를 세 번은 봤는데
처음 알았다..  

