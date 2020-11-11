# What are magic methods in PHP?

* All function names starts with __ in PHP classes are magical and each one does something special. These functions are magical: __construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __serialize(), __unserialize(), __toString(), __invoke(), __set_state(), __clone() and __debugInfo().

* __construct()

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
* Quiz - Output ? 