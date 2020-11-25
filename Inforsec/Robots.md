# Robots.txt

1. Robots.txt 파일의 용도

 - 검색엔진에서 자동 크롤링 도구에 대하여 접근 허용 여부를 제어하기 위한 파일

2. 설정값의 의미

useragent: yeti
useragent: googlebot

가.allow : /

useragent : googlebot-image

나.disallow : /admin/
다.disallow : /*.pdf$

 - 가. 검색엔진 로봇(yeti, googlebot)에 대하여 root 디렉토리(/)밑의 모든 파일 및 디렉토리의 크롤링을 허용
 - 나. 검색엔진 로봇(googlebot-image)에 대하여 /admin 폴더 크롤링을 허용하지 않음
 - 다. 검색엔진 로봇(googlebot-image)에 대하여 