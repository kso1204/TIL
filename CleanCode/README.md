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

- TDD 법칙 세 가지
- 첫째 : 실패하는 단위 테스트를 작성할 때까지 실제 코드를 작성하지 않는다.
- 둘째 : 컴파일은 실패하지 않으면서 실행이 실패하는 정도로만 단위 테스트를 작성한다.
- 셋째 : 현재 실패하는 테스트를 통과할 정도로만 실제 코드를 작성한다.
- 테스트 코드는 실제 코드 못지 않게 중요하다.
- 테스트는 유연성, 유지보수성, 재사용성을 제공한다.
- 깨끗한 테스트 코드는?? 가독성
- 각 테스트는 명확히 세 부분으로 나뉜다
- 테스트 자료를 만들고, 테스트 자료를 조작하고, 조작한 결과가 올바른지 확인한다.
- 깨끗한 테스트 FIRST
- Fast 빠르고, Independent 독립적이고, Repeatable 반복가능하고, Self-Validating 자기검증하고(bool), Timely 적시에(실제 코드를 구현하기 전)


10. 클래스

- 클래스는 작아야하고, 더 작아야 한다
- 단일책임원칙(SRP)은 클래스나 모듈을 변경할 이유가 하나, 단 하나뿐이어야 한다는 원칙

```

public class SuperDashboard extends JFrame implements MetaDataUser
{
    public Component getLastFocusedCompoent()
    public void setLastFocused(Component lastFocused)
    public int getMajorVersionNumber()
    public int getMinorVersionNumber()
    public int getBuildNumber()
}

메서드 수가 작음에도 책임이 너무 많다.

클래스 이름에 Processor, Manager, Super 등과 같이 모호한 단어가 있다면 클래스에다 여러 책임을 떠안겼다는 증거이다.

SuperDashboard는 소프트웨어 버전 정보를 추적한다.

그런데 버전 정보는 소프트웨어를 출시할 때마다 달라진다.

그리고 자바스윙 컴포넌트를 관리한다. 즉, 스윙 코드를 변경할 때마다 버전 번호가 달라진다.

책임, 즉 변경할 이유를 파악하려 애쓰다 보면 코드를 추상화하기도 쉬워진다.

SuperDashboard에서 버전 정보를 다루는 메서드 세 개를 따로 빼내 Version이라는 독자적인 클래스를 만든다.

Version 클래스는 다른 애플리케이션에서 재사용하기 아주 쉬운 구조다.

public class Version {
    public int getMajorVersionNumber()
    public int getMinorVersionNumber()
    public int getBuildNumber()
}

```

