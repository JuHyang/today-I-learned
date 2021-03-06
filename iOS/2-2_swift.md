출처 : https://devxoul.gitbooks.io/ios-with-swift-in-40-hours

#### 함수와 클로저

함수는 ```func``` 키워드를 사용해서 정의합니다. ```->``` 를 사용해서 함수의 반환 타입을 지정합니다.

```
func hello (name : Stirng, time : Int) -> String {
    var string = ""
    for _ in 0 ..< time {
        string += "\(name)님 안녕하세요!\n"
    }
    return string
}
```

Swift에서는 독특하게 함수를 호출할 때 파라미터 이름을 함께 써주어야 합니다.

```
hello (name : "이주향", time : 3)
```

만약, 함수를 호출 할 때 사용하는 파라미터 이름과 함수 내부에서 사용하는 파라미터 이름을 다르게 사용하고 싶으면 이렇게 할 수 있습니다.

```
func hello (to name : String, numberOfTimes time : Int) {
    // 함수 내부에서는 'name'과 'time'을 사용합니다.
    for _ in 0 ..< time {
        print (name)
    }
}

hello (to: "이주향", numberOfTimes : 3) // 이곳에서는 'to' 와 'numberOfTimes' 를 사용합니다.
```

파라미터 이름을 ```_```로 정의하면 함수를 호출할 때 파라미터 이름을 생략할 수 있게 됩니다.

```
func hello (_ name : String, time : Int) {
    // ...
}

hello ("이주향", time : 3) // 'name :'이 생략되었습니다.
```

파라미터에 기본 값을 지정할 수도 있습니다. 기본 값이 지정된 파라미터는 함수 호출 시 생략할 수 있습니다.

```
func hello (name : String, time : Int = 1) {
    // ...
}

helllo ("이주향")
```

```...``` 을 사용하면 개수가 정해지지 않은 파라미터(variadic Parameters) 를 받을 수 있습니다.

```
func sum (_ numbers : Int...) -> Int {
    var sum = 0
    for number in numbers {
        sum += number
    }
    return sum
}

sum (1, 2)
sum (3, 4, 5)
```

함수 안에 함수를 또 작성할 수도 있습니다.

```
func hello (name : String, time : Int) {
    func message (name : String) -> String {
        return "\(name)님 안녕하세요 !"
    }

    for _ in -..< time {
        print (message (name : name))
    }
}
```

심지어 함수 안에 정의한 함수를 반환할 수도 있습니다.

```
func helloGenerator (message : String) -> (String) -> String {
    func hello (name : String) -> String {
        return name + message
    }
    return hello
}

let hello = helloGenerator (message : "님 안녕하세요 !")
hello ("이주향")
```

여기서 핵심은, ```helloGenerator()``` 함수의 반환 타입이 ```(String) -> String``` 라는 것입니다. 즉, ```helloGenerator()```는 '문자열을 받아서 문자열을 반환하는 함수'를 반화하는 함수인 것이죠.

만약 ```helloGenerator()``` 안에 정의한 ```hello()``` 함수가 여러개의 파라미터를 받는다면 이렇게 써야 합니다.

```
func helloGenerator (message : String) -> (String, String) -> String {
    fun hello (firstName : String, lastName : String) -> String {
        return lastName + firstName + message
    }
    return hello
}

let hello = helloGenerator (message : "님 안녕하세요!")
hello ("주향", "이")
```

#### 클로저 (Closure)

클로저(Closure)를 사용하면 바로 위에 작성한 코드를 조금 더 간결하게 만들 수 있습니다. 클로저는 중괄호 (```{}```)로 감싸진 '실행 가능한 코드 블럭' 입니다.

```
func helloGenerator (message : String) -> (String, String) -> String {
    return { (firstName : String, lastName: String) -> String in
        return lastName + firstName + message
    }
}
```

