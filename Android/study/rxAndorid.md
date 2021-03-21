## Reactive Programming

#### 1. RX? - Reactive Programming

-   컴퓨터 프로그램의 세가지 종류
    -   주어진 입력 값을 바탕으로 결과를 계산하는 변환 프로그램이며 일반적으로 컴파일러와 수치 계산을 하는 프로그램
    -   상호작용 프로그램으로 프로그램이 작업을 주도하며 사용자 혹은 다른 프로그램과 상호작용을 한다. 사용자의 관점에서 볼때는 흔히 말하는 시분할 시스템은 상호작용 프로그램이다.
    -   리액티브 프로그램은 **프로그램 자산의 주변 환경과 끊임없이 상호작용을 하는데 프로그램이 주도하는 것이 아니라 환경이 변하면 이벤트를 받아 동작한다.**

즉. 근래에 떠오르고 있는 Reactivr Programming는 데이터의 흐름과 전달에 관한 프로그래밍 패러다임이라고 볼 수 있다.

1. 왜 사용할까 ?

    - 개발적인 측면에서 보면 간단하다.
    - 개발자들은 UX를 향상시키고 싶어 한다.
    - 이를 위해서는 메인스레드가 멈추거나 느려지지 않도록 해야하며 사용자들에게 부드러운 사용자 앱 경험을 제공하고 싶어한다.
    - 하지만 메인 스레드를 자유롭게 핸들링 하면서 유지하려면 무겁고 시간이 오래 걸리는 작업은 백그라운드에서 해야 한다. 그리고 백그라운드에서 조차 무겁고 복잡한 계산 작업이라면 서버에서 수행하는 것이 Best 이다. 그렇기 때문에 **네트워크 운영을 위한 비동기 작업이 필요하다.**

2. 비동기 작업은 AsyncTask 가 있음 !

    - **현재 버전에서는 Deprecated 되었음.** 다른 비동기 처리 라이브러리를 사용해야함.
    - 항상 앱에서 문제가 생기는 부분은 서버로부터 데이터를 가져오는 길고 긴 백그라운드 작업이다. 네트워크 작업은 시간이 짧다면 상관이 없지만 오래 걸리는 상황이 잦기 때문에 비동기적으로 서버에 요청하고 데이터를 받아서 UI 업데이트를 하는것이 중요하다. 하지만 네트워크 요청이 완료 될 때 UI와 관련 된 부분에 어떠한 문제가 있어 더 이상 존재하지 않거나 에러가 발생하여 충돌 또는 버그가 발생할 수 있는 근본적인 문제가 있다. 이건 일반적인 스레드 프로그래밍이 가지고 있는 위험성과 크게 다르지 않다.
    - AsyncTask 는 전체적인 프로세스를 단순화 하지만 **안드로이드의 생명주기를 신경쓰지 않는다.** 그렇기 때문에 **액티비티나 프레그먼트가 안드로이드 생명주기에 의해 재생성되거나 파괴되었을 때 마무리 자겅벵 대한 내용이 보호되지 않는 불편한 점이 있다.**

3. 명령형 프로그래밍과 다르다

    - 명령형 프로그래밍(Imperative Programming) - 작성된 코드가 정해진 순서대로 실행 됨.
    - 리액티브 프로그래밍(Reactive Programming) - 데이터 흐름을 먼저 정의하고 데이터가 변경되었을 때 연관되는 함수나 메서드가 업데이트 되는 방식.

