# PSR-1 기본 코딩 표준

* 파일은 <?php와 <?= 태그만 써야 한다.
* 파일은 BOM을 제외한 UTF-8만 써야 한다.
* 파일은 심볼(classes, functions, constants 등)을 선언하거나, 부작용(side-effects, 출력 생성, .ini 세팅 변경 등)을 발생시켜야 하고, 둘을 동시에 해서는 안 된다.
* 네임스페이스와 클래스는 반드시 오토로딩 PSR-4를 따라야 한다.
* 클래스 이름은 반드시 StudlyCaps 첫글자 대문자, 모든 이어지는 단어의 첫글자 대문자
* 클래스 상수는 반드시 모두 밑줄로 이어진 대문자로 선언한다.
* 메소드 이름은 반드시 camelCase로 선언한다. 모든 이어지는 단어의 첫글자 대문자

# PSR-2 코딩 스타일 가이드

* 코드는 반드시 PSR-1을 따라야 한다.
* 코드는 반드시 탭이 아닌 스페이스 4개로 들여쓰기해야 한다.
* 라인 길이에 엄격한 제한을 둘 필욘는 없다. 약하게 제한은 한 줄에 120자, 강하게 제한은 80자 이하
* 네임스페이스 선언 다음에는 반드시 한 줄을 띄워야 하고, use 선언 블록 다음에도 한 줄을 띄어야 한다.
* 클래스를 여는 중괄호는 반드시 다음 줄에서 시작해야 하고, 닫는 중괄호는 반드시 본문 다음 줄에서 닫아야 한다.
* 메소드를 여는 중괄호는 반드시 다음 줄에서 시작해야 하고, 닫는 중괄호는 반드시 본문 다음 줄에서 닫아야 한다.
* 가시성은 반드시 모든 프로퍼티와 메소드에 선언되어야 한다. Abstract와 final은 가시성 앞에 선언 되어야 하고, Static은 가시성 뒤에 선언되어야 한다.
* 제어 구조 키워드는 반드시 한 칸 띄워야 한다. 메소드와 함수 호출은 그렇지 않다.
* 제어 구조를 여는 중괄호는 반드시 같은 라인에 있어야 하고, 닫는 중괄호는 본문 다음 줄에 있어야 한다.
* 제어 구조를 여는 괄호 뒤에는 반드시 칸을 띄우지 않고, 닫는 괄호 앞은 반드시 칸을 띄우지 않는다.

# Example
```
<?php

namespace Vendor\Package;

use FoolInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\Bazclass;

class Foo extends Bar implements FoolInterface
{
	public function sampleFunction($a, $b = null)
	{
		if ($a === $b) {
			bar();
		} else if ($a > $b) {
			$foo->bar($arg1);
		} else {
			BazClass::bar($arg2, $arg3);
		}
	}

	final public static function bar()
	{
		// method body
	}
}

?>
```