함수와는 다르게 함수 이름 정의가 따로 존재하지 않습니다. 하지만 파라미터를 받을 수 있고, 반환 값이 존재할 수 있다는 점에서 함수와 동일하빈다. 함수는 이름이 있는 클로저입니다.

클로저는 중괄호 (```{}```)로 감싸져 있습니다. 그리고 파라미터를 괄호로 감싸서 정의하고, 함수와 마찬가지로 ```->```를 사용해서 반환 타입을 명시합니다. 조금 다른 점은 ```in```키워드를 사용해서 파라미터, 반환 타입 영역과 실제 클로저의 코드를 분리하고 있습니다.

```
{ (firstName) : String, lastName : String) -> String in
    return lastName + firstName + message
}
```

얼핏 봐서는 별로 간결하다는 느낌을 못받습니다. 클로저의 장점은 간결함과 유연함에 있습니다.

Swift 컴파일러의 타입 추론 덕분에, helloGenerator() 함수에서 반환하는 타입을 가지고 클로저에서 어떤 파라미터를 받고 어떤 타입을 반환하는지를 알 수 있습니다. 생략이 가능합니다.

```
func helloGenerator (message : String) -> (String, String) -> String {
    return { firstName, lastName in 
        return lastName + firstName + message
    }
}
```

훨씬 깔끔해졌죠 ? 놀라운 사실은 여기서 생략할 수 있다는 게 더 있다는 사실입니다. 마찬가지로 타입 추론 덕분에 첫 번째 파라미터가 문자열이고, 두 번째 파라미터도 문자열이라는 것을 알 수 있습니다. 첫 번째 파라미터는 ```$0```, 두 번째 파라미터는 ```$1```로 바꿔서 쓸 수 있습니다.

```
func helloGenerator (message : String) -> (String, String) -> String {
    return {
        return $1 + $0 + message
    }
}
```

클로저 내부의 코드가 한 줄 이라면, return 까지도 생략해버릴 수 있습니다 !

```
func helloGenerator (message : String) -> (String, String) -> String {
    return { $1 + $0 + message }
}
```

클로저는 변수처럼 정의할 수 있습니다.

```
let hello : (String, String) -> String = { $1 + $0 + "님 안녕하세요 !" }
hello ('주향", "이")
```

물론 옵셔널로도 정의할 수 있습니다. 옵셔널 체이닝도 가능합니다.

``` let hello : ((String, Stirng) -> String)?
hello? ("주향", "이")
```

클로저를 변수로 정의하고 함수에서 반환할 수도 있는 것처럼, 파라미터로도 받을 수 있습니다.

```
func manipulate (number : Int, using block : Int -> Int) -> Int {
    return block (number)
}

manipulate (number : 10, using : { (number : Int) -> Int in
    return number * 2 
})
```

아까 했던 것처럼, 생략할 수도 있습니다.

```
manipulate (number : 10, using : {
    $0 * 2
})
```

이런 구조로 만들어진 예시가 바로 ```sort()``` 와 ```filter()``` 입니다. 함수가 클로저 하나만을 파라미터로 받는다면, 괄호를 아예 쓰지 않아도 됩니다.

```
let numbers = [1, 3, 2, 6, 7, 5, 8, 4]

let sortedNumbers = numbers.sort { $0 < $1 }
print (sortedNumbers) // [1, 2, 3, 4, 5, 6, 7 ,8]

let evens = numbers.filter{ %0 % 2 == 0 }
print (evens) // [2, 6, 8, 4]
```

#### 클로저 활용하기

클로저는 Swift의 굉장히 많은 곳에서 사용됩니다. 바로 위에서 예시를 든 것처럼 ```sort()``` 나 ```filter()``` 와 같은 배열에 많이 쓰입니다. 대표적인 메서드로는 ```sort()```, ```filter()```, ```map()```, ```reduce()```가 있습니다. ```sort()```와 ```filter()```는 바로 위에서 써봤으니 ```map()```과 ```reduce()```를 봅니다.

