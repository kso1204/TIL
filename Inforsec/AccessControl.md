# AccessControl

MAC 허용등급과 자료범위를 비교해 권한 부여
정책은 경직되고 구현은 어렵다 (방화벽)

DAC 객체의 소유자는 주체의 신분에 따라 임의적으로 접근을 통제
구현이 쉽고 유연하며 사례는 ACL

RBAC 주체와 객체사이의 역할에 따라 접근 통제
MAC와 DAC의 약점을 보완하여 인사이동이 잦은 경우도 관리 용이

기밀성 : BLP (벨라파듈라 모델)

No write Down, No read up

상위 등급이 하위 등급에 쓸 경우 기밀성 침해

주체(사용자)보다 보안 수준(Security Level)이 높은 객체(ex,문서 등)에 대한 읽기를 허용하지 않는 속성을 말한다.

주체(사용자)보다 보안 수준(Security Level)이 낮은 객체(ex,문서 등)에 대한 쓰기를 허용하지 않는 속성을 말한다.

이를 통해 보안 수준이 높은 주체가 보안 수준이 낮은 객체에 대한 쓰기를 통해 정보가 유출되어 기밀성이 훼손되는 상황을 방지할 수 있다.

무결성 : Biba (비바)

No read down, no write up

하위 등급이 상위 등급을 읽을 수 있으면 무결성 침해

주체(사용자)보다 무결성 수준(Intergrity Level)이 높은 객체(ex,문서 등)에 대한 쓰기를 허용하지 않는 속성을 말한다.

이를 통해 무결성 수준이 높은 객체의 정보가 무결성 수준이 낮은 주체의 쓰기에 의해 손상되어 무결성이 훼손되는 상황을 방지할 수 있다.

