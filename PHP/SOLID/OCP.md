# OCP (Open-Closed Principle), 개방-폐쇄 원칙

출처 : https://www.youtube.com/watch?v=dqa-IdafeIE&t=75s

이해가 되지 않거나, 이해가 잘 되거나, 중요하다고 생각하면 사진을 첨부하는데

이번편은 너무 많은 캡쳐를 한 것 같다.

OCP에 대해서 알려주는 내용도 유익했지만..

미래를 볼 수 있는 크리스탈볼이 있지 않는한 처음부터 OCP를 구현하는 것은 불가능하고..

설계단계에서 적당한 ProtoType모델과 적당한 비용의 투자..

사용자의 요구사항이 변경되면 그 모델을 Refactoring 할 수 있도록 하는 Abstract 구성이 핵심이다.

지금까지도 많이 겪었고.. 앞으로도 항상 겪을 수 밖에 없는 문제(Unknown Unknowns)를 좀 당연하게 생각했다면?

기존 소스가 수정될 때 완전히 엎으면서도.. 좀 더 유익하게 Refactoring해볼 수 있었을텐데?..

공장처럼 소스만 수정했던 것 같다.. SRP에서 얘기했던 Secondary Value인 작동을 위해서만 일한 느낌..?

서비스를 일회성으로 사용하다보니 개선에 대해 큰 의의를 가지지 못하게 되었고.. 이게 발전이 더딘 원인이 된 것 같다.

뭔가를 더 배우는 것도 중요하지만 지금까지 있는 내용을 좀 더 단단하게 다지고 ToyProject 했던 내용들도

처음부터 다시 짜봐야겠다.

기존의 코드를 변경하지 않으면서(closed), 기능을 추가할 수 있도록(open) 설계가 되어야 한다는 원칙

상위 레벨의 모듈이 하위 레벨의 의존성을 갖는 경우를 보면

상위 레벨과 그 디테일한 레벨 사이에 Abstract, Interface를 껴넣어서 의존성을 역전 시킨다!?

상위 레벨을 수정하지 않기 위해(Closed), 인터페이스를 추가한다(Open) - 동작 

POS Example

현찰을 받는 경우에 잘 동작
신용카드를 받고자 할때는 확장을 해야함

이런 구현을 할 때 if문을 계속 추가하게 되면 .. 소스가 산으로 간다.

이런 상황을 fragile한 소스라고 하는데, 이것을 가장 피해야 한다

확장을 해야하는 부분을 Abstract, Interface로 나뉘어야 한다.

Checkout 모듈은 interface에 의존하지 그 하위레벨에 의존하지 않는다.

Checkout 모듈은 수정하지 않는다.

OCP를 준수하면 이론적으로 구현은 가능하나, 실용적이지 않다.

메인은 OCP를 준수할 수 없다.

main partition - 메인에는 if else가 없을 수 없기 때문에..?

crystal ball problem - ?? 확장이 필요할만한 모든 것을 인터페이스로 미리 구현하는 것 자체가 불가능하다? 말이 안 된다?

Agile Design

실용적이고, 반응을 하는 방법
가장 좋은 예시법은 은유법(메타포)이다.

변화에 대한 가장 좋은 예측은 변화를 경험하는 것

Agile Designer는 주단위 정도로 간단한 뭔가를 Deliver한다.
고객이 변경을 요구하면 Agile Designer는 코드를 리팩토링해서 그런 종류의 변경을 쉽게 할 수 있도록 Abstraction을 추가한다.
OCP를 준수하도록

사전 설계는 가치있지만, 사전에 너무 상세하게 들어가는 것은 비용낭비 ! 
빨리 자주 Deliver하고, 고객의 요구사항 변화에 기반하여 리팩토링하는 것은 매우 가치 있다.
이럴때 OCP가 진가를 발휘한다.
하지만 간단한 도메인 모델없이 이렇게 진행하면 방향성 없는 혼란한 구조를 유발한다.

설계를 잘 하는 사람이 Agile도 잘하고 TDD도 잘하고 리팩토링도 잘하는 것