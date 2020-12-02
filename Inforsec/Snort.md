# Snort

https://blog.naver.com/PostView.nhn?blogId=stereok2&logNo=221984313061&parentCategoryNo=25&categoryNo=29&viewDate=&isShowPopularPosts=false&from=postView

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

alert any any -> any 80 (msg "XSS";content:"GET";offset:1;depth:3;content:"/login.php<scrip>XSS";distance:1;)

1. content:"GET"; offset:1; depth:3의 의미? 
2. content:"/login.php<scrip>XSS";distance 1;
3. 바이너리로 전송된 패킷(L이 대문자)을 참고하여 위의 룰로 탐지 안될 경우 어떻게 수정해야 하는지 기술

1. 전송된 패킷의 처음 1바이트를 띄고 3바이트를 검사해서 GET을 찾으라는 의미
2. 이전메시지를 찾은 위치에서 1바이트를 띄고 content안에 기술된 문자열을 찾으라는 의미
3. offset을 0으로 수정하거나 삭제하고 nocase 옵션 추가 or Login으로 수정


alert tcp any any -> any 22 (msg:"SSH Brute force login"; content:"SSH-2.0"; nocase; threshold:type both, track by_src,count 3,seconds 30;sid:1000110;)


Type 은 both, limit, threshold 3개 중 하나를 지정할 수 있습니다.
both라고 지정한 경우 seconds 뒤에 지정된 시간동안 count 뒤에 지정한 횟수에 해당하는 이벤트가 발생 시 한번 action을 수행합니다.

limit : 매 s초 동안 c번째 이벤트까지 action을 수행한다.
ex) threshold type limit, track by_src, count 2, seconds 10
출발지 ip를 기준으로 매10초 동안 2번째 이벤트까지 action을 수행한다.

threshold : 매 s초 동안 c번째 이벤트마다 action을 수행한다.
ex) threshold type threshold, track by_src, count 10, seconds 5
출발지 ip를 기준으로 매5초동안 10번째 이벤트마다 action을 수행한다.

both : 매 s초 동안 c번째 이벤트 시 한번 action을 수행한다.
ex) threshold type both, track by_src, count 10, seconds 1
출발지 ip를 기준으로 매1초 동안 10번째 이벤트 시 한번 action을 수행한다.



