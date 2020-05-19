출처 : https://devxoul.gitbooks.io/ios-with-swift-in-40-hours

#### 변수와 상수
변수 Variable은 값을 수정할수 있고, 상수 Constant는 그렇지 않습니다. Swift에서는 언제 어디서 값이 어떻게 바뀔지 모르는 변수보다는 상수를 사용하는 것을 권장하고 있습니다. 그쪽이 안전합니다 !

변수는 var로 선언하고,  상수는 let으로 선언합니다.

```
var name = "Juhyang Lee"
let birthyear = 1996
```

나중에 이름을 바꾸고 싶다면 바꿀수 있습니다.
```
name = "이주향"
```

하지만, 태어난 해를 바꾸려고 한다면 오류가 납니다.
```
birthyear = 2000 // 컴파일 에러 !!
```

```let``` 키워드로 선언된 상수의 값은 변경할 수 없습니다. 이렇게 바뀌면 안되는 값을 상수로 정의해두면 코딩하는데 조금은 마음을 놓을 수 있습니다.

Swift는 정적 타이핑 언어입니다. 변수나 상수를 정의할 때 그 자료형(타입)이 어떤 것인지를 명시해주어야 하는 언어입니다.
```
var name : String = "Juhyang Lee"
let birthyear : Int = 1996"
var height : Float = 200.1
```

```name```은 ```String```이고, ```birthday```는 ```Int```고, ```height```은 ```Float``` 타입이네요. 이렇게 변수 또는 상수 일므 뒤에 콜론(```:```)을 붙이고 자료형을 써주면 된답니다. 이 때 사용하는 ```: String```과 ```: Int``` 등을 가지고 타입 어노테이션 (Type Annotation)이라고 합니다.

Swift에서는 타입을 굉장히 엄격하게 다루기 때문에, 다른 자료형끼리는 기본적인 연산조차 되지 않습니다.
```
birthyear + height // 컴파일 에러 !
Float(birthyear) + height // 2196.1
String(birthyear) + name + "하이 !" // 1996Juhyang Lee 하이 !
"\(birthyear)\(name) 하이 !" // 1996Juhyang Lee 하이 !
```
#### 타입 추론 (Type Inference)

Kotlin 과 동일하게 타입 추론이 자동으로 된다 !

#### 배열(Array)과 딕셔너리 (Dictionary)

배열과 딕셔너리는 모두 대괄호 (```[]```)를 이용해서 정의할 수 있습니다.

```
var languages = ["Swift", "Objective-C", "Python"]
var capitals = [
  "한국" : "서울",
  "일본" : "도쿄",
  "중국" : "베이징",
]
```

배열과 딕셔너리에 접근하거나 값을 변경할 때에도 대괄호를 사용합니다.

```
languages[0] // Swift
languages[1] = "Ruby"

capitals["한국"] // tjdnf
capitals["프랑스"] = "파리"
```
참고로, 다른 상수와 마찬가지로 배열과 딕셔너리를 let 으로 정의하면 값을 수정할 수 없습니다. 물론 값을 추가하거나 빼는 것도 불가능합니다.

위에서 정의한 ```languages``` 와 ```capitals``` 의 타입은 대괄호를 사용합니다.

```
var languages : [String] = ["Swift", "Objective-C", "Python"]
var capitals : [String : String] = [
  "한국" : "서울",
  "일본" : "도쿄",
  "중국" : "베이징",
]
```

만약 빈 배열이나 빈 딕셔너리를 정의하고싶다면 대괄호를 씁니다

```
var languagse: [String] = []
var capitals : [String:String] = [:]

var languages = [String] ()
var capitals = [String:String] ()
```

#### 조건문과 반복문

조건을 검사할 때에는 ```if```, ```switch``` 를 씁니다

```
var age = 19
var student = ""

if age >= 8 && age < 14 {
  student = "초등학생"
} else if age < 17 {
  student = "중학생"
} else if age < 20 {
  student = "고등학생"
} else {
  student = "기타"
}

student // 고등학생
```

```if``` 문의 조건에는 항상 ```Bool``` 타입만 사용이 가능하다.

Swift 의 ```switch```는 패턴매칭이 가능하다.

