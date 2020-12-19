#  ISP ( Interface Segregation Principle ), 인터페이스 분리 원칙

출처 : https://www.youtube.com/watch?v=IIrjI7YUw6g

자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다는 설계 원칙

One Interface for a sub system

인터페이스를 각 클래스(클라이언트)에 맞게 Actor에 맞게 분리해버린다.

ISP의 방향성을 나타내는 그림

![20201119135701](https://user-images.githubusercontent.com/6989005/99623571-c16fd400-2a6f-11eb-9d8b-56ba6a2e3041.png)

![20201119135731](https://user-images.githubusercontent.com/6989005/99623575-c2a10100-2a6f-11eb-8a09-fd1e06ff6548.png)

Fat class를 만나면

interface를 생성하여 Fat class를 클라이언트로부터 isolate시켜야한다.

interface는 구현체보다는 클라이언트와 논리적으로 결합되므로 클라이언트가 호출하는 메소드만

Interface에 정의되었다는 것을 확신할 수 있음 (ISP 준수)

특정 Interface의 변경으로 인한 다른 클라이언트 영향 없애서

- 재컴파일/재배포 없앰
- 클라이언트들을 다른 독립된 컴포넌트에 배치할 수 있고 (클라이언트+interface가 배치 단위)
- 독립적으로 배포 가능함