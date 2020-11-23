# Database

출처 : https://modernpug.github.io/php-the-right-way/

MySQL 익스텐션 

PHP의 MySQL익스텐션은 아주 오래되었고, 다음 두 익스텐션으로 대체되었습니다.

mysql 익스텐션 개발은 오래전에 개발 중단되었을 뿐만 아니라, PHP 5.5.0 부터는 공식적으로 사용을 권장하지 않는 상태(deprecated)였고, PHP 7.0에서는 공식적으로 제거 되었습니다.

현재 회사 프로젝트는 php 5.6에서 mysql과 mysqli를 병행하면서 사용하고 있다..

mysql에서도 이상한 클래스를 include하여 사용하고 있어서 소스가 더 난잡한듯..

레거시한 부분이 너무 많다면 개선하는 것보다 Laravel을 사용해서 처음부터 짜는 게 나을 것 같다..

근데 이또한 쉽지 않다.. ㅠㅠ

mysqli나 pdo를 추천하는데 pdo가 좀 더 좋아보인다.

```
<?php
// mysqli
$mysqli = new mysqli("example.com", "user", "password", "database");
$result = $mysqli->query("SELECT 'Hello, dear MySQL user!' AS _message FROM DUAL");
$row = $result->fetch_assoc();
echo htmlentities($row['_message']);

// PDO
$pdo = new PDO('mysql:host=example.com;dbname=database', 'user', 'password');
$statement = $pdo->query("SELECT 'Hello, dear MySQL user!' AS _message FROM DUAL");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['_message']);

// mysql
$c = mysql_connect("example.com", "user", "password");
mysql_select_db("database");
$result = mysql_query("SELECT 'Hello, dear MySQL user!' AS _message FROM DUAL");
$row = mysql_fetch_assoc($result);
echo htmlentities($row['_message']);
?>
```

PDO의 장점? 전략패턴인가..?
```
<?php
// PDO + MySQL
$pdo = new PDO('mysql:host=example.com;dbname=database', 'user', 'password');
$statement = $pdo->query("SELECT some_field FROM some_table");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['some_field']);

// PDO + SQLite
$pdo = new PDO('sqlite:/path/db/foo.sqlite');
$statement = $pdo->query("SELECT some_field FROM some_table");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['some_field']);
?>
```

데이터를 바인딩하고 필터링해서 안정적으로 사용하는 방법

<?php
$pdo = new PDO('sqlite:/path/db/users.db');
$stmt = $pdo->prepare('SELECT name FROM users WHERE id = :id');
$id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT); // <-- 먼저 데이터를 필터링 ([데이터 필터링](#data_filtering) 참고), INSERT, UPDATE 등에 특히 중요. 
$stmt->bindParam(':id', $id, PDO::PARAM_INT); // <-- PDO가 자동으로 SQL에서 위험한 요소 제거
$stmt->execute();
?>

PDO란? https://www.php.net/book.pdo

PHP Data Objects( PDO ) 확장은 PHP에서 데이터베이스에 액세스하기위한 경량, 일관성있는 인터페이스를 정의합니다. PDO 인터페이스를 구현하는 각 데이터베이스 드라이버는 데이터베이스 특정 기능을 일반 확장 기능으로 노출 할 수 있습니다. PDO 확장을 단독으로 사용하여 데이터베이스 기능을 수행 할 수 없습니다. 당신은 사용해야 데이타베이스 고유의 PDO 드라이버를 데이터베이스 서버에 액세스 할 수 있습니다.

