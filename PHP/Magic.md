# What are magic methods in PHP? 

* 출처: <https://medium.com/@mahshad/php-magic-methods-dae1847c5cef> 

* All function names starts with __ in PHP classes are magical and each one does something special. These functions are magical: [__construct()](#__construct), [__destruct()](#__destruct), [__call()](#__call), [__callStatic()](#__callStatic), [__get()](#__get), [__set()](#__set), [__isset()](#__isset), [__unset()](#__isset), [__sleep()](#__sleep), [__sleep()](#__wakeup), [__serialize()](#__serialize), [__unserialize()](#__unserialize), [__toString()](#__toString), [__invoke()](#__invoke), [__clone()](#__clone) and [__debugInfo()](#__debugInfo).

# __construct()

Classes that have __construct() method, call it every time new object created. In other words, it’s useful to initialization that the object may need before going further.

```
<?php
class Student {
    public function __construct($name) {
        echo "Initialization...";
        $this->name = $name;
    }
    public function sayHello() {
        return "Hello, $this->name";
    }
}
$student = new Student('Mahshad');
echo $student->sayHello();
?>
```
> Quiz. Output ?

# __destruct()

This method is called as soon as the object is destroyed.

```
<?php
class Student {
    public function __destruct() {
        echo "Destroy...";
    }
}
echo "First...";
$student = new Student();
echo "Last...";
?>
```
> Quiz. Output ?

* In PHP, the term overloading is used to dynamically create methods and properties. There are two methods supporting method overloading: __call() and __callStatic().

# __call()

This magic method is triggered when we call a method that doesn’t defined. This method accepts two parameters, as below:

> public __call ( string $name , array $arguments ) : mixed

```
<?php
class Student {
    public function __call($name, $arguments) {
        echo $name. ' => ' .implode(', ', $arguments);
    }
}
$student = new Student();
echo $student->hello('Kim','Sang','Wook');
?>
```
> Quiz. Output ?

# __callStatic()

This magic method is almost similar to __call() method, except that the __call() method is for object context and __callStatic() method is for static context.
The __callStatic() method accepts two parameters, as below:

> public static __callStatic ( string $name , array $arguments ) : mixed
```
<?php
class Student {
    public static function __callStatic($name, $arguments) {
        echo $name. ' => ' .implode(', ', $arguments);
    }
}
$student = new Student();
echo $student::hello('Kim','Sang','Wook');
?>
```
> Quiz. Output ?

* Another aspect of PHP overloading capabilities is property overloading. There are four magic methods that support property overloading: __get(), __set(), __isset() and __unset().

# __get()

The __get() magic method is utilized for reading data from inaccessible (protected or private) or non-existing properties. The method accepts one parameter, as following:

> public __get ( string $name ) : mixed
```
<?php
class Student {
    private $data = [
        'first_name' => 'Sang Wook',
        'last_name' => 'Kim'
    ];
    public function __get ($name) {
        echo $name . ' => ' . $this->data[$name];
    }
}
$student = new Student();
echo $student->first_name;

?>
```
> Quiz. Output ?

# __set()
The __set() magic method is run when writing data to inaccessible (protected or private) or non-existing properties. The method accepts two parameters, as following:

> public __set ( string $name , mixed $value ) : void

```
<?php
class Student {
    private $data = [];
    public function __set($name, $value) {
        $this->data[$name] = $value;
    }
    public function __get($name) {
        echo $name. " => " .$this->data[$name];
    }
}
$student = new Student();
$student->first_name = "Sang Wook";
echo $student->first_name;

?>
```
> Quiz. Output ?

# __isset() and __unset()

The __isset() magic method is triggered by calling isset() or empty() on inaccessible (protected or private) or non-existing properties. The method accepts a single parameter, as below:

> public __isset ( string $name ) : bool

The __unset() magic method is invoked when unset() is used on inaccessible (protected or private) or non-existing properties. The method accepts a single parameter, as below:

> public __unset ( string $name ) : void
```
<?php
class Student {
    private $data = [
        'name' => 'kim sang wook',
        'age' => 31
    ];
    public function __isset ($name) {
        return isset($this->data[$name]);
    }
    public function __unset ($name) {
        unset($this->data[$name]);
    }
}
$student = new Student();
echo var_dump(isset($student->name));
unset($student->name);
echo var_dump(isset($student->name));

?>
```
> Quiz. Output ?

* 직렬화 또는 시리얼라이제이션은 컴퓨터 과학의 데이터 스토리지 문맥에서 데이터 구조나 오브젝트 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성할 수 있는 포맷으로 변환하는 과정이다. 오브젝트를 직렬화하는 과정은 오브젝트를 마샬링한다고도 한다.

# __sleep() and __wakeup()

The serialize() function triggers the __sleep() magic method if it exists and conversely, the unserialize() function triggers the __wakeup() magic method. Both of them accepts no parameter:

> public __sleep ( void ) : array

> public __wakeup ( void ) : void

```
<?php
class Student {
    public $first_name = 'sang wook';
    private $last_name = 'kim';
    protected $age = 25;
    public function__sleep() {
        return ['first_name', 'age'];
    }
}
$student = new Student();
$serialized = serialize($student);
var_dump($serialized);

?>
```
> Quiz. Output ?

# __serialize()

The serialize() checks if the class has a function with the __serialize() magic method. If so, that function is executed first before any serialization.
Note: If both __serialize() and __sleep() are defined in the same object, only __serialize() will be called and __sleep() will be ignored.
The __serialize() method accepts no parameters:

> public __serialize ( void ) : array
```
<?php
class Student {
    public $first_name = 'sang wook';
    private $last_name = 'kim';
    protected $age = 25;
    public function __serialize() {
        return [
            'first_name' => $this->first_name,
            'last_name' => $this->last_name,
        ];
    }
}
$student = new Student();
$serialized = serialize($student);
var_dump($serialized);

?>
```
> Quiz. Output ?

* 직렬화랑 sleep의 차이점을 그냥 써보면? Sleep은 private 변수를 사용했을 때 
직렬화 하면서 클래스 이름까지 같이 서술된다.ex)Studentlast_name
직렬화는 그냥 이름만 서술 last_name