```map()```은 파라미터로 받은 클로저를 모든 요소에 실행하고, 그 결과를 반환합니다. 예를 들어, 정수 배열의 모든 요소들에 2를 더한 값으로 이루어진 배열을 만들고 싶다면, 이렇게 작성할 수 있습니다.

```
let arr1 = [1, 3, 6, 2, 7, 9]
let arr2 = arr1.map { $0 * 2 } // [2, 6, 12, 4, 14, 18]
```

```reduce()``` 는 초깃값이 주어지고, 초깃값과 첫 번째 요소의 클로저 실행 결과, 그리고 그 결과와 두 번째 요소의 클로저 실행 결과, 그리고 그 결과와 세 번째 요소의 실행 결과, ... 끝까지 실행한 후의 값을 반환합니다. 바로 위에서 정의한 ```arr1```의 모든 요소의 합을 구하고 싶다면, 아래와 같이 작성할 수 있습니다.

```
arr1.reduce(0) { $0 + $1 } // 28
```

첫 번째 인자로 주어진 0부터 시작해서, 각 요소들과의 주어진 클로저에 대한 실행 결과를 바로 다음 요소와 실행합니다. 처음에는 0과 1을 더해서, 그 결과인 1과 3을 더해서4, 그리고 4와 6을 더해서 10, 10과 2를 더해서 12, 12와 7을 더해서 19, 19와 9를 더해서 28이 반환됩니다.

- Tip : Swift에서는 연산자도 함수이빈다. 함수는 곧 클로저이기 때문에 연산자는 클로저입니다. 1 + 2 를 실행하면, ```+```라는 이름을 가진 연산자 함수가 실행됩니다. 파라미터로는 1과 2가 넘겨지게 됩니다. 즉, ```+``` 함수는 파라미터 두 개를 받아서 합을 반환하는 클로저입니다. ```{ $0 + $1 }``` 인거죠. 그렇기 때문에, 이런 문법도 가능해집니다. ```+```라는 연산자를 클로저로 넘겨버리는 거죠.
    ```
    arr1.reduce(0, +) // 28
    ```

#### 클래스와 구조체

클래스(Class)는 ```class```로 정의하고, 구조체(Structure)는 ```struct```로 정의합니다.

```
class Dog {
    var name : String?
    var age : Int,

    func simpleDescription() -> String {
        if let name = self.name {
            return "🐶 \(name)"
        } else {
            return "🐶 No name"
        }
    }
}

struct Coffee {
    var name : String?
    var size : String?

    func simpleDescription() -> String {
        if let name = self.name {
            return "☕️ \(name)"
        } else {
            return "☕️ No name"
        }
    }
}

var myDog = Dog()
mydog.name = "찡코"
myDog.age = 3
print (myDog.simpleDescription()) // 🐶찡코

var myCoffee = Coffee()
myCoffee.name = "아메리카노"
myCoffee.size = "Venti"
print (myCoffee.simpleDescription()) // ☕️ 아메리카노
```

클래스는 상속이 가능합니다. 구조체는 불가능합니다.

```
class Animal {
    let numberOfLets = 4
}

class Dog : Animal {
    var name : String?
    var age : Int?
}

var myDog = Dog()
print (myDog,.numberOfLegs) // Animal 클래스로부터 상속받은 값 (4)
```

클래스는 참조(Reference)하고, 구조체는 복사(Copy)합니다.