- 도구 상자를 어떻게 관리하고 싶은가? 작은 서랍을 많이 두고 기능과 이름이 명확한 컴포넌트를 나눠 넣고 싶은가?
- 아니면 큰 서랍 몇 개를 두고 모두를 던져 넣고 싶은가?
- 큰 클래스 몇 개가 아니라 작은 클래스 여럿!
- 응집도(Cohesion) 클래스는 인스턴스 변수 수가 작아야 한다.
- 각 클래스 메서드는 클래스 인스턴스 변수를 하나 이상 사용해야 한다.
- 일반적으로 메서드가 변수를 더 많이 사용할수록 메서드와 클래스는 응집도가 더 높다.
- 함수를 작게, 매개변수 목록을 짧게라는 전략을 따르다 보면 때때로 몇몇 메서드만이 사용하는 인스턴스 변수가 아주 많아진다.
- 이런 경우 새로운 클래스로 쪼개야 한다는 신호다.
- 응집도가 높아지도록 변수와 메서드를 적절히 분리해 새로운 클래스 두세 개로 쪼개준다.
- 응집도를 유지하면 작은 클래스 여럿이 나온다.
- 큰 함수를 작은 함수 여럿으로 나누기만 해도 클래스 수가 많아진다.
- 예를 들어, 변수가 아주 많은 큰 함수 하나가 있다.
- 큰 함수 일부를 작은 함수 하나로 빼내고 싶은데, 빼내려는 코드가 큰 함수에 정의된 변수 넷을 사용한다.
- 그렇다면 변수 네 개를 새 함수에 인수로 넘겨야 옳을까?
- 전혀 아니다! 만약 네 변수를 인스턴스 변수로 승격한다면 새 함수는 인수가 필요없다.
- 불행히도 이렇게 하면 클래스가 응집력을 잃는다..
- 몇몇 함수가 몇몇 변수만 사용한다면 독자적인 클래스로 분리해도 되지 않는가?
- 클래스가 응집력을 잃는다면 쪼개라
- 커누스 교수가 쓴 Literate Programming에 나오는 유서 깊은 에제 PrintPrimes 179쪽
- 단일 책임 원칙에 맞게 하나의 클래스를 여러 개의 클래스로 쪼갠다.
- 이상적인 시스템이라면 새 기능을 추가할 때 시스템을 확장할 뿐 기존 코드를 변경하지 않는다.
- 변경으로부터 격리
- 요구사항은 변하기 마련이다. 따라서 코드도 변하기 마련이다.
- 객체 지향 프로그래밍 입문에서 구체적인 클래스와 추상 클래스가 있다고 배웠다.
- 구체적인 클래스는 상세한 구현을 포함하며 추상 클래스는 개념만 포함한다고 배웠다.
- 상세한 구현에 의존하는 클라이언트 클래스는 구현이 바뀌면 위험에 빠진다.
- 그래서 우리는 인터페이스와 추상 클래스를 사용해 구현이 미치는 영향을 격리한다.
```
예를들어 Portfolio 클래스를 만든다고 가정하자.

그런데 Portfolio 클래스는 외부 TokyoStockExchange API를 사용해 포트폴리오 값을 계산한다.

따라서 우리 테스트 코드는 시세 변화에 영향을 받는다.

Portfolio 클래스에서 TokyoStockExchange API를 직접 호출하는 대신 StockExchange라는 인터페이스를 생성한 후 메서드 하나를 선언한다.

public interface StockExchange {
    Money currentPrice(String symbol);
}

다음으로 StockExchange 인터페이스를 구현하는 TokyoStockExchange 클래스를 구현한다.

또한 Portfolio 생성자를 수정해 StockExchange 참조자를 인수로 받는다.

public Portfolio {
    private StockExchange exchange;
    public Portfolio(StockExchange exchange) {
        this.exchange = exchange;
    }
}

이제 TokyoStockExchange 클래스를 흉내내는 테스트용 클래스를 만들 수 있다.
테스트용 클래스는 StockExchang 인터페이스를 구현하며 고정된 주가를 반환한다.

public class ProtfolioTest {
    private FixedStockExchangeStub exchange;
    private Portfolio portfolio;

    @Before
    protected void setUp() throws Exception {
        exchange = new FixedStockExchnageStub();
        exchange.fix("MSFT", 100);
        protfolio = new Protfolio(exchange);
    }

    @Test

    public void givenMSFTshouldBe500 throws Exception {
        protfoilo.add(5, "MSFT");
        Assert.assertEquals(500, protfolio.value();)
    }
}

위와 같은 테스트가 가능할 정도로 시스템의 결합도를 낮추면 유연성과 재사용성도 더욱 높아진다.

결합도가 낮다는 소리는 각 시스테 ㅁ요소가 다른 요소로부터 그리고 변경으로부터 잘 격리되어 있다는 의미다.

시스템 요소가 서로 잘 격리되어 있으면 각 요소를 이해하기도 더 쉬워진다.

이렇게 결합도를 최소로 줄이면 자연스럽게 또 다른 클래스 설계 원칙인 DIP를 따르는 클래스가 나온다.

본질적으로 DIP는 클래스가 상세한 구현이 아니라 추상화에 의존해야 한다는 원칙이다.

우리가 개선한 Portfoilo 클래스는 TokyoStockExchnage라는 상세한 구현 클래스가 아니라 StockExchange 인터페이스에 의존한다.

StockExchange 인터페이스는 주식 기호를 받아 현재 주식 가격을 반환한다는 추상적인 개념을 포함한다.

이와 같은 추상화로 실제로 주가를 얻어오는 출처나 얻어오는 방식 등과 같은 구체적인 사실을 모두 숨긴다.

```


