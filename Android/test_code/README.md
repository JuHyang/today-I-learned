# JUnit

### 단정문

-   assertArrayEquals(a, b) : 배열 a와 b가 일치함을 확인
-   assertEquals(a, b) : 객체 a와 b의 값이 같은지 확인
-   assertSame(a, b) : 객체 a와 b가 같은 객체임을 확인
-   assertTrue(a) : a가 참인지 확인
-   assertNotNull(a) : a 객체가 null이 아님을 확인

이외에도 다른 단정문들이 존재한다.
http://junit.sourceforge.net/javadoc/org/junit/Assert.html

### 어노테이션 활용

-   테스트 메소드
    -   @Test가 메소드 위에 선언되면 이 메소드는 테스트 대상 메소드임을 의미한다.
-   테스트 메소드 수행시간 제한하기
    -   @Test(timeout = 5000)를 메소드 위에 선언합니다. 시간단위는 밀리 초 이다. 이 테스트 메소드가 결과를 반환하는데 5000 미리 초를 넘긴다면 이 실패하는 것이다.
-   테스트 메소드 Exception 지정하기
    -   @Test(expected=RuntimeException.class)가 메소드 위에 선언되면 이 테스트 메소드는 RuntimeException이 발생해야 테스트가 성공, 그렇지 않으면 실패하는 것이다.
-   초기화 및 해제
    -   @BeforeClass, @AfterClass 가 메소드 위에 선언되면 해당 테스트 클래스에서 딱 한번씩만 수행되도록 지정하는 어노테이션이다.
    -   @Before, @After 가 메소드 위에 선언되면 해당 테스트 클래스 안에 메소드들이 테스트 되기 전과 후에 각각 실행되게 지정하는 어노테이션이다.
