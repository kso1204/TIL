# SOLID

출처 : https://www.youtube.com/watch?v=SaycTFHwpYQ

* SOLID

    * [SRP](https://github.com/kso1204/TIL/blob/main/PHP/SOLID/SRP.md) 단일 책임 원칙
    * [OCP](https://github.com/kso1204/TIL/blob/main/PHP/SOLID/OCP.md) 개방 폐쇄 원칙
    * [LSP](https://github.com/kso1204/TIL/blob/main/PHP/SOLID/LSP.md) 리스코프 치환 원칙
    * [ISP](https://github.com/kso1204/TIL/blob/main/PHP/SOLID/ISP.md) 인터페이스 분리 원칙
    * [DIP](https://github.com/kso1204/TIL/blob/main/PHP/SOLID/DIP.md) 의존 역전 원칙


Use Case - 시스템이 가지는 주요 기능
Entity List - 데이터 모델

![20201119164537](https://user-images.githubusercontent.com/6989005/99636654-0d7a4300-2a87-11eb-8eff-254b464ccc9c.png)

![20201119164751](https://user-images.githubusercontent.com/6989005/99636650-0bb07f80-2a87-11eb-8d09-0b9098602df4.png)

SRP로 시작

누가 어플리케이션의 액터인가?! 그들의 관심사는?

목적
- 모듈들을 분리하는 것
- 각 모듈은 반드시 하나의 액터만 담당해야 한다.

![20201119165346](https://user-images.githubusercontent.com/6989005/99637665-88902900-2a88-11eb-9e5d-eb2897d7c9e6.png)

두 개의 Actor가 하나의 모듈을 가르킬 때 어떻게 해야 하는가?

![20201119165428](https://user-images.githubusercontent.com/6989005/99637658-86c66580-2a88-11eb-9e0f-f1bacf3337c1.png)

한 모듈이 하나의 Actor를 위한 Responsibility를 갖도록 분리하는 설계를 하는 것이 의미를 가짐

Actor를 찾고 이에 기반하여 Module을 분리한다!

OCP

OCP는.. 기본적으로 펑션을 바로 잡는게 아니고 인터페이스를 거친다.

![20201119170110](https://user-images.githubusercontent.com/6989005/99640354-1c172900-2a8c-11eb-85e1-d7c8b446600c.png)


LSP

인터페이스가 아무것도 안하도록 override하는 것은 LSP 위반..

![20201119172536](https://user-images.githubusercontent.com/6989005/99640462-41a43280-2a8c-11eb-94a5-e5b5c78dd1f8.png)

Downcast란? 상위 클래스로 선언 된 내용을 하위 클래스로 재 지정 하는 것? (Hourly)

ISP

![20201119171843](https://user-images.githubusercontent.com/6989005/99640381-2507fa80-2a8c-11eb-82b4-d613885d5837.png)


DIP

최종..?

![20201119172119](https://user-images.githubusercontent.com/6989005/99640397-2afddb80-2a8c-11eb-87a7-cefdbdd737bc.png)

![20201119172146](https://user-images.githubusercontent.com/6989005/99640402-2cc79f00-2a8c-11eb-960b-85ce95c45586.png)
