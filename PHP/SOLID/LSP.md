# LSP ( Liskov Substitution Principle ), 리스코프 치환 원칙

출처 : https://www.youtube.com/watch?v=OfVwuWJSHOY

자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙

타입에 대한 의존성은 아주 지독한 의존성?

OCP

Abstraction, polymorphism(inheritance)를 이용해서 구현

LSP

OCP를 받쳐주는 polymorphism에 관한 원칙을 제공
LSP가 위반되면 OCP도 위반됨
LSP를 위반하면 subtype이 추가될때마다 클라이언트들이 수정되어야 함
instanceof/downcasting을 사용하는 것은 전형적인 LSP 위반의 징조

LSP에 가장 많이 나오는 예제.. 사각형과 정사각형


![20201119134859](https://user-images.githubusercontent.com/6989005/99623668-ed8b5500-2a6f-11eb-8c2b-428eca83d464.png)

![20201119134925](https://user-images.githubusercontent.com/6989005/99623674-ef551880-2a6f-11eb-9c46-218658c4fd05.png)

![20201119135029](https://user-images.githubusercontent.com/6989005/99623660-ea906480-2a6f-11eb-9b20-40b8e6d2ee16.png)


The Representative Rule

대리인은 자신이 대리하는 어떤 것들에 대한 관계까지 대리(공유)하지는 않는다.
이혼 소송 변호사들(대리인)이 이혼하는 부부들의 관계(부부)를 대리(공유)하지 않는 것 처럼
따라서 기하학에 따르면 Square IS-A Rectangle이지만 이들을 표현/대리(represent)하는
SW는 그들의 관계(IS-A)를 공유하지 않는다.

