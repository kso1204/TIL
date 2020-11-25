# Snort

alert tcp any any -> any 80 (msg:"경고메세지"; content:/"GET \ HTTP\ 1./"; nocase; offset:0; sid:10000001; threshold:type
treshold, track_src, count 10, seconds 1;)

1. snort의 action 중 차단과 로그를 남기는 action 두 가지
2. 해당 content를 처음 위치에서 13byte만 확인하여 매칭하는 옵션 작성
3. 해당 rule에서의 threshold 동작은 어떻게 이뤄지는가

1) Drop, Reject
2) Depth 13;
3) 동일한 출발지에 1초에 10번오는 패킷을 탐지하여 10번째마다 alert 함