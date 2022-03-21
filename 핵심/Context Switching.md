# 문맥 교환(Context Switching)

- 현재 진행하고 있는 Task(Process, Thread)의 상태를 저장하고 다음 진행할 Task의 상태 값을 읽어 적용하는 과정

![Context](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F994590345BB1B4DB2F7E5C)

- 출처 : https://www.crocus.co.kr/1364

- 프로세스 P0을 실행하던 중에, interrupte or system call로 인하여 P1 실행을 요청하는 과정에 대한 설명이다.

- PCB0에 P0의 정보를 저장하고 PCB1로부터 P1의 정보를 가져오는 과정동안 P1은 idle(유휴시간)을 갖고, 

- P1을 정상적으로 실행한 다음 다시 interrupt or system call로 인하여 PCB1에 P1의 정보를 저장하고, PCB0으로부터 P0의 정보를 가져와서 다시 P0을 실행하는

- 대기 - 실행을 번갈아 하는 과정을 컨텍스트 스위칭이라고 한다.

# 컨텍스트 스위칭 인터럽트

1. 컨텍스트 스위칭은 다음과 같은 상황에서 일어난다.

- I/O Interrupt

- CPU 사용시간 만료

- 자식 프로세스 Fork

2. 이러한 컨텍스트 스위칭이 일어날 때 다음번 프로세스는 스케쥴러가 결정하게 된다.

![PCB](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F99FC69365BB1B67D211D7A)

- 출처 : https://www.crocus.co.kr/1364

- PCB에서 저장되는 정보는 프로세스 번호, 포인터, 프로세스 상태, 레지스터, 프로그램 카운터(코드 위치) 등등이 저장된다.

# CPU에서 프로세스를 실행하는 과정

1. https://www.youtube.com/watch?v=Fg00LN30Ezg