# Cookie

쿠키, 세션, 캐시는 유사한 방식으로 작동한다.

즉, 세 가지 모두 같은 방식으로 값을 저장하고 조회할 수 있다.

그러나 쿠키는 본질적으로 요청과 응답에 첨부되는 것이므로 다른 방식으로 취급해야 한다.

어떤 점이 다른지 간단하게 알아보자.

# 라라벨에서의 쿠키

라라벨에 쿠키와 관련된 곳은 세 곳이다.

먼저 쿠키는 요청을 통해 들어올 수 있다.

이는 사용자가 페이지를 방문할 때 쿠키를 가지고 있다는 것을 의미한다.

Cookie 퍼사드를 이용하거나 요청 객체에서 빼내서 쿠키를 읽을 수 있다.

두 번째로 쿠키는 응답과 함께 내보낼 수 있다.

이는 응답이 사용자의 브라우저에게 다음 방문에 사용할 용도로 쿠키를 저장하라고 지시한다는 것을 뜻한다.

쿠키를 내보내려면 응답 객체를 반환하기 전에 쿠키를 응답 객체에 추가한다.

마지막으로 쿠키는 큐를 통해 처리할 수 있다.

Cookie 퍼사드를 이용해서 쿠키를 설정하면 쿠키가 CookieJar 큐에 들어간다.

큐에 추가된 쿠키는 AddQueuedCookiesToresponse 미들웨어에 의해 응답 객체에 추가된 뒤 큐에서 제거된다.

요청 객체에서 쿠키 읽기

```
Route::get('dashboard', function (Request $request) {
    $userDismissedPopup = $request->cookie('dismissed-popup', false);
})
```

cookie() 메서드는 파라미터 2개를 전달받을 수 있다.

첫 번째 파라미터는 쿠키명이고, 두 번째는 옵션 값으로 해당 파라미터의 값이 없는 경우 반환될 값이다.

응답 객체에 쿠키 설정하기

```
Route::get('dashboard', function () {
    $cookie = cookie('saw-dashboard', true);

    return Response::view('dashboard')->cookie($cookie);
})
```