4. 그래서 ReactiveX 등장
    - [ReactiveX](http://reactivex.io/intro.html)는 **비동기 프로그래밍과 Observable 시퀀스를 이용해 이벤트를 처리하기 위한 라이브러리 이다.**

#### 2. RxKotin, RxAndroid 도 같은 맥락인가 ?

-   사실 현재 많은 리액티브 관련 라이브러리가 나와있는데 대부분 ReactiveX를 사용하기 때문에 RxKotlin, RxJava, RxAndroid, RxSwift 등 들은 서로 다른 것이 아니라 하나의 ReactiveX Extensions로 보면 된다.

    -   **RxJava : Java(JVM)을 위한 ReactiveX Extensions. Reactive Programming(리액티브 프로그래밍) 패러다임을 자바에서 구현** 한 프로그래밍 라이브러리
    -   **RxKotlin : Kotlin을 위한 ReativeX Extensions.** RxJava 라이브러리를 기반으로 포팅하여 **코틀린을 위한 리액티브 프로그래밍의 특정 부분을 함수형 프로그래밍으로써 구현**한 라이브러리
    -   **RxAndroid : Android를 위한 ReactiveX Extensions.** RxJava에 최소한의 클래스를 추가하여 \*\*안드로이드 앱에서 리액티브 구성요소를 쉽고 간편하게 사용하게 만드는 라이브러리
    -   \*\*RxSwift : Swift를 위한 Reactive Extensions

위의 ReactiveX Extensions 에는 공통점이 있습니다.

-   효율적으로 신속하게 비동기 처리를 도와줌
-   함수형 프로그래밍을 일부 지원함
-   \*\*옵저버 패턴(Observer pattern)을 사용함
-   콜백(Callback)에서 또 콜백을 하는 지옥에서 벗어날 수 있다.

하지만 단점 : 러닝커브가 가파르기에 진입장벽이 높다.

참고 - https://velog.io/@jojo_devstory/Android-RxKotlin-RxAndroid란-Reactive-Programing

### Observable

#### 1. Observable 이란? (https://jeongupark-study-house.tistory.com/40)

-   ReactiveX는 옵저버패턴을 사용하기 때문에 rx의 Observer는 Observable을 구독하게 된다. Observable이 emit하는 하나 혹은 연속된 item에 대해 Observer에게 알림을 보냅니다. RxJava는 Observable의 시작이면서 Observable의 끝이라고 할 정도로 중요한 개념입니다.
-   Obserbale 은 onNext, onError, onComplete의 세가지 알림을 구독자에게 전달합니다.

    -   onNext : Observable이 데이터 발행을 알림
    -   onError : error가 발생했음을 알리고 Observable을 종료
    -   onComplete : 모든 이벤트가 발행을 완료했음을 알린다. 이벤트가 발생한 후 onNext를 발행해서는 안된다.

-   just() 함수

    -   just 함수는 Observable 을 생성하는 가장 간단한 방법이다. 한 개의 값을 넣을 수도 있고, 여러개를 넣을 수 도 있다. (단 같은 타입이어야 한다.)

    ```kotlin
    fun main() {
        Observable.just(1, 2, 3, 4, 5).subscribe(System.out::println)
    }
    ```

위의 code를 보면 just를 통하여 Observable을 생성하고 데이터 1, 2, 3, 4, 5를 넣는다. 그리고 subscribe를 넣은 데이터들을 발행한다.

-   subscribe() 함수

    -   RxJava는 실제로 실행되기 위해서 사용하는 함수는 subscribe 함수 입니다. just등으로 데이터 흐름을 정한 후 subscribe 함수를 호출해야 실제로 데이터를 발행한다.
    -   subscribe() 함수를 보면 모두 Disposable 인터페이스 객체를 리턴하고 있다. Disposable 인터페이스는 dispose() 함수와 isDisposed() 두가지가 있는데, dispose() 함수는 Observable에게 더 이상 데이터를 발행하지 않도록 구독을 해지하는 함수이다.
    -   위에서 Observable이 onComplete()을 호출할 경우 자동으로 dispose()를 호출해 Observable과 구독자의 관계를 끊는다. 그러므로 Observable이 정상적으로 onComplete로 종료가 되면 dispose를 호출할 필요가 없다.

-   onCreate()

    -   just는 데이터를 인자로 넣으면 자동으로 알림 이벤트가 발생하지만 create는 onNext, onComplete, onError 같은 알림을 개발자가 직접 호출해야 합니다.

        ```kotlin
        Observable.create<Integer> {
            it.onNexx(100 as Integer)
            it.onNext(200 as Integer)
            it.onNext(300 as Integer)
        }.subscribe { data -> println(data)}
        ```

    -   위 code를 보면 it은 ObservableEmitter로 람다 형식으로 간소하게 작성함. 그리고 as Integer를 하지 않을 경우 `the integer literal does not conform to the expected type integer`로 에러가 발생하기 때문에 사용. 그리고 data는 변수이므로 원하는 이름으로 작성하면 된다.
    -   onCreate 사용시 주의할 점은
        -   Observable이 구독 해지 되었을 때 등록된 콜백을 모두 해제해야 한다. 그렇지 않으면 메모리 누수가 발생한다.
        -   구독자가 구독하는 동안에만 onNext, onComplete 이벤트를 호출해야 한다.
        -   에러 발생 시 오직 onError 이벤트로만 에러를 전달해야 한다.
        -   배압을 직접 처리해야 한다.

-   fromArray()

    -   just와 onCreate()는 단일 데이터를 다룬다. 그럼 단일 데이터가 아닐 때는 어떻게? fromXXX() 함수를 사용하면 된다.

    ```kotlin
    fun main () {
        val arr = arrayOf(100, 200, 300)
        val source = arr.toObservable()
        source.subscribe {
            println(it)
        }
    }
    ```

##### Observable, Observer 차이

1. Observable

    - 데이터 스트림을 의미하고 옵저버는 이 데이터 스트림을 구독함
    - onClickListener가 가장 쉬운 대표적인 오벚버 패턴의 예
    - 데이터 발행, 발행의 완료, 발행 중 에러 발생 등의 이벤트를 구독하고 있는 Observer들에게 알림
    - **Observerable 의 데이터들을 만들고, 분별하여 걸러내고, 조합하는 수많은 오퍼레이터들은 데이터 흐름 상태를 알려주는 함수(onSuccess, onError, onSubscribe, onComplete)와는 별개로 생각해야함.**
    - coldObservable은 subscribe 함수를 호출해야 그때서야 데이터를 발행함.

2. Observer
    - Observable에 의해 방출된 데이터를 소비하는 주체이고 액션을 취할 수 있음
    - Observable에 등록된 Observer는 Observable이 데이터를 방출 할때마다 알맞은 onNext onError onSubscribe 등의 메서드를 통해 해당 결과를 처리할 수 있음.

##### RxJava 스케줄러

-   데이터 흐름이 발생하는 쓰레드와 처리된 결과를 구독자에게 전달하는 쓰레드를 분리할 수 있음
-   스케줄러를 별도로 지정하지 않으면 메인 쓰레드가 기본값
-   subscribeOn 쓰레드를 지정하고 onserveOn쓰레드를 지정하지 않으면 observeOn 쓰레드는 subscribeOn 쓰레드를 따라감

1. newThread()

    - 새로운 별도의 쓰레드를 생성하여 작업을 함
    - 두 개의 옵저버블 쓰레드를 지정한다고 치면 둘은 서로 관여를 아예 안함

2. single()

    - SingleThreadPool을 사용
    - RxJava내부에서 단일 쓰레드를 생성하여 구독작업을 처리함
    - 여러번 구독요청이 와도 쓰레드 하나를 사용, 순서 보장

3. computation()

    - 계산 작업 때 사용하고 별도의 I/O가 없는 스케줄러
    - 코어 개수만큼 thread pool을 만들어 사용함
    - interval 함수는 기본적으로 계산 스케줄러를 사용

4. io()

    - 내부적으로 cachedPool을 사용, thread가 동시에 계속 늘어나면서 생성될 수 있음
    - 네트워크 작업을 비롯한 각종 비동기 I/O 작업을 위한 스케줄러
    - 필요할 때마다 쓰레드를 계속 생성

5. tranpoline()

    - 호출을 수행한 thread를 이용해 수행
    - 새로운 쓰레드를 생성하지 않고 단일 쓰레드이고 Queuing 되어 여러 작업 요청에도 순서가 보장됨
    - 하지만 Queuing 작업이 끝나야만 다음 코드라인이 수행될 수 있음

6. Scheduler.from(executor)

    - Excutor를 전달해 새로운 스케쥴러를 생성할 수 있음

7. mainThread()

    - RxAndorid 사용 시 mainThread에서 수행하기 위한 스케줄러

8. HandlerScheduler.from(handler)
    - 특정 핸들러에 의존하여 동작합니다.
