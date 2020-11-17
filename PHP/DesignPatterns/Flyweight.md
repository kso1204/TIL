# Flyweight

출처 : https://refactoring.guru/design-patterns/flyweight

Flyweight 는 각 개체의 모든 데이터를 유지하는 대신 여러 개체간에 상태의 공통 부분을 공유하여 사용 가능한 RAM 양에 더 많은 개체를 넣을 수있는 구조적 디자인 패턴입니다.

복잡하기도 하고.. 잘 이해가 가지 않는다

플라이웨이트의 클래스는 두 부분으로 구성되어있다.

고유 상태: 많은 객체에 복제 된 변하지 않는 데이터를 포함하는 필드 (Brand, Model, Color) 
외부 상태: 각 객체에 고유 한 컨텍스트 데이터를 포함하는 필드 (Plates, Owner)

Unique (extrinsic) data such as a pet’s name, age, and owner info.
Shared (intrinsic) data such as a breed name, color, texture, etc.

The state stored inside a flyweight is called intrinsic.
The state passed to the flyweight’s methods is called extrinsic.

두 부분으로 나누어진 데이터를 구분하는 게 쉬운듯 하면서 어려움.. 이 부분만 이해하면 된다.

![20201116144140](https://user-images.githubusercontent.com/6989005/99216772-deab6500-2819-11eb-9128-1b062c0fbb24.png)

고유 상태(본질적인 상태)와 외부 상태

문제

![20201116143918](https://user-images.githubusercontent.com/6989005/99216701-a1df6e00-2819-11eb-82e4-772d7308d803.png)

해결

![20201116143926](https://user-images.githubusercontent.com/6989005/99216698-a0ae4100-2819-11eb-9f72-207eb3451ff2.png)

램 소모량 21GB <-> 32MB

As you’ve probably guessed by now, an object that only stores the intrinsic state is called a flyweight.

![20201116144446](https://user-images.githubusercontent.com/6989005/99216964-4b266400-281a-11eb-9426-c0814614d11a.png)

```
<?php

//Flyweight의 operation 부분이 핵심인데..
//Shared, Unique
//FlyweightFactory에서 plates와 owner가 지정된 모델이 삽입됐다고 했을 때
//FlyweightFacotry가 가지고 있는 Brand, Model, Color면 reusing하고 가지고 있지 않으면 creating한다.


class Flyweight
{
    private $sharedState;

    public function __construct($sharedState)
    {
        $this->sharedState = $sharedState;
    }

    public function operation($uniqueState): void
    {
        $s = json_encode($this->sharedState);
        $u = json_encode($uniqueState);
        echo "Flyweight: Displaying shared ($s) and unique($u) state";
    }
}

class FlyweightFactory
{
    private $flyweights = [];

    public function __construct(array $initalFlyweights)
    {
        foreach ($initalFlyweights as $state) {
            $this->flyweights[$this->getKey($state)] = new Flyweight($state);
        }
    }

    public function getKey(array $state): string
    {
        ksort($state);

        return implode("_", $state);
    }
    //* Returns an existing Flyweight with a given state or creates a new one.
    public function getFlyweight(array $sharedState): Flyweight 
    {
        $key = $this->getKey($sharedState);

        if (!isset($this->flyweights[$key])) {
            echo "FlyweightFactory: Can't find a flyweight, creating new one";
            $this->flyweights[$key] = new Flyweight($sharedState);
        } else {
            echo "FlyweightFacotry: Reusing existing flyweight";
        }

        return $this->flyweights[$key];
    }

    public function listFlyweights(): void
    {
        $count = count($this->flyweights);
        echo "FlyweightFacotry: I have $count flyweights";
        foreach ($this->flyweights as $key => $value) {
            echo $key;
        }
    }
}

/**
 * The client code usually creates a bunch of pre-populated flyweights in the
 * initialization stage of the application.
 */
$factory = new FlyweightFactory([
    ["Chevrolet", "Camaro2018", "pink"],
    ["Mercedes Benz", "C300", "black"],
    ["Mercedes Benz", "C500", "red"],
    ["BMW", "M5", "red"],
    ["BMW", "X6", "white"],
    // ...
]);
$factory->listFlyweights();


function addCarToPoliceDatabase(FlyweightFactory $ff, $plates, $owner, $brand, $model, $color) {
    echo "\nClient: Adding a car to database.\n";
    $flyweight = $ff->getFlyweight([$brand, $model, $color]);

    // The client code either stores or calculates extrinsic state and passes it
    // to the flyweight's methods.
    $flyweight->operation([$plates, $owner]);
}

addCarToPoliceDatabase($factory,
    "CL234IR",
    "James Doe",
    "BMW",
    "M5",
    "red",
);

addCarToPoliceDatabase($factory,
    "CL234IR",
    "James Doe",
    "BMW",
    "X1",
    "red",
);

$factory->listFlyweights();

?>
```