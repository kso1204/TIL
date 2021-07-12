# 서버 에러 발생 케이스 정리

# 7월3일 오후 11시 35분 경 로드밸런스로 연결되어 있는 인스턴스가 하나 사망하면서 504 에러가 발생했다.

1. 결국에는 아파치 재시작으로 해결했는데, 상세한 원인은 당시에 파악하지 못해서 네오텍을 통해 AWS로 문의

2. 네오텍과 AWS에서 데이터를 주고 받으면서 모니터링 결과를 봤는데, CPU사용률이 갑자기 떨어지면서 서버가 작동하지 않았고,

3. 이 이유에 대해서는 인스턴스 문제가 아닌 내부 어플리케이션 타임아웃으로 인해 발생했다고 알려줌.

4. 해당 내용을 확인하기 위해 라라벨 로그와 access log, error_log를 확인 중인데 마땅한 내용이 나오지 않고 있음.

```

Debian / Ubuntu Linux Apache error log file location – /var/log/apache2/error.log

grep ErrorLog /etc/apache2/apache2.conf

```
5. AccessLog에서는 별다른 로그를 확인 할 수 없었고 dummy connection 부분만 존재했다.

6. errorLog에서는 

```

[Sat Jul 03 06:25:38.257456 2021] [mpm_prefork:notice] [pid 28656] AH00163: Apache/2.4.18 (Ubuntu) configured -- resuming normal operations
[Sat Jul 03 06:25:38.257471 2021] [core:notice] [pid 28656] AH00094: Command line: '/usr/sbin/apache2'
[Sat Jul 03 11:38:32.115721 2021] [core:error] [pid 5481] [client 172.31.2.177:59858] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.129449 2021] [core:error] [pid 13656] [client 172.31.28.5:41774] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.139188 2021] [core:error] [pid 5576] [client 172.31.28.5:41504] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.167752 2021] [core:error] [pid 9802] [client 172.31.2.177:60012] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.168822 2021] [core:error] [pid 11592] [client 172.31.28.5:41034] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.228476 2021] [core:error] [pid 9921] [client 172.31.2.177:60268] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.350945 2021] [core:error] [pid 9913] [client 172.31.2.177:60106] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.353594 2021] [core:error] [pid 12709] [client 172.31.28.5:41422] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 11:38:32.355999 2021] [core:error] [pid 5481] [client 172.31.2.177:59858] AH00082: an unknown filter was not added: jsminify
[Sat Jul 03 12:18:49.734329 2021] [php7:warn] [pid 2970] [client 172.31.2.177:49528] PHP Warning:  POST Content-Length of 55986108 bytes exceeds the limit of 52428800 bytes in Unknown on line 0
[Sat Jul 03 13:53:20.637116 2021] [core:notice] [pid 28656] AH00051: child pid 6668 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.637775 2021] [core:notice] [pid 28656] AH00051: child pid 9919 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.705726 2021] [core:notice] [pid 28656] AH00051: child pid 18074 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.708292 2021] [core:notice] [pid 28656] AH00051: child pid 18388 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.750337 2021] [core:notice] [pid 28656] AH00051: child pid 12988 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.756369 2021] [core:notice] [pid 28656] AH00051: child pid 7300 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.761309 2021] [core:notice] [pid 28656] AH00051: child pid 818 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.762845 2021] [core:notice] [pid 28656] AH00051: child pid 318 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.763038 2021] [core:notice] [pid 28656] AH00051: child pid 18368 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.769830 2021] [core:notice] [pid 28656] AH00051: child pid 26560 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.773356 2021] [core:notice] [pid 28656] AH00051: child pid 20840 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.775715 2021] [core:notice] [pid 28656] AH00051: child pid 16471 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.776000 2021] [core:notice] [pid 28656] AH00051: child pid 21120 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.896326 2021] [core:notice] [pid 28656] AH00051: child pid 2793 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.896524 2021] [core:notice] [pid 28656] AH00051: child pid 10311 exit signal Segmentation fault (11), possible coredump in /etc/apache2
[Sat Jul 03 13:53:20.918143 2021] [core:notice] [pid 28656] AH00051: child pid 10459 exit signal Segmentation fault (11), possible coredump in /etc/apache2

```

7. ELB에서 CPU 사용률이 급격하게 떨어지면서, ALB 5XX (504)에러 카운트가 급격하게 증가했고, TargetResponseTime이 급격하게증가했다.

8. 해당 로그를 확인해봐도 별 이상이 없어서 네오텍에 다시 문의한 결과

9. ELB 타임아웃이 200으로 설정되어 있으니 서버 설정은 이것보다 커야 한다는 것..해서 MaxKeepAliveTimeout이 15로 되어 있는데, 이 부분을 수정해야 한다는 것인지 문의했다.

- KeepAlive에 대한 설명 

- /etc/apache2/apache2.conf

- https://kamang-it.tistory.com/entry/Web%EC%84%9C%EB%B2%84%EC%99%80%EC%9D%98-%EC%97%B0%EA%B2%B0%EC%9D%84-%EA%B3%84%EC%86%8D-Keep-Alive

- 아파치 또는 Nginx를 ELB의 백엔드 서버로 사용하기 위한 최적의 설정은? 

- https://aws.amazon.com/ko/premiumsupport/knowledge-center/apache-backend-elb/

- 아파치 설정파일을 수정했을 때 재시작하지 않고 설정만 변경하는 방법

- http://urin79.com/blog/20654918

- 로드밸런스 연결 유휴 제한 시간 확인하기

- 로드밸런스 들어가서 해당 로드밸런스 클릭한 다음 설명에서 밑으로 내리면 속성이 있다 해당 속성에 유휴 제한 시간 200 초로 설정되어 있음

- AWS 504에러에 대한 글

- https://pearlluck.tistory.com/128

10. 


11. Keep-Alive 아이들 타임 세션이 200인데, 서버쪽은 짧으면 

12. 504에러 메시지 게이트웨이 타겟 

13. 시간안에 응답

14. ALB 액세스로그 

15. 어플리케이션 내부 구조 

16. ALB액세스 로그를 확인해라

17. 클라이언트가 어떤 URL 패스를 던졌는데 백엔드 응답이 504가 오더라

18. 로그를 분별하는 방법

19. CSV 파일로 로그가 떨어지는데, 전부 받으면 안되고

20. AWS에서 아테나 서비스 -> S3에 

21. 찾아보는 팁 - 구글에다가 -> ALB ACCESS LOG ATENA라고 치면

22. https://docs.aws.amazon.com/ko_kr/athena/latest/ug/application-load-balancer-logs.html

23. 아테나 같은 경우에는 쿼리 요청당 비용이 있어서 