```
var dog1 = Dog()	// dog1은 새로 만들어진 Dog() 를 참조합니다.
var dog2 = dog1		// dog2는 dog1이 참조하는 Dog()를 똑같이 참조합니다.
dog1.name = "찡코"	// dog1의 이름을 바꾸면 Dog()의 이름이 바뀌기 때문에,
print (dog2.name)	// dog2의 이름을 가져와도 바뀐 이름 ("찡코")이 출력됩니다.

var coffee1 = Coffee()		// coffee1은 새로 만들어진 Coffee() 그 자체입니다.
var coffee2 = coffee1		// coffee2는 coffee1을 복사한 값 자체입니다.
coffee1.name = "아메리카노"	// coffee1의 이름을 바꿔도
coffee2.name				// coffee2는 완전히 별개이기 때문에 이름이 바뀌지 않습니다. (nil)
```

#### 생성자 (Initializer)

클래스와 구조체 모두 생성자를 가지고 있습니다. 생성자에서는 속성의 초깃값을 지정할 수 있습니다.

```
class Dog {
	var name : String?
	var age : Int?

	init () {
		self.age = 0
	}
}

struct Coffee {
	var name : String?
	var size : String?

	init () {
		self.size = "Tall"
	}
}
```

만약 속성이 옵셔널이 아니라면 항상 초깃값을 가져야 합니다. 만약 옵셔널이 아닌 속성이 초깃값을 가지고 있지 않으면 컴파일 에러가 발생합니다.

```
class Dog {
	var name : String?
	var age : Int // 컴파일 에러!
}
```

속성을 정의할 때 초깃값을 지정해 주는 방법과,

```
class Dog {
	var name : String?
	var age : Int = 0 // 속성을 정의할 때 초깃값 지정
}
```

생성자에서 초깃값을 지정해주는 방법이 있습니다.

```
class Dog {
	var name : String?
	var age : Int

	init() {
		self.age = 0 // 생성자에서 초깃값 지정
	}
}
```

생성자도 함수와 마찬가지로 파라미터를 받을 수 있습니다.

```
class Dog {
	var name : String?
	var age : Int

	init (name : String?, age : Int) {
		self.name = name
		self.age = age
	}
}

var myDog = Dog (name : "찡코", age : 3)
```

먄약 상속받은 클래스라면 생성자에서 상위 클래스의 생성자를 호출해주어야 합니다. 만약 생성자의 파라미터가 상위 클래스의 파라미터와 같다면, ```override``` 키워드를 붙여주어야 합니다. ```super.init()``` 은 클래스 속성들의 초깃값이 모두 설정 된 후에 해야 합니다. 그리고 나서부터 자기 자신에 대한 ```self```키워드를 사용할 수 있습니다.

```
class Dog : Animal {
	var name : String?
	var age : Int

	override init(0 {
		self.age = 0 // 초깃값 설정
		super.init() // 상위 클래스 생성자 호출
		print (self.simpleDescription()) // 여기서부터 'self' 접근 가능
	})

	func simpleDescription() -> String {
		if let name = self.name {
			return "🐶 \(name)"
		} else {
			return "🐶 No name"
		}
	}
}
```

만약, 위 예시 코드를 아래처럼 바꿔서 ```super.init()```을 하기 전에 ```self```에 접근한다면 컴파일 에러가 발생합니다.

```
override init () {
	self.age = 0
	print (self.simpleDescription()) // 컴파일 에러 !
	super.init()
}
```

```deinit```은 메모리에서 해제된 직후에 호출됩니다.

```
class Dog {
	// ...

	deinit {
		print ("메머리에서 해제됨")
	}
}
```

#### 속성 (Properties)

속성은 크게 두 가지로 나뉩니다. 값을 가지는 속성(Sorted Property)과 계산되는 속성 (Computed Property)입니다. 쉽게 말하면 속성이 값 자체를 가지고 있는지, 혹은 어떠한 연산을 수행한 뒤 그 결과를 반환하는지의 차이입니다.

우리가 지금까지 정의하고 사용한 ```name```, ```age```와 같은 속성들은 모두 Stored Property입니다. Computed Property는 ```get```, ```set```을 사용해서 정의할 수 있습니다. ```set```에서는 새로 설정된 값을 ```newValue``` 라는 예약어를 통해 접근할 수 있습니다.

