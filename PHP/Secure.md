# Secure

출처 : https://modernpug.github.io/php-the-right-way/

데이터 필터링 https://www.php.net/book.filter

외부로부터의 입력은 절대(절대로) 믿어서는 안됩니다. 
외부에서 입력 받은 데이터를 사용하기 전에는 반드시 검증하고 위험한 요소를 제거해야 합니다.
filter_var()와 filter_input() 함수를 사용하여 텍스트에서 위험한 내용을 제거하고, 규칙(메일 주소 등)에 맞는지 검증할 수 있습니다.

https://www.php.net/manual/en/filter.filters.validate.php



외부 입력으로 받은 문자열에서 위험하거나 필요없는 문자열을 제거하거나 이스케이프처리 하는 일을 Sanitization 이라고 합니다.
예를 들어 외부 입력 데이터를 HTML이나 SQL 쿼리에 넣기 전에 반드시 위험한 요소를 제거해야합니다. PDO의 파라미터 바인딩을 사용한다면 PDO가 자동으로 그러한 처리를 해 줍니다.

Validation is used to validate or check if the data meets certain qualifications. For example, passing in FILTER_VALIDATE_EMAIL will determine if the data is a valid email address, but will not change the data itself.


Validate filters로 사용할 수 있는 인자

FILTER_VALIDATE_EMAIL

이메일, float, int, ip, MAC주소, regexp<--정규식?, url, domain, boolean 등


Sanitization will sanitize the data, so it may alter it by removing undesired characters. For example, passing in FILTER_SANITIZE_EMAIL will remove characters that are inappropriate for an email address to contain. That said, it does not validate the data.


Sanitize filters로 사용할 수 있는 인자

FILTER_SANITIZE_EMAIL

이메일,encoded, masic_quotes(addslashes()), number_float, number_int, special_chars(특수문자-AscII32보다 작은것), full_special_chars(htmlspecialchars()), string, url, raw 등..

Sanitizer Example

```
<?php
$a = 'joe@example.org';
$b = 'bogus - at - example dot org';
$c = '(bogus@example.org)';

$sanitized_a = filter_var($a, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_a, FILTER_VALIDATE_EMAIL)) {
    echo "This (a) sanitized email address is considered valid.\n";
}

$sanitized_b = filter_var($b, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_b, FILTER_VALIDATE_EMAIL)) {
    echo "This sanitized email address is considered valid.";
} else {
    echo "This (b) sanitized email address is considered invalid.\n";
}

$sanitized_c = filter_var($c, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_c, FILTER_VALIDATE_EMAIL)) {
    echo "This (c) sanitized email address is considered valid.\n";
    echo "Before: $c\n";
    echo "After:  $sanitized_c\n";    
}
?>
```

