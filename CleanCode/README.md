# 클린 코드

1. 깨끗한 코드

- 중복을 피하라, 한기능만 수행하라, 제대로 표현하라, 작게 추상화하라
- 캠프장은 처음 왔을 때보다 더 깨끗하게 해놓고 떠나라
- 변수 이름 하나를 개선하고, 조금 긴 함수 하나를 분할하고, 약간의 중복을 제거하고, 복잡한 if 문 하나를 제거하라


2. 의미 있는 이름

- 접두어는 옛날에 작성한 구닥다리 코드
- 클래스이름은 명사나 명사구, 메서드 이름은 동사나 동사구 deletePage, getName ..
- 한 개념에 한 단어를 사용해라
- 기술 개념에는 기술 이름이 가장 적합한 이름이다.

3. 함수

- 작게 만들어라
- 더 작게 만들어라
- 함수에서 들여쓰기 수준은 1단이나 2단을 넘어가면 안 된다. 즉 중첩 구조가 생길만큼 크면 안 된다.
- 함수는 한 가지를 해야 한다. 그 한 가지를 잘해야 한다. 그 한 가지만을 해야 한다.
- 함수당 추상화 수준은 하나로 (한 함수가 하는일이 근본개념인지? 세부사항인지? 구분해야 한다.)
- 코드는 위에서 아래로 이야기처럼 읽히고, 한 함수 다음에는 추상화 수준이 한 단계 낮은 함수가 와야한다.
- switch 문은 작게 만들기 어렵기 때문에.. abstract factory에 꽁꽁 숨긴다??
- 서술적인 이름을 사용하라
- 함수 인수는 2개 이하로 사용.. 가능한 한 무항, 한 개
- 플래그 인수는 끔찍하다.
- 명령과 조회를 분리하라
- 오류 코드보다 예외를 사용하라
- try/catch 블록은 원래 추하기 때문에, 각 블록을 별도 함수로 뽑아내야 한다.

```

try {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
} catch (Exception e) {
    logger.log(e.getMessage());
}

를

public void delete(Page page) {
    try {
        deletePageAndAllReferences(page);
    } catch (Exception e) {
        logError(e);
    }
}

private voide deletePageAndAllReferences(Page page) throws Exception {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
}

private void logError(Exception e) {
    logger.log(e.getMessage());
}

```

- 반복하지 마라, 중복은 소프트웨어에서 모든 악의 근원이다.
- 구조적 프로그래밍, 함수는 return 문이 하나여야 한다.
- 소프트웨어를 짜는 행위는 글짓기와 비슷하다.
- 처음에는 길고 복잡하다. 들여쓰기 단계도 많고 중복된 루프도 많다. 인수 목록도 아주 길다. 이름은 즉흥적이고 코드는 중복된다.
- 하지만 단위 테스트 케이스를 만들고 코드를 다듬고, 함수를 만들고, 이름을 바꾸고, 중복을 제거하고, 메서드를 줄이고, 전체 클래스를 쪼개고, 순서를 바꾼다.

4. 주석

- 부정확한 주석은 아예 없는 주석보다 훨씬 더 나쁘다
- 주석은 나쁜 코드를 보완하지 못한다.
- 주석으로 달려는 설명을 함수로 만들어 표현해도 충분하다.
- 정말로 좋은 주석은, 주석을 달지 않을 방법을 차아낸 주석이다.

```
// 테스트 중인 Responder 인스턴스를 반환한다.
protected abstract Responder responderInstance();

protected abstract Responder responderBeingTested();
```

- 주석으로 처리된 코드는 다른 사람들이 지우기를 주저한다. 
- 하지만 우리는 오래전부터 우수한 소스 코드 관리 시스템을 사용해왔다. 코드를 그냥 삭제해라

5. 형식 맞추기

- 신문 기사처럼 작성하라. 이름은 간단하면서도 설명이 가능하게 짓는다.
- 개념은 빈 행으로 분리하라
- 줄바꿈이 개념을 분리한다면 세로 밀집도는 연관성을 의미한다.
- 변수는 사용하는 위치에 최대한 가까이 선언한다.
- 인스턴스 변수는 클래스 맨 처음에 선언한다.
- 종속함수. 한 함수가 다른 함수를 호출한다면 두 함수는 세로로 가까이 배치한다. 또한 가능하다면 호출하는 함수를 호출되는 함수보다 먼저 배치한다.
- 개념적 유사성 