```
struct Hex {
	var decimal : Int?
	var hexString : String? {
		get {
			if let decimal = self.decimal {
				return String(decimal, radix : 16)
			} else {
				return nil
			}
		}
		set {
			if let newValue = newValue {
				self.decimal = Int (newValue, radix : 16)
			} else {
				self.decimal = nil
			}
		}
	}
}

var hex = Hex()
hex.decimal = 10
hex.hexString // "a"

hex.hexString = "b"
hex.decimal // 11
```

위 코드에서 ```hexString```은 실제 값을 가지고 있지는 않지만, ```decimal``` 로부터 값을 받아와 16진수 문자열로 만들어서 반환합니다. ```decimal```은 Stored Proterty, ```hexString```은 Computed Property 입니다.

참고로, ```get```만 정의할 경우에는 ```get``` 키워드를 생략할 수 있습니다. 이런 속성을 읽기 전용(Read Only)이라고 합니다.

```
class Hex {
	// ...

	var hexCode : String? {
		if let hex = self.hexString {
			return "0x" + hex
		}
		return nil
	}
}
```

```get```, ```set```과 비슷한 ```willSet```, ```didSet```을 이용하면 속성에 값이 지정되기 직전과 직후에 원하는 코드를 실행할 수 있습니다.

```
struct Hex {
	var decimal : Int ? {
		willSet {
			print ("\(self.decimal)에서 \(newValue)로 값이 바뀔 예정입니다.")
		}
		didSet {
			print ("\(oldValue)에서 \(self.decimal)로 값이 바뀌었습니다.")
		}
	}
}
```

마찬가지로, ```willSet```에서는 새로운 값을 ```newValue```로 얻어올 수 있고, ```didSet```에서는 예전 값을 ```oldValue``` 라는 예약어를 통해 얻어올 수 있습니다.

```willSet```과 ```didSet```은 일반적으로 어떤 속성의 값이 바뀌었을 때 UI를 업데이트하거나 특정 메서드를 호출하는 등의 역할을 할 때에 사용됩니다.

#### 튜플 (Tuple)

튜플 (Tuple)은 어떠한 값들의 묶음입니다. 배열과 비슷하다고 볼 수 있는데요. 배열과는 다르게 길이가 고정되어 있습니다. 값에 접근할 때에도 ```.```을 사용합니다.

``` 
var coffeeInfo = {"아메리카노", 5100}
coffeeInfo.0 // 아메리카노
coffeeInfo.1 // 5100
coffeeInfo.1 = 5100
```

이 튜플의 파라미터에 이름을 붙일 수도 있어요.

```
var namedCoffeeInfo = {coffe : "아메리카노", price : 5100}
namedCoffeeInfo.coffee // 아메리카노
namedCoffeeInfo.price // 5100
namedCoffeeInfo.price  = 5100
```

이렇게 보면, 앞의 구조체와 비슷합니다. 실제로 간단한 자료형을 만들 때에 구조체 대신 튜플을 사용합니다.

튜플의 타입 어노테이션

```
var coffeeInfo : (String, Int)
var namedCoffeeInfo : (coffee : String, price : Int)
```

튜플을 조금 응용하면, 아래와 같이 여러 변수에 값을 지정할 수도 있습니다.

```
let (coffee, price) = ("아메리카노", 5100)
coffee // 아메리카노
price // 5100
```

튜플이 가진 값을 가지고 변수에 값을 지정할 때, 무시하고 싶은 값이 있다면 ```_``` 키워드를 사용해서 할 수 있습니다. 아래 코드에서는 	```"라떼"``` 라는 첫 번째 값을 무시합니다

```
let (_, latteSize, lattePrice) = ("라떼", "Venti", 5600)
latteSize // Venti
lattePRice // 5600
```

물론, 튜플을 반환하는 함수도 만들 수 있습니다.

