# Singleton

Singleton 은 클래스에 인스턴스가 하나만 있는지 확인 하면서 이 인스턴스에 대한 전역 액세스 포인트를 제공 할 수있는 생성 디자인 패턴입니다.

Singleton의 모든 구현에는 다음 두 단계의 공통점이 있습니다.

다른 개체 new가 Singleton 클래스와 함께 연산자를 사용하지 못하도록 기본 생성자를 비공개로 설정합니다.
생성자 역할을하는 정적 생성 메서드를 만듭니다. 내부적으로 이 메서드는 개인 생성자를 호출하여 개체를 만들고 정적 필드에 저장합니다.
이 메서드에 대한 다음 호출은 모두 캐시 된 개체를 반환합니다.

![structure-en](https://user-images.githubusercontent.com/6989005/99183873-7cebec00-2782-11eb-93ad-b5b9194e1707.png)

```
<?php

//https://pronist.tistory.com/27 static과 self..?

//https://wani.kr/posts/2015/02/12/php-something-3-static-vs-self/

//PHP 객체지향에서 static은 상속이 됩니다. 
//그리고 그 static메서드 안에서 자기 자신 클래스를 생성하고 싶을때가 있습니다.
//그때 사용할 수 있는 것이 static 일까요 self 일까요?

class Foo {
	public static function func1() {
		return new Foo;
	}
	public static function func2() {
		return new static();
	}
	public static function func3() {
		return new self();
	}
}

class Bar extends Foo {}

var_dump( Bar::func1() );
var_dump( Bar::func2() );
var_dump( Bar::func3() );


class Person{
  private $count = 0;
  private $name;
  function __construct($name){
    $this->name = $name;
    $this->count = $this->count + 1;
  }
  function enter(){
    echo "<h1>Enter ".$this->name." ".$this->count."th</h1>";
  }
  static function getCount(){
    return $this->count;
  }
}

$p1 = new Person('egoing');
$p1->enter();
$p2 = new Person('leezche');
$p2->enter();
$p3 = new Person('duru');
$p3->enter();
$p4 = new Person('taiho');
$p4->enter();
echo Person::getCount();

//각자 자신의 인스턴스 안에서만 유효하기 때문에 1을 증가시키는 게 각각의 인스턴스 안에 생성된 인스턴스의 변수에 1을 올리는 것 뿐이다.


class Person{
    private static $count = 0;
    private $name;
    function __construct($name){
      $this->name = $name;
      self::$count = self::$count + 1;
    }
    function enter(){
      echo "<h1>Enter ".$this->name." ".self::$count."th</h1>";
    }
    static function getCount(){
      return self::$count;
    }
  }
  $p1 = new Person('egoing');
  $p1->enter();
  $p2 = new Person('leezche');
  $p2->enter();
  $p3 = new Person('duru');
  $p3->enter();
  $p4 = new Person('taiho');
  $p4->enter();
  echo Person::getCount();

//instance라는 변수를 생성할 때 dynamic이라는 변수가 있다고 생각하면, 
//인스턴스가 생성 될 때 name이라는 property는 사실 네 개가 만들어지는 것인데,
//static을 앞에서 선언하면 그 뒤에있는 변수는 class 내에 소속되어 버린다.
//static이 붙어있지 않은 변수는 $p1인스턴스에 $name이 소속되고, $p2인스턴스에 $name이 소속된다. 동적인 의미를 이해하는가?
//static은 모든 인스턴스가 공유하기 때문에, 상태를 공유한다.

class Singleton
{
    private static $instances = [];

    protected function __construct() {}

    protected function __clone() {}

    public function __wakeup()
    {
        throw new \Exception("Cannot unserialize a singleton");
    }

    public static function getInstance(): Singleton
    {
        $cls = static::class;
        if (!isset(self::$instances[$cls])) {
            self::$instances[$cls] = new static();
        }

        return self::$instances[$cls];
    }

    public function someBusinessLogin()
    {
        // ...
    }
}


function clientCode()
{
    $s1 = Singleton::getInstance();
    $s2 = Singleton::getInstance();

    if ($s1 === $s2) {
        echo "Singleton works, both variable contain same instances";
    } else {
        echo "Singleton failed, variables contain different instances";
    }
}

clientCode();

?>
```