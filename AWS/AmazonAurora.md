# AmazonAurora

1. https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html

2. https://notemusic.tistory.com/69

3. mysql의 경우 read replica도 binlog를 받아서 처리해야 하기 때문에 read 뿐만 아니라 write도 같이 처리해야하는 단점이 있는데,

4. 오로라의 경우 replica가 binlog를 읽어서 싱크를 맞추는 것이 아니라 redo log를 받아서 동기화하기 때문에 read에만 집중 가능하다.