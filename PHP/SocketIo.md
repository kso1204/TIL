# Socket.Io

https://laravel.kr/docs/8.x/broadcasting#Socket.IO

socket.Io 기능을 위해..

https://medium.com/@jan.kulma/laravel-broadcasting-with-redis-and-socket-io-51ce2660633d

Note that Socket.IO !== WebSockets, but it uses it under the hood. If you’re interested, check this out https://en.wikipedia.org/wiki/Socket.IO. I’m just using term “WebSockets” for the sake of simplicity.


laravel-echo-server 설정파일인데 여기서 protocol https->http로 변경했다.

https or http 둘 중 하나만 지원한다고 되어 있는데.. ssl 인증서 경로 안 넣었더니 오류가 생기길래 저 부분 변경했더니 됨


```
{
	"authHost": "http://project_2.test/",
	"authEndpoint": "/broadcasting/auth",
	"clients": [],
	"database": "redis",
	"databaseConfig": {
		"redis": {},
		"sqlite": {
			"databasePath": "/database/laravel-echo-server.sqlite"
		}
	},
	"devMode": true,
	"host": null,
	"port": "6001",
	"protocol": "http",
	"socketio": {},
	"secureOptions": 67108864,
	"sslCertPath": "",
	"sslKeyPath": "",
	"sslCertChainPath": "",
	"sslPassphrase": "",
	"subscribers": {
		"http": true,
		"redis": true
	},
	"apiOriginAllow": {
		"allowCors": false,
		"allowOrigin": "",
		"allowMethods": "",
		"allowHeaders": ""
	}
}
```

```
ioredis] Unhandled error event: Error: connect ECONNREFUSED 127.0.0.1:6379
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1141:16)
```

ssl 설정은 끝나도 새로운 오류.. 127.0.0.1 6379 127.0.0.1이 아니고 redis로 변경되면 될려나..

흠 방법을 못 찾겠다 ㅠㅠ

https://medium.com/sjk5766/laravel-broadcast-redis-%ED%8E%B8-74be51464a19

이걸 보고 한발짝 더 왔는데도 안 된다..

아무리 찾아도 redis에 관련한 오류를 해결할 수가 없다..

laravel-echo-server databaseconfig쪽 설정을 host주는 부분에서 redis가 들어가야 정상적으로 연결 되는 것 같은데

이 부분이 나만 막히는 것 같다.. 처음부터 다시 해봐도 안 되고 도커 설정이나 이런 부분들이 뭐가 달라서

안 되는 것 같은데.. ㅠㅠㅠ 사수가 절실하다