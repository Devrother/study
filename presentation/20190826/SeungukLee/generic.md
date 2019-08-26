# Generic

---

> 코드는 자바 코드

---

## Generic?

---

``` java
class Hello<T> { ... }

new Hello<String>();
```

- `Hello` 옆에 `<T>`: 타입 파라미터
- `<String>` : 타입 인자(type argument)
- 여러 다른 데이터 타입들을 가질 수 있음
- 컴파일 시점에서 컴파일러가 좀 더 정확하게 타입을 체킹함

---

``` java
List<String> list = new ArrayList<>();
list.add(1); // compile 시점에서 에러가 남

List list2 = new ArrayList();
list2.add("str");
String s = (String) list2.get(0); // casting 해줘야됨
```

---

## 제네릭 메소드, 제네릭 클래스

---

### 제네릭 메소드

``` java
// 메소드 레벨에 타입 파라미를 정의해서 사용
<T> void print(T t) {
    System.out.println(t);
}
```

---

### 제네릭 클래스

``` java
public class Generic2<T> {
     // 클래스 레벨로 타입 파라미터를 정의하였을 경우
    static void print(T t) {
        System.out.println(t);
    }
}
```

- 다음과같이 static method 에서 에러남
- 저 위의 타입 변수는 이 클래스의 인스턴스가 만들어질때 인자값을 받아오는데static 메소드는 클래스 오브젝트를 만들지 않고 사용하다보니 T 타입이 무엇인지 알 수 없음
- `static <T> void print(T t)` 이렇게 사용해야한다-
- 이름이 같아 혼동하기 쉽움 -> `T` 대신 `S` 같은 다른 이름으로 사용하는 것이 좋음

---

## Bounded Type Parameter

---

### Bounded Type Parameter

- 제한을 둘 떄 사용
- `<T extends List>` : `T` 타입은 `List` 의 서브 타입만 가능
- multiple bound : 제약을 하나만 두는 것이 아니라 여러개 둠
	- `<T extends List & Serializable & Comparable & Closeable>`
	- 단 제약을 둘 때 클래스는 하나만 있어야함

---

코드 실행

---

## Subtyping in generics

---

``` java
Integer i = 10;
Number n = i; // Number 가 Integer 의 슈퍼 클래스이기 때문에 가능
```

``` java
List<Integer> intList = new ArrayList<>();
List<Number> numberList = intList; // compile error!!

ArrayList<Integer> arrList = new ArrayList<>();
List<Integer> intList2 = arrList;
```



---

- `Integer` 는 `Number` 의 서브 타입
- `List<Integer>` 는 `List<Number>` 의 서브 타입이 아님
- 타입 파라미터 사이에 슈퍼 타입 서브 타입 관계가 있다고 해서 위 처럼 타입 파라미터가 적용된 클래스 사이에 서브 타입, 슈퍼 타입 관계가 형성되지는 않도록 설계되어있음
- 타입 파라미터의 서브 타입, 슈퍼 타입 관계 즉 상속 관계는 타입 파라미터가 적용이된 제너릭 타입의 상속관계에 영향을 주지 않는다고 생각하면 됨

---

코드 실행

---

## Wildcards

---

```java
List<?> list
// List<? extends Object> list2
```

- Object 에 정의되어있는 기능만 가져와 사용을 하겠다
- 나는 ? 에 오는 타입이 무엇이 와도 상관이 없어.
- 나는 타입 파라미터를 받는 List 라는 녀석이 가지고 있는 메소드만 사용을 할거야라는 의미

---


## Reference & Further More

- [토비의 봄 TV 4회 (1) 자바 Generics](https://www.youtube.com/watch?v=ipT2XG1SHtQ)

- [토비의 봄 TV 4회 (2) Generics에서 와일드카드 활용법, 람다와 인터섹션 타입을 이용한 동적인 기능확장법](https://www.youtube.com/watch?v=PQ58n0hk7DI)

- [공변성과 반공변성은 무엇인가?](https://edykim.com/ko/post/what-is-coercion-and-anticommunism/)

- [Java의 Generics](https://medium.com/@joongwon/java-java%EC%9D%98-generics-604b562530b3)