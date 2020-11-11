# Closure

PHP는 일급 함수(first-class function)를 지원합니다. 이는 함수가 변수에 할당될 수 있다는 것입니다. 사용자가 정의한 함수나 내장 함수 모두 변수에 의해서 참조될 수 있고 동적으로 호출될 수 있습니다. 함수는 다른 함수의 인자로 전달될 수 있고 함수가 다른 함수를 리턴값으로 리턴하는 것도 가능합니다. 이런 기능을 고차함수(Higher-order function)라고 합니다.
함수가 자기 스스로 다시 호출하는 재귀 호출(Recursion)도 지원하지만, 대부분의 PHP 코드는 재귀보다는 반복(iteration)하는 형태로 작성됩니다.
익명 함수(와 클로저)는 2009년에 발표된 PHP 5.3부터 지원됩니다.
PHP 5.4에서는 클로저를 특정 객체의 스코프에 바인딩하는 기능이 추가되었습니다. 또한 대부분의 경우 익명 함수와 동일하게 사용할 수 있는 호출가능한 타입(callable) 지원이 강화되었습니다.
전략 패턴(strategy pattern, 디자인 패턴 중의 하나)를 구현할 때 고차함수를 사용하는 경우가 많습니다. array_filter() 내장 함수는 입력 배열과 함수(전략 혹은 콜백이라고 할 수 있죠)를 인자로 받아서 배열의 항목을 필터링하는 데에 사용합니다.


> 익명함수의 사용 초급
```
<?php
$input = array(1, 2, 3, 4, 5, 6);
//익명 함수
$filter_even = function($item) {
    return ($item % 2) == 0;
}
// array_filter 내장 함수는 배열과 함수를 인자로 받는다.
$output = array_filter($input, $filter_even);
// 익명 함수를 변수에 할당해서 전달할 필요없이 이렇게 하는 것도 가능하다
$output = array_filter($input, function($item){
    return ($item % 2) == 0;
});
print_R($output);
?>
```
> Quiz. Output ?
```
<?php
function criteria_greater_than($min)
{
    return function($item) use ($min) {
        return $item > $min;
    };
}
$input = array(1, 2, 3, 4, 5, 6);
$output = array_filter($input, criteria_greater_than(3));
print_R($output);

?>
```
> Quiz. Output ?

```
<?php
$message = 'hello';
$example = function () {
    var_dump($message);
};
$example();

Notice: Undefined variable: message in /home/genipco/cy_mice/oda2020/test.php on line 6
NULL


$example = function () use ($message) {
    var_dump($message);
};
$example();

string(5) "hello"

$message= 'world';
$example();

string(5) "hello" <-- $message의 변수 변경했는데 변경 X

$message = 'hello';
$example = function () use (&$message) {
    var_dump($message);
};
$example();

string(5) "hello" <-- Hello로 다시 초기화하고 참조자를 사용했다.

$message = 'world';
$example();

string(5) "world" <-- 참조자를 선언한 상태에서 $message값을 변경했더니 example도 변경되었다.

$example = function ($arg) use ($message) {
    var_dump($arg. ' ' . $message);
};
$example("hello "); 

string(12) "hello world" <-- 클로저가 일반 인수를 허용하는 모습이다.

?>
```


출처: <https://www.php.net/functions.anonymous> 

예제 # 4 클로저 및 범위 지정
```
<?php
// A basic shopping cart which contains a list of added products
// and the quantity of each product. Includes a method which
// calculates the total price of the items in the cart using a
// closure as a callback.
class Cart
{
    const PRICE_BUTTER  = 1.00;
    const PRICE_MILK    = 3.00;
    const PRICE_EGGS    = 6.95;

    protected $products = array();
    
    public function add($product, $quantity)
    {
        $this->products[$product] = $quantity;
    }
    
    public function getQuantity($product)
    {
        return isset($this->products[$product]) ? $this->products[$product] :
               FALSE;
    }
    
    public function getTotal($tax)
    {
        $total = 0.00;
        
        $callback =
            function ($quantity, $product) use ($tax, &$total)
            {
                $pricePerItem = constant(__CLASS__ . "::PRICE_" .
                    strtoupper($product));
                $total += ($pricePerItem * $quantity) * ($tax + 1.0);
            };
        
        array_walk($this->products, $callback);
        return round($total, 2);
    }
}

$my_cart = new Cart;

// Add some items to the cart
$my_cart->add('butter', 1);
$my_cart->add('milk', 3);
$my_cart->add('eggs', 6);

// Print the total with a 5% sales tax.
print $my_cart->getTotal(0.05) . "\n";
// The result is 54.29
?>
```

> 잘 몰랐던 부분? Const 로 상수변수 선언하고, 이 값을 가져오는데   
> __CLASS__하면 현재 클래스 가져오고 Product 내용 가져오는건데 butter이면   
> constant(__CLASS__::PRICE_BUTTER) 하면 1.00을 가져옴   

> Array_walk는

* array_walk(배열, 함수) 출처: https://dororongju.tistory.com/114

* 배열의 각 요소들을 함수의 인자로 넘겨 함수를 배열의 크기만큼 실행시키는 함수입니다.
사용자 정의 함수인 함수는 인자로 ($value, $key)를 받아 처리합니다.

* ※순서 주의, ($key, $value) 아닙니다. ($value, $key) 입니다.
```
<?php

$arr_phone = array(
                  'A' => '01011111111',
                  'B' => '01022222222',
                  'C' => '01033333333',
                  'D' => '01044444444',
); 에서

$arr_phone = array(
                  'A' => '010-1111-1111',
                  'B' => '010-2222-2222',
                  'C' => '010-3333-3333',
                  'D' => '010-4444-4444',
); 로 변환한다고 하면

function setPhoneNumFormat(&$value)
{
    $value = substr($value,0,3)."-".substr($value,3,4)."-".substr($value,7,4);
}

array_walk($arr_phone, 'setPhoneNumFormat');

?>
```

# Callable

* php에서는 callable 이라는 타입 힌트를 제공한다. 이 타입 힌트는 말 그대로 호출이 가능한 클래스, 메소드, 또는 함수인 경우에 사용할 수 있다. php에서는 타입이 별도의 타입으로 존재하지 않는 대신에 문자열로 처리하고 있어서 다소 모호한 부분도 있다. callable을 타입 힌트로 사용했을 때 어떤 값을 넘길 수 있는지 명확히 알고 있어야 한다.
```
function callableOnly(callable $callable): void {
    // callable에 해당하면 다음처럼 호출할 수 있음
    call_user_func($callable);
// 일부를 제외하고는 다음과 같이 호출 가능함
    $callable();
}
```

* 출처: <https://edykim.com/ko/post/a-look-at-php-callable/#%ED%95%A8%EC%88%98> 

* Call_user_func라는것은 결국.. 익명함수나 invoke함수를 호출하는 내용이고
Is_callable은 callable이 되는지에 대한 함수이다.

```
class C {
    public function __invoke($name) {
        echo 'Hello ', $name, "\n";
    }
}

$c = new C();
call_user_func($c, 'PHP!');
```

> Quiz. Output ? 