# __unserialize()

Conversely, unserialize() checks for the presence of a function with the magic name __unserialize(). If present, this function will be passed the restored array that was returned from __serialize().
The __unserialize() method accepts only one parameter:

> public __unserialize ( array $name ) : void
```
<?php
class Student {
    public $first_name = 'sang wook';
    private $last_name = 'kim';
    protected $age = 25;
    public function __serialize() {
        return [
            'first_name' => $this->first_name,
            'last_name' => $this->last_name,
        ];
    }
    public function __unserialize() {
        $this->first_name = $data['first_name'];
        var_dump($data['first_name']);
    }
}
$student = new Student();
$serialized = serialize($student);
$unserialized = unserialize($serialized);

?>
```
> Quiz. Output ?

# __toString()

The __tostring() magic method triggeres when the class is treated like a string. The method accepts no parameter:

> public __toString ( void ) : string
```
<?php
class Student {
    public $first_name = 'sang wook';
    protected $last_name = 'kim';
    public function __tostring () {
        return $this->first_name . ' - ' . $this->last_name;
    }
}
echo new Student();

?>
```
toString은 echo로 호출한다고 생각하면 됨

> Quiz. Output ?

# __invoke()

The __invoke() magic method is called when when the object is being called as a function. The method accepts multi parameters:

> public __invoke ([ $... ] ) : mixed
```
<?php
class Student {
    public function __invoke ($first_name, $last_name) {
        echo $first_name. ' - '.$last_name;
    }
}
$student = new Student();
$student('Sang Wook', 'Kim');

?>
```

Invoke는 callable, call_user_func, is_callable등과 연관이 있다.

> Quiz. Output ?

# __clone()

The __clone() magic method is triggered where cloning objects is done by using clone keyword. The method accepts no parameter.

> public __clone ( void ) : void
```
<?php
class Student {
    public $id;
    public function __clone () {
        $this->id = null;
    }
}
$student_1 = new Student();
$student_1->id = 2372732;
$student_2 = clone $student_1;
var_dump($student_1);
var_dump($student_2);
?>
```
> Quiz. Output ?

# __debugInfo()

The __debugInfo() magic method is triggered when var_dump function is called. The method accepts no parameter:

> public __debugInfo ( void ) : array
```
<?php
class Student { 
    public $fisrt_name = "Sang Wook";
    public $salary = 700;
    public $bonus = 1.2;
    public function __debugInfo () {
        return [
            'name' => $this->first_name,
            'income' => $this->salary * $This->bonus
        ];
    }
}
var_dump(new Student());
?>
```

__debuginfo는 var_dump로 호출한다 echo 는 __tostring 

> Quiz. Output ?