```
switch age {
  case 8 ..< 14 :
    student = "초등학생"
  case 14 ..< 17 :
    student = "중학생"
  case 17 ..< 20 :
    student = "고등학생"
  default : 
    student = "기타"
}
```

반복자는 ```for```, ```while```

```
for language in languages {
  print ("저는 \(language) 언어를 다룰 수 있습니다.")
}

for (country, capital) in capitals {
  print ("\(country)의 수도는 \(capital)입니다.")
}

for i in 0 ..< 100 {
  i
}

for _ in 0 ..< 10 {
  print ("Hello")
}
```

#### 옵셔널 (Optioinal)

Swift가 가지고 있는 가장 큰 특징 중 하나가 바로 옵셔널(Optional)입니다. 직역하면 '선택적인'이라는 뜻이 되는데, 값이 있을수도 있고 없을수도 있는 것을 나타냅니다.

다른 언어에서의 ```null``` 은 Swift 에서는 ```nil``` 입니다.

값이 없는 경우를 나타낼 때 ```nil``` 을 사용합니다.
그렇다고 해서 모든 변수에 ```nil```을 넣을 수 있는것은 아닙니다.

값이 있을 수도 있고 없을 수도 있는 변수를 정의할 때에는 타입 어노테이션에 ```?```를 붙여야 합니다. 이렇게 정의한 변수를 옵셔널(Optional)이라고 합니다. 옵셔널에 초깃값을 지정하지 않으면 기본값은 ```nil``` 입니다.

```
var email : String?
print (email) // nil

email = "ljh28891004@gmail.com"
print (email) // Optional("ljh28891004@gmail.com")
```

#### 옵셔널 바인딩 (Optional Binding)

옵셔널의 값을 가져오고 싶을때는 옵셔널 바인딩(Optional Binding)을 사용해야 합니다.

옵셔널 바인딩은 옵셔널의 값이 존재하는지를 검사한 뒤, 존재한다면 그 값을 다른 변수에 대입시켜 줍니다. ```if let``` 또는 ```if var```를 사용하는데요. 옵셔널의 값을 벗겨서 값이 있다면 ```if```문 안으로 들어가고, 값이 ```nil```이라면 그냥 통과하게 됩니다.

```
if let email = optionalEmail {
  print (email) // optionalEmail의 값이 존재한다면 해당 값이 출력됩니다.
}
// optionalEmail의 값이 존재하지 않는다면 if 문을 그냥 지나칩니다.
```

하나의 ```if```문에서 콤마(```,```)로 구분하여 여러 옵셔널을 바인딩 할 수 있습니다. 이곳에 사용된 모든 옵셔널의 값이 존재해야 ```if```문 아능로 진입합니다.

```
var optionalName : String? = "이주향"
var optionalEmail : String? = "ljh28891004@gmail.com"

if let name = optionalName, email = optionalEmail {
  // name과 email 값이 존재
}
```

- Tip : 코드가 너무 길 경우에는 이렇게 여러 줄에 걸쳐서 사용하는 것이 바람직 합니다.
  ```
  if let name = optionalName,
    let email = optionalEmail {
      // name과 email 값이 존재
    }
  ```

  참고로, 두 번째 let 부터는 생략이 가능합니다.

위 코드는 아래 코드와 동일합니다.

```
if elt name = optionalName {
  if let email = optionalEmail {
    // name 과 email 값이 존재
  }
}
```

- Tip : 한 번의 if 문에서 여러 옵셔널을 바인딩할 수 있게 된 것은 Swift 1.2 버전부터입니다. 이전 버전까지는 바로 위와 같이 여러 번으로 감싸진 옵셔널 바인딩을 사용했습니다.

옵셔널 바인딩을 할 때 ```,```를 사용해서 조건도 함께 지정할 수 있습니다. ```,```이후의 조건절은 옵셔널 바인딩이 일어난 후에 실행됩니다. 즉, 옵셔널이 벗겨진 값을 가지고 조건을 검사하게 됩니다.

```
var optionalAge : Int? = 22

if let age = optionalAge, age >= 20 {
  // age의 값이 존재하고, 20 이상입니다.
}
```

위 코드는 아래 코드와 동일합니다.

```
if let age = optionalAge {
  if age >= 20{
    // age의 값이 존재하고, 20 이상입니다.
  }
}
```

