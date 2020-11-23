# DIP ( Dependency Inversion Principle ), 의존 역전 원칙

출처 : https://www.youtube.com/watch?v=mI1PsrgogCw&t=1s

객체들이 서로 정보를 주고 받을 때 의존 관계가 형성되는데,
이 때 객체들은 나름대로의 원칙을 갖고 정보를 주고 받아야 한다는 설계 원칙입니다.

상위레벨의 정책은 하위레벨의 상세함에 의존하면 안된다..
둘은 Abstract Type에 의존해야 한다

![20201119141522](https://user-images.githubusercontent.com/6989005/99634622-23d2cf80-2a84-11eb-84ce-e2a582a5c3d7.png)

상속에 대한 재사용은 객체지향의 핵심은 아니다.
IoC를 통해 상위 레벨의 모듈을 하위레벨의 모듈로부터 보호하는 것
-Why? 하위레벨은 빈번하게 변경되기 때문에..

객체지향의 핵심은 의존성 관리다!

구조적 설계

B의 구체적인 변경으로부터 A를 보호하는 것 (객체지향 + 의존 역전 + 맨날 나오는 패턴)

Application에서 나가는 방향이 없고. WEB이랑 Database가 다 Application을 향하고 있다.

![20201119162633](https://user-images.githubusercontent.com/6989005/99634617-22a1a280-2a84-11eb-8f60-ad8fd60e1c3e.png)

이게 DIP의 구조

OCP와 DIP의 차이점은

OCP는 확장을 위해 DIP는 Low-Level의 의존성을 갖는 부분을 Abstraction한다?