11. 시스템

- 복잡성은 죽음이다.
- 도시가 돌아가는 이유는 적절한 추상화와 모듈화 때문이다.
- 깨끗한 코드를 구현하면 낮은 추상화 수준에서 관심사를 분리하기 쉬워진다.
- 이 장에서는 높은 추상화 수준, 즉 시스템 수준에서도 깨끗함을 유지하는 방법을 살펴본다.
- 시스템 제작과 시스템 사용을 분리하라
- 제작은 사용과 아주 다르다는 사실을 명심한다.
- 소프트웨어 시스템은 (애플리케이션 객체를 제작하고 의존성을 서로 '연결'하는) 준비 과정과 (준비 과정 이후에 이어지는) 런타임 로직을 분리해야 한다.
- 시작 단계는 모든 애플리케이션이 풀어야 할 관심사다.
- 불행히도 대다수 애플리케이션은 시작 단계라는 관심사를 분리하지 않는다.
- 준비 과정 코드를 주먹구구식으로 구현할 뿐만 아니라 런타임 로직과 마구 뒤섞는다.
- Main 분리
- 시스템 생성과 시스템 사용을 분리하는 한 가지 방법으로, 생성과 관련한 코드는 모두 main이나 main이 호출하는 모듈로 옮기고,
- 나머지 시스템은 모든 객체가 생성되었고 모든 의존성이 연결되었다고 가정한다.
- main 함수에서 시스템에 필요한 객체를 생성한 후 이를 애플리케이션에 넘긴다.
- 애플리케이션은 그저 객체를 사용할 뿐이다.
- 애플리케이션은 main이나 객체가 생성되는 과정을 전혀 모르고, 단지 모든 객체가 적절히 생성되었다고 가정한다.
- Factory
- 물론 때로는 객체가 생성되는 시점을 애플리케이션이 결정할 필요도 생긴다.
- 이때는 Abstract Factory 패턴을 사용한다.
- 그러면 객체를 생성하는 시점은 애플리케이션이 결정하지만 객체를 생성하는 코드는 애플리케이션이 모른다.
- 의존성 주입
- 사용과 제작을 분리하는 강력한 메커니즘 하나가 의존성 주입이다.
- 의존성 주입은 제어 역전 기법을 의존성 관리에 적용한 메커니즘이다.
- 제어 역전에서는 한 객체가 맡은 보조 책임을 새로운 객체에게 전적으로 떠넘긴다.
- 새로운 객체는 넘겨받은 책임만 맡으므로 단일 책임 원칙을 지키게 된다.
- 소프트웨어 시스템은 물리적인 시스템과 다르다. 관심사를 적절히 분리해 관리한다면 소프트웨어 아키텍처는 점진적으로 발전할 수 있다.
- 최선의 시스템 구조는 각기 POJO (또는 다른) 객체로 구현되는 모듈화된 관심사 영역(도메인)으로 구성된다.
- 이렇게 서로 다른 영역은 해당 영역 코드에 최소한의 영향을 미치는 관점이나 유사한 도구를 사용해 통합한다.
- 이런 구조 역시 코드와 마찬가지로 테스트 주도 기법을 적용할 수 있다.
- 의사 결정을 최적화하라
- 관심사를 모듈로 분리한 POJO 시스템은 기민함을 제공한다. 이런 기민함 덕택에 최선 정보에 기반해 최선의 시점에 최적의 결정을 내리기가 쉬워진다. 또한 결정의 복잡성도 줄어든다.
- 명백한 가치가 있을 때 표준을 현명하게 사용하라.
- 표준을 사용하면 아이디어와 컴포넌트를 재사용하기 쉽고, 적절한 경험을 가진 사람을 구하기 쉬우며, 좋은 아이디어를 캡슐화하기 쉽고, 컴포넌트를 엮기 쉽다.
- 하지만 때로는 표준을 만드는 시간이 너무 오래 걸려 업계가 기다리지 못한다.
- 시스템은 도메인 특화 언어가 필요하다. 도메인 특화 언어(Domain-Specific Language, DSL)를 사용하면 고차원 정책에서 저차원 세부사항에 이르기까지 모든 추상화 수준과 모든 도메인을 POJO로 표현할 수 있다.
- 모든 추상화 단계에서 의도는 명확히 표현해야 한다. 그러려면 POJO를 작성하고 관점 혹은 관점과 유사한 메커니즘을 사용해 각 구현 관심사를 분리해야한다.

