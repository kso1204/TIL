# Error and Exception

출처 : https://modernpug.github.io/php-the-right-way/

면접 질문에서 에러와 예외에 대해 아냐고 물어보셨다.

뭔가 다른데 뭐가 다른지 설명할 수가 없었다...

부족함을 많이 느끼게 해준 면접이었다.

PHP는 “예외를 양념으로 사용하는(exception-light)” 프로그래밍 언어입니다. 

$ php -a
php > echo $foo;
Notice: Undefined variable: foo in php shell code on line 1

PHP에는 여러 레벨의 에러가 있습니다. 가장 일반적인 것으로는 에러(error), 알림(notice), 경고(warning)이 있습니다. 
이것들의 심각도(severity)는 각각 E_ERROR, E_NOTICE, E_WARNING 입니다.
‘에러’는 치명적인 런타임 에러인데, PHP 스크립트의 실행을 중지시키는 수준이므로 코드를 수정해야 합니다.

PHP 설정을 변경하거나 함수 호출을 하여 에러 보고 방식을 바꿀 수 있습니다.
내장 PHP 함수인 error_reporting()을 사용하면 해당 스크립트가 실행되는 동안 사용될 에러 레벨을 설정할 수 있습니다.
```
<?php
error_reporting(E_ERROR | E_WARNING);
?>

내가 작성했던 소스중 이런 부분이 있는데.. 웃기다 모든 에러를 다 리포팅하면서 에러를 보여주지 말라고 설정한다.

```
<?
error_reporting(E_ALL); 
ini_set('display_errors','0');
?>
```

ErrorException

PHP도 완벽하게 “예외를 적극적으로 사용하는” 프로그래밍 언어로서 동작할 수 있는 능력이 있습니다.
코드 몇 줄만 있으면 쉽게 전환시킬 수 있죠. 
기본적으로는 “에러”를 “예외”로 던지는 식으로 하면 됩니다.
Exception 클래스를 상속한 ErrorException 예외를 사용해서 말입니다.

Exception 클래스는 개발자가 디버깅에 사용할 수 있는 정보를 그리 많이 제공하지는 않습니다.
하지만 이런 점을 보완하기 위해서 Exception 클래스를 상속해서 좀 더 구체적인 예외 클래스를 만들 수 있습니다.
class ValidationException extends Exception {}
이렇게 예외 클래스를 구체적으로 만들면 여러 개의 catch 문을 달아서 다른 종류의 예외를 서로 다르게 처리할 수 있게 됩니다

```
<?php
$email = new Fuel\Email;
$email->subject('My Subject');
$email->body('How the heck are you?');
$email->to('guy@example.com', 'Some Guy');

try
{
    $email->send();
}
catch(Fuel\Email\ValidationFailedException $e)
{
    // 데이터의 유효성 체크에 실패한 경우
}
catch(Fuel\Email\SendingFailedException $e)
{
    // 메일 전송을 시도했는데 성공하지 못한 경우
}
finally
{
    // 이 부분은 예외가 발생했는지 아닌지와 상관없이 항상 실행됨
}
?>
```


SPL 예외 https://www.php.net/spl.exceptions

예를 들어 __call() 특수 매서드(Magic Method)에 잘못된 메소드 호출이 들어온 상황을 처리할 때, 두루뭉실하게 그냥 Exception을 던지거나 Exception 클래스를 상속받은 예외 클래스를 작성해서 던지는 대신에 throw new BadMethodCallException; 이라고 할 수 있겠습니다.

예외처리를 거의 안하다 보니까 어떤 상황에 자주 쓰이는지도 잘 모르겠다.

LogicException에

function과 method, Domain, InvalidArgument, Length, OutOfRange 등...

RuntimeException에

OutOfBounds?, Overflow, Range, Underflow, UnexpectedValue 등...

```
<?php
// Here, use InvalidArgumentException
function media($x) {
    switch ($x) {
        case image:
            return 'PNG';
        break;
        case video:
            return 'MP4';
        break;
        default:
            throw new InvalidArgumentException ("Invalid media type!");
    }
}?>
This is completly diffirent situation than this:
<?php
// Here, use DomainException
$object = new Library ();
try {
    $object->allocate($x);
} catch (toFewMin $e) {
    throw new DomainException ("Minimal value to allocate is too high").
}
?>
The simillar situation, but problem occurs during runtime:
<?php
class library {
    function allocate($x) {
        if ($x<1000)
            throw new RangeException ("Value is too low!")
    }
}
?>
```


