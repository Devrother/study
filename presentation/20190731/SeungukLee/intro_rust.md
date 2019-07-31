# Rust

---

Rust 에 대해 간단한 소개 및 실습

---
## Agenda

- 특징
- Rust 설치
- 추리 게임 튜토리얼
---


## 특징

- System Programming Language
- No GC
- Speed
- Memory Safety
- Thread Safety

**메모리 오류를 컴파일 시간에 잡아냄**

---

## Install Rust

- 패키지 매니저 (`apt-get` or `brew`)
- 소스코드 빌드
- rustup (관리자 도구)

우리는 rustup 을 설치할 것이다

---


`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

https://rustup.rs/

---

`$ cargo --version`
`$ cargo new guessing_game --bin`
`$ cd guessing_game`

`$ cargo check`
`$ cargo build`
`$ cargo run`

---

vscode 에서 Rust(rls) 설치
task 설정
launch 설정

---

## 추리 게임 튜토리얼

---

### 추리값 처리하기

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}

```

---

- `use std::io;`

입력을 받고 결과값을 표시하기 위해 `io` 라이브러리를 가져온다
- `let mut guess = String::new();`
guess 라는 mutable 변수를 생성한다
`::` 는 `new` 가 `String` 타입의 연관함수임을 나타낸다

---

### Result 타입으로 잠재된 실패 다루기

`read_line`은 우리가 인자로 넘긴 문자열에 사용자가 입력을 저장할 뿐 아니라 하나의 값을 돌려 줍니다. 여기서 돌려준 값은 `io::Result` 입니다.

> Result 타입은 열거형으로써 enums 라고 부르기도 한다
---

### 비밀번호 생성하기


Cargo.toml
``` toml
[dependencies]

rand = "0.3.14"
```
`$ cargo build`

Cargo는 Crates.io 데이터의 복사본인 레지스트리(registry) 에서 모든 것들을 가져옵니다. 

> 새로운 버전을 업데이트 할 때는 $ cargo update

---

### 임의의 숫자를 생성하기

```rust
extern crate rand;

use std::io;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng()
    .gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}
```
---

`extern crate rand;`을 추가하여 러스트에게 우리가 외부에 의존하는 크레이트가 있음을 알립니다.

`rand::thread_rng` 함수는 현재 스레드에서만 사용되는 특별한 정수생성기를 돌려 줍니다.

`$ cargo doc --open`

---

### 비밀번호와 추리값을 비교하기

```rust
extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng()
    .gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();

    
```

---


``` rust
    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);

    match guess.cmp(&secret_number) {
        Ordering::Less    => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal   => println!("You win!"),
    }
}
```

---

`Ordering`은 `Result`와 같은 열거형이지만 `Ordering`의 값은 `Less`, `Greater`, `Equal`입니다

---

`match` 표현식은 arm 으로 이루어져 있습니다. 하나의 arm은 하나의 패턴 과 match 표현식에서 주어진 값이 패턴과 맞는다면 실행할 코드로 이루어져 있습니다. 

---

하지만 위 코드는 컴파일되지 않는다!!

---

```rust
    let guess: u32 = guess.trim().parse()
        .expect("Please type a number!");
```

문자열의 `parse` 메소드는 문자열을 숫자형으로 파싱합니다. 

---
### 반복문을 이용하여 여러 번의 추리 허용

``` rust
extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);

    match guess.cmp(&secret_number) {
        Ordering::Less    => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal   => println!("You win!"),
    }
}
```

---

``` rust
let guess: u32 = guess.trim().parse()
        .expect("Please type a number!");
```
---

### 반복문을 이용하여 여러 번의 추리 허용

``` rust
extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = guess.trim().parse()
            .expect("Please type a number!");

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => println!("You win!"),
        }
    }
}
```

---

### 정답 이후에 종료하기

``` rust
extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = guess.trim().parse()
            .expect("Please type a number!");

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => {
                println!("You win!");
                break;
            }
        }
    }
}
```
---

### 잘못된 입력값 처리하기

```rust
extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => {
                println!("You win!");
                break;
            }
        }
    }
}
```

---
## References & Further More

- [한국 러스트 사용자 그룹](https://rust-kr.org/)
- [The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)
- [The big picture of compilation in Rust](https://users.rust-lang.org/t/the-big-picture-of-compilation-in-rust/6380)
- [Rust 읽으거리](https://blog.seulgi.kim/2018/11/rust.html)
- [Rust 자주 묻는 질문들](https://prev.rust-lang.org/ko-KR/faq.html)
---