```
/// 커피 이름에 맞는 커피 가격 정보를 반환합니다. 일치하는 커피 이름이 없다면 'nil'을 반환합니다.
///
/// - parameter name : 커피 이름
///
/// - returns : 커피 이름과 가격 젖ㅇ보로 구성된 튜플을 반환합니다.

func conffeeInfo (for name : String) -> (name : String, price : Int)? {
	let coffeeInfoList : [(name : String, price: Int)] = [
		("아메리카노", 5100),
		("라떼", 5600)
	]

	for coffee in coffeeInfoList {
		if coffeeInfo.name == name {
			return coffeeInfo
		}
	}
	return nil
}
```
#### Enum

열거라는 뜻을 가진 Enumeration 에서 따온 용어입니다. 한글로 번역할때는 열거형 이라는 말을 많이 사용합니다.

```
enum Month : Int {
	case january = 1
	case feburary
	case march
	case april
	case may
	case june
	case july
	case august
	case september
	case october
	case november
	case december

	func simpleDescription() -> String {
		swithc self {
			case .janurary :
				return "1월"
			case .feburary :
				return "2월"
			case .march :
				return "3월"
			case .april :
				return "4월"
			case .may :
				return "5월"
			case .june :
				return "6월"
			case .july :
				return "7월"
			case .august :
				return "8월"
			case .september :
				return "9월"
			case .october :
				return "10월"
			case .november :
				return "11월"
			case .december :
				return "12월"
			
		}
	}
}

ley december = Month.december
print (december.simpleDescription()) // 12월
print (december.rawValue) // 12
```

위 예시에서 작성한 ```Month```는 ```Int```를 원시값 (Raw Value)으로 가지도록 정의되었습니다. 그렇기 때문에 각 케이스들은 1부터 12까지의 값을 가지고 있습니다. ```rawValue``` 속성이 바로 그 값을 나타내느데요. 반대로, 원시값을 가지고 Enum을 만들 수도 있습니다.

```
let october = Month (rqwValue : 10)
print (cotober) // Optional(Month.october)
```

Moht(rawValue:) 의 반환값이 옵셔널인 이유는, Enum에서 정의되지 않은 원시값을 가지고 생성할 경우 ```nil```을 반환하기 때문입니다.

```
Month (rawValue : 13) // nil
```

일반적으로 Enum은 ```Int``` 만을 원시값으로 가질 수 있다고 생각합니다. Swift의 Enum은 다른 자료형도 원시값으로 가질 수 있습니다.

```
enum IssueState : String {
	case open = "open"
	case closed = "closed"
}
```

만약 어떤 API의 응담을 내려주는 ```state```의 값이 ```open``` 또는 ```closed```라면, ```if-else``` 없이도 ```IssueState(rawValue:)``` 를 사용해서 Enum을 생성할 수 있습니다.

Enum은 원시값을 가지지 않을 수도 있습니다. 원시값을 가져야 할 필요가 없다면 굳이 만들지 않아도 됩니다.

```
enum Spoon {
	case dirt
	case bronze
	case silver
	case gold

	fun simpleDescription() -> {
		switch self {
			case .dirt:
				return "흙수저"
			case .bronze :
				return "동수저"
			case .silver :
				return "은수저"
			case .gold :
				return "금수저"
		}
	}
}
```

Enum을 예측할 수 있다면 Enum의 이름을 생략할 수 있습니다. 코드가 간결해 집니다.

```
let spoon : Spoon = .gold // 변수에 타입 어노테이션이 있기 때문에 생략 가능

func doSomething (with spoon : Spoon) {
	// ...
}
doSomething(with: .silver) // 함수 정의에 타입 어노테이션이 있기 때문에 생략 가능
```

##### 연관 값 (Associated Values)을 가지는 Enum

