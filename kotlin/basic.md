[`youtube - Kotlin 문법 총 정리`](https://www.youtube.com/watch?v=OtHkb6wAI5U) 를 보면서 정리합니다.

### 변수
```kotlin
const val a = 20 // 컴파일 타임 상수, 성능 향상 우위

fun main() {
    var i = 10 // 타입 추론이 가능함. 별도 지정을 하지 않아도 된다.
    var name: String = "hyejin" // 명시할 수도 있다.
    var point: Double = 3.3

    val num = 20 // 상수, java 의 final 과 유사하다.
    // num == 30 // compile error
}
```

### 형변환 
```kotlin
    var i = 10
    var l = 20L // long
    var name = "hj"

    l = i.toLong()
    i = l.toInt()
    name = i.toString()
```

### string interpolation 
```kotlin
    var name = "hyejin"
    print("제 이름은 ${name + 28}입니다.")
```

### max, random, in
```kotlin
import kotlin.random.Random
import kotlin.math.max

fun main() {
    var i = 10
    var j = 20
    println(max(i, j))

    val randomNum = Random.nextInt(0, 100)
    val randomNum2 = Random.nextDouble(0.0,1.0)
    println(randomNum)
    println(randomNum2)

    val reader = Scanner(System.`in`) // in 은 코틀린에서 사용할 수 없는 키워드, 자동으로 `` 감싸진다.
    reader.nextInt()
    reader.next()
}
```

### ~조건문~이 아닌 조건식 - if, when
```kotlin
fun main() {
    var i = 7
    
    if (i > 10) {
        print("10 보다 크다")
    }  else if (i > 5) {
        print("5 보다 크다")
    } else {
        print("")
    }

    when {
        i > 10 -> {
            print("10 보다 크다")
        }
        i > 5 -> {
            print("5 보다 크다")
        }
        else -> {
            print("")
        }
    }
    
    // 조건식이기 때문에 값을 받아서 쓸 수 있다.
    var i = 7
    var result = when {
        i > 10 -> {
            "10 보다 크다"
        }
        i > 5 -> {
            "5 보다 크다"
        }
        else -> {
            ""
        }
    }
    print(result)

    i = 11
    result = if (i > 10) {
        "10 보다 크다"
    }
    else if (i > 5) {
        "5 보다 크다"
    }
    else {
        ""
    }
    print(result)
}
```

### 반복문 
```kotlin
fun main() {
    val items = listOf(1,2,3,4,5)

    for (item in items) {
        print(item)
    }

    items.forEach { item ->
        print(item)
    }

    for (i in 0..(items.size - 1)) {
        print(items[i])
        // break
        // continue
    }
}
```

### list, array 
```kotlin
fun main() {
    val items = listOf(1,2,3,4,5)
    items.add(6) // X

    val mutableItems = mutableListOf(1,2,3,4,5)
    mutableItems.add(6)
    mutableItems.remove(3)

    val arrayItems = arrayOf(1,2,3)
    arrayItems[0] = 10
}
```

### try - catch
```kotlin
fun main() {
    val items = listOf(1,2,3)
    try {
        val item = items[4]
    } catch (e: Exception) {
        print(e.message)
    }
}
// Index 4 out of bounds for length 3
```

### null safety 
```kotlin 
fun main() {
    val name: String = null // X, String 타입엔 null 을 넣을 수 없다.

    val name1: String? = null // O
    var name2: String = ""

    if (name != null) {
        name2 = name
    }
    name2 = name!! // ? 를 떼는 방법이지만, 명시적이지 않는 듯..?

    // null 이 아니라면, 이 블록을 실행하자. it 로 접근 가능
    name?.let {
        name2 = name
    }
}
```

### 함수, 클래스
```kotlin
fun main() { // 탑레벨 함수
    print(sum(10, 20))
    
    val john = Person("John", 20)
    print(john.name) // X, private 
    print(john.age)

    john.name = "aaa" // X, val
    john.age = 25 // O, var
}
fun sum(a: Int, b: Int, c: Int = 0) = a + b + c

class Person(private val name: String, var age: Int)
```