6. 객체와 자료구조

- 자료 추상화. 자료를 세세하게 공개하기보다는 추상적인 개념으로 표현하는 편이 좋다.
- 개발자는 객체가 포함하는 자료를 표현할 가장 좋은 방법을 심각하게 고민해야 한다.
- 자료/객체 비대칭
- 객체는 추상화 뒤로 자료를 숨긴 채 자료를 다루는 함수만 공개한다.
- 자료구조는 자료를 그대로 공개하며 별다른 함수는 제공하지 않는다.
- 객체와 자료구조는 상호 보완적인 특질이 있기 때문에, 사실상 반대이고 객체와 자료 구조는 근본적으로 양분된다.
- 자료구조를 사용하는 절차적인 코드는 기존 자료구조를 변경하지 않으면서 새 함수를 추가하기 쉽다.
- 반면, 객체 지향 코드는 기존 함수를 변경하지 않으면서 새 클래스를 추가하기 쉽다.
- 객체 지향 코드에서 어려운 변경은 절차적인 코드에서 쉬우며, 절차적인 코드에서 어려운 변경은 객체 지향 코드에서 쉽다.
- 복잡한 시스템을 짜다 보면 새로운 함수가 아니라 새로운 자료 타입이 필요한 경우가 생긴다. 이때는 클래스와 객체 지향 기법이 가장 적합하다.
- 반면, 새로운 자료 타입이 아니라 새로운 함수가 필요한 경우도 생긴다. 이때는 절차적인 코드와 자료 구조가 좀 더 적합하다.
- 디미터 법칙. 디미터 법칙은 잘 알려진 휴리스틱으로, 모듈은 자신이 조작하는 객체의 속사정을 몰라야 한다는 법칙.
- 객체는 자료를 숨기고 함수를 공개한다. 객체는 조회 함수로 내부 구조를 공개하면 안 된다는 의미다.
- 자료 전달 객체. 자료 구조체의 전형적인 형태는 공개 변수만 있고 함수가 없는 클래스다. 이런 자료 구조체를 때로는 자료 전달 객체라 한다. (DTO)
- 결론. 객체는 동작을 공개하고 자료를 숨긴다. 그래서 기존 동작을 변경하지 않으면서 새 객체 타입을 추가하기는 쉬운 반면, 기존 객체에 새 동작을 추가하기는 어렵다.
- 자료구조는 별다른 동작 없이 자료를 노출한다. 그래서 기본 자료에 새 동작을 추가하기는 쉬우나, 기존 함수에 새 자료 구조를 추가하기는 어렵다.
- 어떤 시스템을 구현할 때, 새로운 자료 타입을 추가하는 유연성이 필요하면 객체가 더 적합하다.
- 다른 경우로 새로운 동작을 추가하는 유연성이 필요하면 자료 구조와 절차적인 코드가 더 적합하다.

7. 오류 처리

- 오류 코드보다 예외를 사용하라. 오류가 생기면 예외를 던져라
- Try-Catch-Finally 문부터 작성해라
- 호출자를 고려해 예외 클래스를 정의하라.

오류를 형편없이 분류한 사례

```

ACMEPort port = new ACMEPort(12);

try {
    port.open();
} catch (DeviceResponseException e) {
    reportPortError(e);
    logger.log("Device response exception", e);
} catch (ATMlockedException e) {
    reportPortError(e);
    logger.log("Unlock exception", e);
} catch (GXEerror e) {
    reportPortError(e);
    logger.log("Device response exception");
} finally {
    ...
}

코드를 간결하게 고쳐보기

LocalPort port = new LocalPort(12);

try {
    port.open();
} catch (ProtDeviceFailure e) {
    reportError(e);
    logger.log(e.getMessage(), e);
} finally {
    ...
}

여기서 LocalPort 클래스는 단순히 ACMEPort 클래스가 던지는 예외를 잡아 변환하는 감싸기 클래스일 뿐이다.

public class LocalPort {
    private ACMEPort innerPort;

    public LocalPort(int portNumber) {
        innerPort = new ACMEPort(portNumber);
    }
}

public void open() {
    try {
        innerPort.open();
    } catch (DeviceResponseException e) {
        throw new PortDeviceFailure(e);
    } catch (ATMUnlockedException e) {
        throw new PortDeviceFailure(e);
    } catch (GMXerror e) {
        throw new PortDeviceFailure(e);
    }
}

```