Enum은 연관 값(Associated)을 가질 수 있습니다. 아래 예시는 어떤 API에 대한 에러를 정의한 것인데요. ```invalidParameter``` 케이스는 필드 이름과 메시지를 가지도록 정의되었습니다.

```
enum NetworkError {
	case invalidParameter (String, String)
	case timeout
}

let error : NetworkError = .invalidParameter ("email", "이메일 형식이 올바르지 않습니다.")
```

이 값을 꺼내올 수 있는 방법으로는  `if-case` 또는 `switch`를 활용하는 방법이 있습니다.

```
if case .invalidParameter (let field, let message) = error {
    print (field) // email
    print (message) // 이메일 형식이 올바르지 않습니다.
}

switch error {
    case .invalidParameter (let field, let message) :
        print (field) // email
        print (message) // 이메일 형식이 올바르지 않습니다.

    default :
        break
}
```

### 프로토콜 (Protocol)

프로토콜 (Protocol) 은 인터페이스 입니다. 최소한으로 가져야 할 속성이나 메서드를 정의합니다. 구현은 하지 않습니다. 정의만 합니다.

```
/// 전송가능한 인터페이스를 정의합니다

protocol Sendable {
    var from : String? { get }
    var to : String { get } 

    func send()
}
```

클래스와 구조체에 프로토콜을 적용 (Conform) 시킬 수 있습니다. 프로토콜을 적용하면, 프로토콜에서 정의한 속성과 메서드를 모두 구현해야 합니다.

```
struct Mail: Sendable {
    var from : String?
    var to : String

    fun send() {
        print ("Send a mail from \(self.from) to \(self.to)")
    }
}

struct Feedback : Sendable {
    var from : String? {
        return nil // 피드백은 무조건 익명으로 보냅니다.
    }
    var to : String

    fun send() {
        print ("Send a feedback to \(self.to)")
    }
}
```

프로토콜은 마치 추상클래스처럼 사용될 수 있습니다.

```
func sendAnything (_ sendable: Sendable) {
    sendable.send()
}

let mail = Mail (from : "ljh28891004@gmnail.com, to : "jeon@stlesha.re")
sendAnything (mail)

let feedback = Feedback (to: "ljh28891004@gmail.com")
sendAnything (feedback)
```

`sendAnything()` 함수는 `Sendable` 타입을 파라미터로 받습니다. `Mail` 과 `Feedback` 은 엄연히 다른 타입이지만, 모두 `Sendable`을 따르고 있으므로 `sendAnything()` 함수에 전달될 수 있습니다. 그리고, `Sendable` 에서는 `send()` 함수를 정의하고 있기 때문에 호출이 가능합니다.

프로토콜은 또다른 프로토콜을 따를 수 있습니다.

```
protocol Messagable {
    var message : String? { get }
}

protocal Sendable : Messagable {
    // ...
}
```

`Sendable`은 `Messagable`을 기본적으로 따르는 프로토콜입니다. 따라서, `Sendable` 을 적용하려면 `var message : String? { get }`을 정의해주어야 합니다.

### Any 와 AnyObject

`Any`는 모든 타입에 대응합니다. `AnyObject`는 모든 객체 (Object)에 대응합니다.

```
let anyNumber : Any = 10
let anyString : Any = "Hi"

let anyInstance : AnyObject = Dob()
```

`Any` 와 `AnyObject`는 프로토콜입니다. Swift에서 사용 가능한 모든 타입은 `Any`를 따르도록 설계되었고, 모든 클래스들에는 `AnyObject` 프로토콜이 적용되어 있습니다.

### 타입 캐스팅 (Type Casting)

`anyNumber`에 `10`을 넣었닫고 해서 `anyNumber` 가 `Int` 는 아닙니다. `Any` 프로토콜을 따르는 어떤 값이기 때문이죠

```
anyNumber + 1 // 컴파일 에러 !
```

