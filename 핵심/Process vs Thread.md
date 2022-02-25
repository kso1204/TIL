# Process Vs Thread

# 프로그램(Program)

- 어떤 작업을 위해 실행할 수 있는 파일

# 프로세스(Process)

- 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램
- 메모리에 올라와 실행되고 있는 프로그램의 인스턴스(독립적인 개체)
- 운영체제로부터 시스템 자원을 할당받는 작업의 단위

![Process](https://gmlwjd9405.github.io/images/os-process-and-thread/process.png)

- 프로세스는 각각 독립된 메모리 영역 (Code, Data, Stack, Heap)을 할당 받는다.
- 기본적으로 프로세스당 최소 1개의 스레드(메인 스레드)를 가지고 있다.
- 각 프로세스는 별도의 주소 공간에서 실행되며, 한 프로세스는 다른 프로세스의 변수나 자료구조에 접근할 수 없다.
- 한 프로세스가 다른 프로세스의 자원에 접근하려면 프로세스 간의 통신(IPC, Inter-Process-Communication)을 사용해야 한다.

# 스레드(Thread)

- 프로세스 내에서 실행되는 흐름의 단위
- 프로세스가 할당받은 자원을 이용하는 실행의 단위

![Thread](https://gmlwjd9405.github.io/images/os-process-and-thread/thread.png)

- 스레드는 프로세스 내에서 각각 Stack만 따로 할당받고 Code, Data, Heap 영역은 공유한다.
- 스레드는 한 

# References 

1. https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html