LocalPort 클래스처럼 ACMEPort를 감싸는 클래스는 매우 유용하다.

실제로 외부 API를 사용할 때는 감싸기 기법이 최선이다.

외부 API를 감싸면 외부 라이브러리와 프로그램 사이에서 의존성이 크게 줄어든다.

- 정상 흐름을 정의하라 

비용 청구 애플리케이션에서 총계를 계산하는 허술한 코드

```

try {
    MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
    m_total += expenses.getTotal();
} catch (MealExpensesNotFound e) {
    m_total += getMealPerDiem();
}

식비를 비용으로 청구했다면 직원이 청구한 식비를 총계에 더한다.

식비를 비용으로 청구하지 않았다면 일일 기본 식비를 총계에 더한다.

예외가 논리를 따라가기 어렵게 만든다.

특수 상황을 처리할 필요가 없다면 더 좋지 않을까?

MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
m_total += expenses.getTotal();

위처럼 간결한 코드가 가능할까?

ExpensesReportDAO를 고쳐 언제나 MealExpense 객체를 반환한다.

청구한 식비가 없다면 일일 기본 식비를 반환하는 MealExpense 객체를 반환한다.

public class PerDiemMealExpenses implements MealExpenses {
    public function getTotal() {
        // 기본값으로 일일 식비를 반환한다.
    }
}

```

- null을 반환하지 마라
- null을 전달하지 마라

8. 경계

- 시스템에 들어가는 모든 소프트웨어를 직접 개발하는 경우는 드물다.
- 외부 코드 사용하기
- 인터페이스 제공자와 인터페이스 사용자 사이에는 특유의 긴장이 존재한다.
- 패키지 제공자나 프레임워크 제공자는 적용성을 최대한 넓히려 애쓰고, 사용자는 자신의 요구에 집중하는 인터페이스를 바란다.

ex) JAVA.utils.map

- map 사용자라면 누구나 map을 지울 권한이 있다.
- map은 객체 유형을 제한하지 않기 때문에 마음만 먹으면 사용자는 어떤 객체 유형도 추가할 수 있다.
- 제네릭스를 사용해서 코드 가용성을 높인다 하더라도, 필요하지 않은 기능까지 제공하는 것은 막을 수 없다.

```
ex) Map<string, Sensor> sensor = new HaspMap<Sensor>();

Sensor S = sensors.get(sensorId);
```

Map을 좀 더 깔끔하게 사용한 코드

Sensor 사용자는 제네릭스가 사용되었는지 여부에 신경 쓸 필요가 없다.

제네릭스의 사용 여부는 Sensor 안에서 결정한다.

```
public class Sensors {
    private Map Sensors = new HashMap();

    public Sensor getById(String id) {
        return (Sensor) sensors.get(id);
    }
}
```

경계 인터페이스인 map을 sensors 안으로 숨긴다. 따라서 map 인터페이스가 변하더라도 나머지 프로그램에는 영향을 미치지 않는다.

제네릭스를 사용하든 하지 않든 더 이상 문제가 안 된다.

sensor 클래스 안에서만 객체 유형을 관리하고 변환하기 때문이다.

또한 sensor 클래스는 프로그램에 필요한 인터페이스만 제공한다.

그래서 코드는 이해하기 쉽고 오용하기 어렵다.

sensors 클래스는 나머지 프로그램이 설계 규칙과 비즈니스 규칙을 따르도록 강제할 수 있다.

- 경계 살피고 익히기
- 곧바로 우리쪽 코드를 작성해 외부 코드를 호출하는 대신 먼저 간단한 테스트 케이스를 작성해 외부 코드를 익힌다.
- 이를 학습 테스트라 부른다.
- 아직 존재하지 않는 코드를 사용하기
- 경계와 관련해 또 다른 유형은 아는 코드와 모르는 코드를 분리하는 경계다.
- 우리가 바라는 인터페이스를 구현하면 우리가 인터페이스를 전적으로 통제한다는 장점이 생긴다.
- 또한 코드 가독성도 높아지고 코드 의도도 분명해진다.
- 우리는 우리가 통제하지 못하며 정의되지도 않은 API에서 controller를 분리했다.

9. 단위 테스트

10. 클래스

11. 시스템

12. 창발성

13. 동시성

14. 점진적인 개선
