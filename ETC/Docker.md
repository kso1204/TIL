# Docker

laravel을 처음 시작할 때 localhost에서 작업하다가 규모가 있는 패키지를 설치하려면 필요한 내용들이 많아서

homestead vagrant환경에서 간단한 프로젝트를 진행했습니다.

프로젝트를 회사 데스크탑, 집 데스크탑, 집 노트북 세 가지의 Windows 10 환경으로 진행했는데

노트북에서 vagrant 설치가 느려서 이것저것 찾아보고 아키텍쳐에 대해서 좀 찾아볼일이 생겨서

Docker에 입문하게 되었습니다.

Laravel + Docker의 기능이 있는 Laradock으로 처음에 시작했는데 컨테이너를 띄우는데 처음에 시간이 오래 걸리고

이미 삽입되어 있는 내장 이미지들이 너무 많이 있어서 무겁다는 생각을 했고.. 그래도 다 있는게 좋으니까 그냥 써보려다가

오픈채팅방에서 laradock을 안 쓰고 dockerfile 만들어서 사용한다고 하여 시도해봤습니다.

처음에는.. window에서 ubuntu이미지만 만들고 그 안에서 작업하면 될까 생각해서 그러한 도커파일 예제들을 찾아서 작업해보다가

현재는 docker-file로는 php-fpm만 실행하고 php, mysql, redis, phpMyAdmin, nginx를 사용하는 docker-compose.yml 파일로 구성중입니다.

php artisan 명령어를 사용할 때 도커 컨테이너를 사용했기 때문에.. git bash shell에서 정상적으로 적용되지 않았고

이상하게 사용하다가(Docker-compose exec php php./game/artisan migrate) 이런식으로.. 

그러다가 문제가 생겨서 또 질문했더니 winpty docker-compose exec php sh에서 작업하는 방법을 알려주셨고.. 이렇게 이용중입니다.

웬만한 기능들은 다 됐었는데, Redis를 사용하려고 보니까 여러 문제들이 생겼고 연쇄되는 에러들을 해결하기 어려운 상황에 놓였습니다.

이 문제를 해결하기 위해..

윈도우에서 wsl2를 사용하여 ubuntu환경으로 작업하는 방법도 있는 것 같고.. ubuntu 이미지를 사용해서 작업하는 방법도 있는 것 같은데 어떻게 해야할지..

도커를 사용하는 여러 방법 중 한 가지라도 제대로 알면 어느 방법을 사용해도 될 것 같지만..

한 가지를 제대로 모르고 사용하니까 너무 헷갈린다 많은 글을 봐도 궁금증이 풀리지 않음..

https://stackoverflow.com/questions/54226604/how-to-add-php-redis-for-a-dockerfile-of-laravel-to-kubernetes

dockerfile에서 설정하는 게 있어서 이대로 해보려고 하는데..

docker-compose build 명령어를 또 그새 까먹어서 헤매고 있었다.

