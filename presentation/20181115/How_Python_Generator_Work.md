# How Python Generator Work

## Frame object
- Contains information for executing a function
- 함수를 실행할떄 필요한 정보를 담고있는 객체.

Frame 객체에는 `f_locals`, `f_lasti`, `f_back`, `f_code` 등 속성이 있다.

- `f_locals` : 지역변수 상태 (Local variables are stored)
- `f_bakc` : 자신을 호출한 프레임을 가르킨다.(Previous stack frame, this frame's caller
- `f_lasti` : 가장 최근에 실행된 바이트코드 인덱스 (Index of last attempted instruction in bytecode.)
- `f_code`: 코드 객체
	- `co_consts` : Constant values
	- `co_names` : Global variable names
	- `co_varnames` : Local variable names
	- `co_code` : Complied bytecode

----
인터프린터 내부에는 각 스레드마다 `ThreadState` 라는 객체가 있다. 현재 실행되고 있는 함수를 멤버로서 가지고 있다.
함수가 다른 함수를 호출하면 Frame 객체가 생성되고 새롭게 생긴 프레임의 `f_back` 은 호출한 프레임을 가르킨다. `ThreadState` 는 현재 실행중인 프레임을 갱신하게 된다. 이것이 콜 스택

----
코드 객체에는 여러가지 속성들이 있다.(바이트 코드를 이해해야됨)
어디까지 진행됬는지 제너레이터가 프레임을 들고있음으로서 알수있기때문에 일시중지한다음에 재게할수있다.

## PyEval_EvalFrameEx

The code object associated with the execution frame is executed, interpreting bytecode and executing calls as needed.
프레임을 실행하는 함수. 바이트 코드들의 opcode 가 여기서 실행된다.

## 정리

### Frame object
- 함수가 실행될때 사용된다.
- 함수가 실행하는데 필요한 정보들을 담고 있다.
    - Call stack 을 만듬
    - Value stack
    - Local variables
    - Last attempted bytecode instruction

### Generator
- Contains a frame object like thread state
- The frame memorizes which index of bytecode is executed.
- The frame stores local variables.

따라서 함수를 일지중지하고 재게하는 것이 가능하다