이럴 때에는 `as`를 이용해서 다운 캐스팅 (Down Casting)을 합니다. `Any` 는 `Int` 보다 더 큰 범위이기 때문에, 작은 범위로 줄인다고 하여 '다운 캐스팅' 입니다.

`Any` 는 `Int`뿐만 아니라 `String` 과 같은 전혀 엉뚱한 타입도 포합되어 있기 때문에 무조건 `Int` 로 변환되지 않습니다. 따라서 `as?` 를 사용해서 옵셔널을 취해야 합니다.

```
let number : Int? = anyNumber as? Int
```

옵셔널이기 때문에, 옵셔널 바인딩 문법도 사용할 수 있습니다. 실제로 이렇게 사용하는 경우가 굉장히 많습니다.

```
if let number = anyNumber as? Int {
    print (number + 1)
}
```

### 타입 검사

타입 캐스팅까지는 필요 없고, 만약 어떤 값이 특정한 타입인지를 검사할 때에는 `is`를 사용할 수 있습니다.

```
print (anyNumber is Int) // true
print (anyNumber is Any) // true
print (anyNumber is String) // false
print (anyString is String) // true
```

### Swift 주요 프로토콜

Swift 에는 기본적으로 제공하는 기초적인 프로토콜들이 있스빈다. 알아두면 개발할 때 굉장히 유용하게 사용할 수 있습니다.

#### CustomStringConvertible

자기 자신을 표현하는 문자열을 정의합니다. `print()`, `String()` 또는 `"\()"` 에서 사용될 때의 값입니다. 
`CustomStringConvertible` 의 정의는 아래와 같이 생겼습니다.

```
public protocol CustomStringConvertiblae {
    /// A textual representation of 'se;f'.
    public var description : String { get }
}
```

ex)

```
struct Dog : CustomSTringConvertible {
    var name : String
    var description : String {
        return "🐶 \(self.name)"
    }
}

let dog = Dog (name : "찡코")
print (dog) // 🐶 찡코
```

#### ExpressibleBy

우리는 지금까지 `10` 은 `Int`, `"Hi"` 는 `String` 이라고 '당연하게' 인지하고 있었습니다. 하지만, 엄밀히 말하자면 `10` 은 원래 `Int (10)` 으로 선언되어야 하고, `"Hi"` 는 `String("Hi")` 로 선언되어야 합니다.

이렇게, 생성자를 사용하지 않고도 생성할 수 있게 만드는 것을 리터럴 (Literal)이라고 합니다. 직역함녀 '문자 그대로'라는 뜻입니다.

```
let number = 10
let string = "Hi"
let array = ["a", "b", "c"]
let dictionary = [
    "key1" : "value1",
    "key2" : "value2"
]
```

이 리터럴을 가능하게 해주는 프로토콜이 있답니다. 바로 `ExpressibleByXXXLiteral` 인데요. `Int` 는 `ExpressibleByIntegerLiteral` 을, `String` 은 `ExpressibleByStringLiteral` 을, `Array` 는 `ExpressibleByArrayLiteral` 프로토콜을 따르고 있습니다.

ex

```
struct DollarConverter : ExpressibleByIntegerLiteral {
    typealias IntegerLiteralType = Int

    let price = 1_177
    var dollars : Int

    init (integerLiteral value : IntegerLiteralType) {
        self.dollars = value * self.price
    }
}

let converter : DollarConverter = 100
converter.dollars // 117700
```

### 익스텐션 (Extension)

Swift에서는 이미 정의된 타입에 새로운 속성이나 메서드를 추가할 수 있습니다. 익스텐션 (Extension) 이라는 기능인데요. `extension` 키워드를 사용해서 정의할 수 있습니다.

```
extension String {
    var length : Int {
        return self.characters.count
    }

    func reservced() -> String {
        return self.characters.reversed().map { String($0) }.joined(separator: "")
    }
}

let str = "안녕하세요"
str.length // 5
str.reversed() // 요세하녕안
```