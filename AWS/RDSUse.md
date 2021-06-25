# RDS Use

1. https://develop-im.tistory.com/13

2. rds 생성 할 때 클러스트 보안 그룹 설정

3. 클러스트 내부 인스턴스 퍼블릭 액세스 허용

4. dev3-instance-1 쓰기	Aurora MySQL	ap-northeast-2a	db.r5.large	수정 중

5. 위에 문제가 됐던 부분을 해결했는데 RDS 연결이 되지 않았던 이유는.. 

6. 해당 VPC에 대한 서브넷 그룹을 설정하는 부분이 있었는데, 보안그룹 말고

7. 이 부분을 private rds 그룹으로 설정해서 외부 ip 접근을 아예 막아버렸다.

8. 해당 부분을 default (public) 설정으로 변경하여 문제 해결