#### 옵셔널 체이닝 (Optional Chaining)

Swift 코드를 간결하게 만들어주는 많은 요소들이 있는데, 옵셔널 체이닝(Optional Chaining)을 알게되면 다른 프로그래밍 언어가 조금 불편하게 느껴지는 경우가 생깁니다.

옵셔널 체이닝은 이해하는 데에는 설명보다 코드를 보는 편이 훨씬 좋습니다.

예컨데, 옵셔널로 선언된 어떤 배열을 떠올려봅시다. 이 배열이 '빈 배열' 인지를 검사하려면 어떻게 해야 할까요 ? nil 이 아니면서 빈 배열인지를 확인해보면 될것입니다. 이렇게요 !

```
let array : [String]? = []
var isEmptyArray = false

if let array = array, array.isEmpty {
  isEmptyArray = true
} else {
  isEmptyArray = false
}

isEmptyArray
```

옵셔널 체이닝을 사용하면 이 코드를 더 간결하게 쓸 수 있습니다.

```
let isEmptyArray = array?.isEmpty == true
```

혹시 감이 오시나요 ? 옵셔널 체이닝은 옵셔널의 속성에 접근할 때, 옵셔널 바인딩 과정을 ```?``` 키워드로 줄여주는 역할을 합니다.

- ```array```가 ```nil``` 인 경우
  ```
  array?isEmpty
  ~~~
  여기까지 실행되고 'nil'을 반환합니다.
  ```

- ```array```가 빈 배열인 경우
  ```
  array?.isEmpty
  ~~~~
  여기까지 실행되고 'nil'을 반환합니다.
  ```

- ```array```가 빈 배열인 경우
  ```
  array?.isEmpty
  ~~~
  여기까지 실행되고 'true'를 반환합니다.
  ```

```array?.isEmpty```의 결과로 나올 수 있는 값은 ```nil```, ```true```, ```false```가 됩니다. ```isEmpty```의 반환값은 ```Bool```인데, 옵셔널 체이닝으로 인해 ```Bool?```을 반환하도록 바뀐 것이죠. 따라서 값이 실제로 ```true```인지를 확인하려면, ```== true```를 해주어야 합니다.

#### 옵셔널 벗기기

옵셔널을 사용할 때마다 옵셔널 바인딩을 하는 것이 가장 바람직합니다. 하지만, 개발을 하다보면 분명히 값이 존재할 것임에도 불구하고 옵셔널로 사용해야 하는 경우가 종종 있는데요. 이럴 때에는 옵셔널에 값이 있다고 가정하고 값에 바로 접근할 수 있도록 도와주는 키워드인 ```!```을 붙여서 사용하면 됩니다.

```
print (optionalEmail) // Optional("ljh28891004@gmail.com")
print (optionalEmail!) // ljh28891004@gmail.com
```

```!```을 사용할 때에는 주의할 점이 있는데, 옵셔널의 값이 ```nil```인 경우에는 런타임 에러가 발생한다는 것입니다.

```
var optionalEmail : String?
print (optionalEmail!) // 런타임 에러 !
```

#### 압묵적으로 벗겨진 옵셔널 (Implicitly Unwrapped Optional)

만약, 옵셔널을 정의할 때 ```?``` 대신 ```!```를 붙이면 ```ImplicitlyUnwrappedOptional```이라는 옵셔널로 정의됩니다.

```
var email : String! = "lh28891004@gmail.com"
print (email) // ljh28891004@gmail.com
```

이렇게 정의된 옵셔널은 ```nil```을 포함할 수 있는 옵셔널이긴 한데, 접근할 때 옵셔널 바인딩이나 옵셔널을 벗기는 과정을 거치지 않고도 바로 값에 접근할 수 있다는 점에서 일반적인 옵셔널과 조금 다릅니다.

옵셔널 벗기기와 마찬가지로, 값이 없는데 접근을 시도하면 런타임 에러가 발생합니다.

```
var email : String!
print (email) // 런타임 에러
```

가급적이면 일반적인 옵셔널을 사용해서 정의하고, 옵셔널 바인딩 또는 옵셔널 체이닝을 통해 값에 접근하는 것이 더 바람직 합니다.
