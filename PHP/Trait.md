# Trait 

* 출처 : https://www.php.net/language.oop5.traits

* As of PHP 5.4.0, PHP implements a method of code reuse called Traits.

Traits are a mechanism for code reuse in single inheritance languages such as PHP. A Trait is intended to reduce some limitations of single inheritance by enabling a developer to reuse sets of methods freely in several independent classes living in different class hierarchies. The semantics of the combination of Traits and classes is defined in a way which reduces complexity, and avoids the typical problems associated with multiple inheritance and Mixins.

A Trait is similar to a class, but only intended to group functionality in a fine-grained and consistent way. It is not possible to instantiate a Trait on its own. It is an addition to traditional inheritance and enables horizontal composition of behavior; that is, the application of class members without requiring inheritance.

> 우선 순위

```
<?php
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}
trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}
class MyHelloWorld extends Base {
    use SayWorld;
}
$o = new MyHelloWorld();
$o->sayHello();
//output?
//'Hello World!';
?>
```
> Parent는 부모의 함수를 호출하는 것이다.

```
<?php
trait HelloWorld {
    public function sayHello() {
        echo 'Hello World!';
    }
}
class TheWorldIsNotEnough {
    use HelloWorld;
    public function sayHello() {
        echo 'Hello Universe!';
    }
}
$o = new TheWorldIsNotEnough();
$o->sayHello();
// output?
// Hello Universe!
?>
```
> 우선순위를 보면 트레이트의 부모의 중복되는 함수가 우선한다.

```
<?php
trait Hello {
    public function sayHello() {
        echo 'Hello ';
    }
}
trait World {
    public function sayWorld() {
        echo 'World';
    }
}
class MyHelloWorld {
    use Hello, World;
    public function sayExclamationMark() {
        echo '!';
    }
}
$o = new MyHelloWorld();
$o->sayHello();
$o->sayWorld();
$o->sayExclamationMark();
?>
```
> 여러 trait를 쉼표로 구분하여 use문에 나열하여 클래스에 삽입할 수 있다.

```
<?php
trait A {
    public function smallTalk() {
        echo 'a';
    }
    public function bigTalk() {
        echo 'A';
    }
}

trait B {
    public function smallTalk() {
        echo 'b';
    }
    public function bigTalk() {
        echo 'B';
    }
}

class Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
    }
}

class Aliased_Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
        B::bigTalk as talk;
    }
}
?>
```

> Trait A와 B에서 같은 이름으로 선언된 함수는 충돌이 일어난다.   
> 이 충돌을 방지하기 위해서 Class에서는 insteadof를 사용하는데   
> B::smallTalk insteadof A라는건 A의 smallTalk대신에 B의SmallTalk를 사용하겠다는 거고   
> A::bigTalk insteadof B; 은 마찬가지로 B의 bigTalk대신에 A의 BigTalk를 사용한다는 것이다.   
> B의 BigTalk를 사용하고 싶다면 as talk<-- as로 별명을 선언해서 사용한다.   




