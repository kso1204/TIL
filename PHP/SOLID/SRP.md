# SRP (Single Responsibility Principle), 단일 책임 원칙

출처 : https://www.youtube.com/watch?v=AdANHDp5dTM // 클린 코더스 강의 SRP

작성된 클래스는 하나의 책임(기능)만을 가지며 클래스가 제공하는 모든 서비스는 그 하나의 책임을 수행하는데 집중 되어야 한다.

디자인 패턴 : Factory Method,

클래스가 가지고 있는 메소드 중

책임 SW의 변경을 요청하는 특정 사용자들에 대해 클래스/함수가 갖는 것

변경의 원인이 같은 애들은 같은 책임이다.

누가 해당 메소드의 변경을 유발하는 사용자인가..?

User가 특정 Role을 수행할 때 Actor라고 부른다.

- 책임은 개인이 아니라 액터와 연결

Employee 클래스에는 3개의 액터가 있다.

- Policy, Architect, Operations


![20201119104046](https://user-images.githubusercontent.com/6989005/99613223-84e5ad80-2a5a-11eb-82ff-b89dbc82f38e.png)

책임 - 특정 액터의 요구사항을 만족시키기 위한 일련의 함수의 집합

Actor의 요구사항 변경이 일련의 함수들의 변경의 근원이 된다.

Primary and Seconday Values

Secondary value of SW is it's behaivor

현재의 sw가 현재 사용자의 현재 요구사항을 만족하는 가?

Primary value of SW

- 지속적으로 변화하는 요구사항을 수용(tolerate, facilitate)하는 것
- 대부분의 SW의 경우 현재 요구사항을 잘 만족하지만 변경하긴 어렵다.

모듈은 하나/반드시 하나의 변경사유를 가져야 한다.

One and only one responsibility

-동일한 이유로 변경되어야 하는 것들은 동일 모듈에,

-다른 이유로 변경되어야 하는 것들은 다른 모듈에

시스템 설계를 할 때 SRP를 잘 사용하기 위해서는 Actor 파악에 주의해야 한다. (UseCase)

의존성 역전

- 클래스를 인터페이스와 클래스로 분리
- Actor를 클래스에 Decouple
- 모든 Actor들이 하나의 인터페이스에 coupled
- 하나의 클래스에 구현되어 구현도 coupled

![20201119110050](https://user-images.githubusercontent.com/6989005/99613230-86af7100-2a5a-11eb-8339-6c3ce165ac8d.png)

Extract Classes

3개의 책임을 분리하는 방법: 3개의 클래스로 분리

Actor들은 분리된 3개의 클래스에 의존

3개의 책임에 대한 구현은 분리

하나의 책임의 변경에 다른 책임에 영향 안미침

transitive dependency(EmployeeGateWay/EmployeeRepoter->Employee)

Employee의 개념이 3개의 조각으로 분리되고 Employee의 변경으로 인해 영향을 미칠 수 있다.

![20201119110130](https://user-images.githubusercontent.com/6989005/99613235-86af7100-2a5a-11eb-979d-c0c15c4527ba.png)


Facade - 어디에 구현이 있는지 찾기 쉽게?

![20201119111009](https://user-images.githubusercontent.com/6989005/99613236-87480780-2a5a-11eb-914d-04958e61791a.png)

Interface Segregation

![20201119111029](https://user-images.githubusercontent.com/6989005/99613237-87e09e00-2a5a-11eb-91b5-2341667a4e1d.png)

![20201119112302](https://user-images.githubusercontent.com/6989005/99613238-87e09e00-2a5a-11eb-9608-31020046d303.png)