12. 창발성

- 창발적 설계로 깔끔한 코드를 구현하자
- 착실하게 따르기만 하면 우수한 설계가 나오는 간단한 규칙 네 가지
- 모든 테스트를 실행한다.
- 중복을 없앤다.
- 프로그래머 의도를 표현한다.
- 클래스와 메서드 수를 최소로 줄인다.
- 테스트 케이스를 만들고 계속 돌려라라는 간단하고 단순한 규칙을 따르면 시스템은 낮은 결합도와 높은 응집력이라는, 객체 지향 방법론이 지향하는 목표를 저절로 달성한다.
- 테스트 케이스를 모두 작성했다면 이제 코드와 클래스를 정리해도 괜찮다.
- 구체적으로는 코드를 점진적으로 리팩터링 해나간다.
- 코드를 정리하면서 시스템이 깨질까 걱정할 필요가 없다. 테스트 케이스가 있으니까
- 응집도를 높이고, 결합도를 낮추고, 관심사를 분리하고, 시스템 관심사를 모듈로 나누고, 함수와 클래스 크기를 줄이고, 더 나은 이름을 선택하는 등 다양한 기법을 동원한다.
- 중복을 없애라 ** 

```
int size() {
    boolean isEmpty() {}
}

각 메서드를 따로 구현하는 방법도 있다. isEmpty 메서드는 부울 값을 반환하며 size 메서드는 개수르 ㄹ반환한다.

하지만 isEmpty 메서드에서 size 메서드를 이용하면 코드를 중복해 구현할 필요가 없어진다.

boolean isEmpty() {
    return 0 === size();
}

```

- 중복을 제거하면서 공통적인 코드를 새 메서드로 뽑고 보니 클래스가 SRP를 위반할 수도 있다.
- 그런 경우에는 새 메서드를 다른 클래스로 옮겨가도 좋다.
- Template method 패턴을 사용하여 고차원 중복을 제거한다.
- 좋은 이름을 선택하고, 함수와 클래스 크기를 가능한 줄이고, 표준 명칭을 사용하고, 단위 테스트 케이스를 작성해라
- 나중에 읽은 사람을 고려해 조금이라도 읽기 쉽게 만들려는 충분한 고민은 거의 찾기 어렵다.
- 하지만 나중에 코드를 읽을 사람은 바로 자신일 가능성이 높다는 사실을 명심하자.

13. 동시성

- 동시성과 깔끔한 코드는 양립하기 어렵다.
- 동시성이 필요한 이유? 동시성은 결합을 없애는 전략이다.
- 즉, 무엇과 언제를 분리하는 전략이다
- 무엇과 언제를 분리하면 애플리케이션 구조와 효율이 극적으로 나아진다.
- 동시성은 항상 성능을 높여준다. 동시성을 구현해도 설계는 변하지 않는다. 웹또는 EJB 컨테이너를 사용하면 동시성을 이해할 필요가 없다.
- 동시성은 다소 부하를 유발한다. 동시성은 복잡하다. 일반적으로 동시성 버그는 재현하기 어렵다
- 스레드는 가능한 독립적으로 구현하라
- 공유 객체 하나에는 메서드 하나만 사용하라
- 동기화하는 부분을 최대한 작게 만들어라

14. 점진적인 개선

- Args 구현 ** 247
- 아침에 엉망으로 만든 코드를 오후에 정리하기는 어렵지 않다.
- 더욱이 5분 전에 엉망으로 만든 코드는 지금 당장 정리하기 아주 쉽다.
- 그러므로 코드는 언제나 최대한 깔끔하고 단순하게 정리하자

15. Junit

- 조건문을 캡슐화해라
- 부정문은 긍정문보다 이해하기 약간 더 어렵다

16. SerialDate 리팩터링

- 