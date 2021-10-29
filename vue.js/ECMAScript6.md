> ECMA

- 정보통신에 대한 표준을 제정하는 비영리 표준화 기구
- ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세를 말한다.



> 변수와 식별자

1. 식별자 

- 식별자는 반드시 `문자`, `달러($)`, `밑줄(_)` 로 시작
- 식별자 작성 스타일
  - 카멜 케이스 (camelCase, lower-camel-case) : 변수, 객체, 함수에 사용
  - 파스칼 케이스 (PascalCase, upper-camel-case) : 클래스, 생성자에 사용
  - 대문자 스네이크 케이스 (SNAKE_CASE) : 상수(constants)*에 사용

2. 변수

- `const`, `let` 모두 블록 스코프, 재선언 불가
- `const` : 재할당 불가
- `let` : 재할당 가능
- `var` : 함수 스코프, 재선언 가능



> 호이스팅* (hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상

```javascript
console.log(hoisted)
var hoisted = 'can you see me?'
```

```javascript
var hoisted
console.log(hoisted)
hoisted = 'can you see me?'
```



> TDZ (Temporal Dead Zone)

```javascript
pi; // ReferenceError, !!!TDZ!!!
const pi = 3.14; // Declaration & initialization
pi; // 3.14
```



---

> 데이터 타입 종류

- 원시 타입 (Primitive) : `Number`, `String`, `Boolean`, `undefined`, `null` 
  - 객체가 아닌 기본 타입, 실제 값이 담김
  - `Number` 타입 중, `NaN`, `Infinity` 
  - `string`, 템플릿 리터럴
    - ES6부터 지원
    - 파이썬의 f-string 처럼 사용 가능 
  - `undefined` : '값이 없음'이 자동으로 들어감
  - `null` : `object` 타입, '값이 없음'을 의도적으로 표현
  - `Boolean` : [] 는 true, '' 는 false
- 참조 타입 (Reference) : `Objects`, `Array`, `Function` 
  - 변수에 해당 객체의 참조 값이 담김



---

> 조건문 (switch statement)

```javascript
switch(expression) {
  case 'first value': {
    // do something
    [break] // 선택사항
  }
  case 'second value': {
    // do something
    [break]
  }
  [default: {
    // do something
  }]
}
```



> 반복문

- `for`
- `for... in` : object(키-벨류 형태) 순회할 때 사용, 배열에선 권장하지 X
- `for... of` : 파이썬의 `for... in` 과 유사하다.



---

> 함수 in JavaScript

- 함수 선언식 (declaration) : 익명 함수 불가, 호이스팅 가능
- 함수 표현식 (expression) : const/let 변수에 담아서 hoisting을 방지할 수 있다. `'에어비엔비에서 권장하는 방식'` 
- JS도 `일급 객체`에 해당



> 화살표 함수 (Arrow Function) - '=>'

- function 키워드 생략 가능
- 함수의 매개변수가 하나뿐이라면, `()` 생략 가능
- 바디에 표현식이 하나라면, `{}`, `return` 생략 



##### 예제

```javascript
/*
isValid = function (password) {
	return password.length >= 8 ? true: false
}
*/
isValid = password => password.length >= 8 ? true: false
isValid('abcdabcd')
```

```javascript
/*
const join = function (array, separator) {
	let ret = array[0]
	for (let i = 1; i < array.length; i++) {
		ret += separator + array[i]
	}
	return ret
}
*/
const join = (array, separator) => {
	let ret = array[0]
	for (let i = 1; i < array.length; i++) {
		ret += separator + array[i]
	}
	return ret
}
join(['010', '1234', '5678'], '-')
```



---

> 배열 (Arrays) 관련 주요 메서드 목록 (1)

- `reverse`
- `push & pop` : 스택과 유사
- `unshift & shift` : 가장 앞에 추가 및 삭제
- `includes` : 특정 값이 존재하는지 판별
- `indexOf` 
- `join` : 배열의 모든 요소를 연결하여 반환, separator 생략 시 쉼표를 기본값으로 사용



> 배열 관련 메서드 목록 (2)

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 콜백 함수를 받는다.
- `forEach` : 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 -> 반환X
  - array.forEach(callback(`element`[, `index`[, `array`]])) 
- `map` : 콜백함수의 반환 값을 요소로 하는 새로운 배열 반환
  - 콜백함수에 항상 `return`이 있어야 한다.
- `filter` : 반환값이 참인 요소들만 모아서 새로운 배열 반환
- `find` : 콜백함수의 반환값이 참이면 해당 요소 반환
- `some` : 배열의 요소 중 하나라도 참이라면 true 반환
- `every` : 배열의 모든 요소가 참이라면 true 반환
- `reduce` : 콜백함수의 반환값들을 하나의 값(acc)에 누적 후 반환
  - array.reduce(callback(`acc`, `element`, [`index`[, `array`]]), initialValue)
  - acc : 이전 콜백 함수의 반환 값이 누적되는 변수
  - initialValue(Optional) : default 값은 배열의 첫번째 값, 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생



---

> 객체 관련 ES6 문법 - 구조 분해 할당

```javascript
const userInformation = {
  name: 'hj',
  userid: 'hj123',
  phone: '010-0000-1111'
}
const { name } = userInformation
// const name = userInformation.name
const { userid, phone } = userInformation
```

```javascript
const users = [
  {
    name: 'hailey',
    contact: '010-1234-5678',
  },
  {
    name: 'paul',
    contact: '010-5678-1234',
  },
]

// 축약 전
function saveUserData (users) {
  const userData = users.map((user, index) => {
    return { id: index, name: user.name, contact: user.contact }
  })

  return userData
}

// [Object Destructuring]
function saveUserData (users) {
  const userData = users.map(({ name, contact }, id) => {
    return { id, name, contact }
  })
  return userData
}
```



> JSON (JavaScript Object Notation)

- JSON => Object : `parse()`
- Object => JSON : `JSON.stringify()`  

