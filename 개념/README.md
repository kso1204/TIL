# 한번 더 개념 정리

# 의존성 주입 (DI)

1. https://mangkyu.tistory.com/150

# 스프링에서 사용하는 Application Context

1. https://mangkyu.tistory.com/151

# 스프링 빈?

1. https://velog.io/@gillog/Spring-Bean-%EC%A0%95%EB%A6%AC

# static 변수와 static 메소드

1. https://mangkyu.tistory.com/47?category=872426

- static은 객체의 생성 없이 접근, static을 선언하지 않은 변수는 new를 통해 새로운 heap(메모리) 영역에 할당

- static은 모든 메모리가 공유하는 영역에 있다 (static영역)

# REST API

1. https://mangkyu.tistory.com/46?category=925341

- Resource

- Method

- Representation of Resource (json(자바스크립트 데이터 오브젝트))

# 서버 기반 인증시스템 VS 토큰 기반 인증 시스템

1. https://mangkyu.tistory.com/55?category=925341

# JWT

1. https://mangkyu.tistory.com/56

# SHA, RSA, AES

1. https://stage-loving-developers.tistory.com/23

- 암호화 - 공개키, 복호화 - 개인키

- SHA - 단방향 해싱, RSA - 비대칭키 암호화 방식 (공개키 != 개인키), AES - 대칭키 암호화 방식 (공개키 = 개인키)

# Cache

1. https://mangkyu.tistory.com/69?category=925341

- 캐시는 Cache Hit, Cache miss, Long Tail의 주요 키 포인트

- Long Tail이란 상위 20%의 요구가 리소스의 대부분을 사용하는 것

# SQL 고급 

1. https://mangkyu.tistory.com/25?category=761304

# 트랜잭션, 동시성 제어, 회복

1. https://mangkyu.tistory.com/25?category=761304

- 트랜잭션이란 DBMS에서 데이터를 다루는 논리적인 작업의 단위

- Commit이란 트랜잭션의 수행이 완료됨을 트랜잭션 관리자에게 알려 주는 연산

- 트랜잭션은 전체가 수행되거나 또는 전혀 수행되지 않아야 한다.(All or Nothing)

- 
# Stream API

1. https://mangkyu.tistory.com/112

2. 람다식이란? 함수를 하나의 식으로 표현한 것 

3. 함수를 람다식으로 표현하면 메소드의 이름이 필요 없기 때문에, 람다식은 익명 함수의 한 종류라고 볼 수 있다.

4. 함수형 인터페이스의 인스턴스를 생성하여 함수를 변수처럼 사용하는 람다식  

5. 장점 -> 함수를 만드는 과정없이 한번에 처리할 수 있어 생산성이 높아진다.

6. 병렬프로그래밍이 용이하다.

7. 단점 -> 람다를 사용하면서 만든 익명함수는 재사용이 불가능하다.

8. 디버깅이 어렵다.

9. 람다를 남발하면 비슷한 함수가 중복 생성되어 코드가 지저분해질 수 있다.

10. 함수형 인터페이스란? 함수를 1급 객체처럼 다룰 수 있는 어노테이션으로, 인터페이스에 선언하여 단 하나의 추상 메소드만을 갖도록 제한하는 역할

11. Java에서 제공하는 함수형 인터페이스 네 가지

- Supplier<\T>

- 매개변수 없이 반환값 만을 갖는 함수형 인터페이스이다.

- T get()을 추상메소드로 가지고 있다.

- Consumer<\T>

- Function<\T,R>

- Predicate<\T>

- 내용이 너무 어려워서 복습이 필요해보임; https://mangkyu.tistory.com/113

# 디자인 패턴

1. 생성 패턴

- 팩토리 패턴 - 객체를 생성하기 위한 디자인 패턴

- 추상 팩토리 패턴 - 객체를 생성하는 팩토리를 생성하기 위한 디자인 패턴

- 빌더 패턴 - 상황에 따라 동적인 인자를 필요로 하는 객체를 생성하기 위한 디자인 패턴

- 싱글톤 패턴 - 객체를 1개만 생성하여 항상 참조가능하도록 고안된 디자인 패턴

2. 구조 패턴

- 어댑터 패턴 - 호환성이 맞지 않는 두 클래스를 연결하여 사용하기 위한 디자인 패턴

- 프록시 패턴 - 어떤 객체에 접근하기 위해 대리인을 사용하는 패턴

- 퍼사드 패턴 - 어떤 복합적인 기능에 대해 간략화된 인터페이스를 제공하는 디자인 패턴

3. 행위 패턴

- 전략 패턴 - 상황에 따라 다른 전략을 사용하기 위한 디자인 패턴

- 옵저버 패턴 - 값을 관찰하여 빠르게 반영하기 위한 디자인 패턴

- 커맨드 패턴 - 실행될 기능을 캡슐화하여 재사용성이 높은 클래스를 설계하기 위한 디자인 패턴

# 가상화

1. https://mangkyu.tistory.com/86

2. 가상화란 가상화를 관리하는 소프트웨어(주로 HyperVisor)를 사용하여 하나의 물리적 머신에서 가상 머신(VM)을 만드는 프로세스이다.

3. 가상 머신은 물리적 머신과 동일한 역할 및 성능을 수행하지만, cpu와 메모리 및 스토리지와 같은 물리적 머신의 컴퓨팅 리소스를 사용한다.

4. HyperVisor는 필요에 따라 각 가상 머신에 이러한 컴퓨팅 리소스를 할당한다.

5. 최근에는 Docker와 같은 컨테이너 가상화 기술이 등장하기도 하였다. 도커를 윈도우에서 사용하는 경우에는 HyperVisor를 사용하지만,

6. 리눅스에서 사용하는 상황에서는 커널의 특징을 이용하기 때문에 HyperVisor를 사용하지 않는다.

7. 가상화를 이용하면 서버를 통합하고 서버의 자원을 최대한으로 활용함으로써 서버 급증 문제를 해결할 수 있다.