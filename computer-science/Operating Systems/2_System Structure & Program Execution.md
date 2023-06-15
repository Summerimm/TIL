# 2 System Structure & Program Execution
## 컴퓨터 시스템 구조
![image](https://github.com/Haaarimmm/TIL/assets/108309396/28f2c956-9242-439f-8650-1855ae7a834c)
1. CPU: 매 clock cycle마다 memory에서 instruction을 읽어 실행
   - mode bit: kernel mode or user mode
   - interrupt line: instruction 한 줄 수행 후 interrupt line을 확인해 들어온 interrupt가 있는지 확인
   - registers: memory보다 빠르면서 정보를 저장할 수 있는 작은 공간
2. Memory: CPU의 작업 공간
3. I/O Device: disk, keyboard, ...
   - 각각 device controller와 local buffer가 존재
   - device controller: I/O Device의 작은 CPU 역할, 작업 완료 후 CPU에 interrupt
   - local buffer: device controller의 작업 공간
4. timer: 특정 프로그램이 CPU를 독점하는 것을 막음
- CPU의 처리속도가 가장 빠르고 I/O device의 처리속도가 가장 느림

## Mode bit
- user program의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치
- mode bit = 0: **Kernel mode** - previleged instruction 수행
  - Interrupt나 Exception 발생 시 하드웨어가 mode bit을 0으로 바꿈
  - user program에게 CPU를 넘기기 전에 mode bit을 1로 set
- mode bit = 1: **User mode** - 제한된 instruction 수행

## Timer
- 정해진 시간이 흐른 뒤 OS에게 제어권이 넘어가도록 interrupt를 발생시킴
- 타이머 값이 매 clock 1씩 감소하다가 0이 되면 timer interrupt 발생
- **특정 프로그램이 CPU를 독점하는 것을 막음**
- *time sharing* 구현, 현재 시간 계산 등을 위해 사용

## I/O Device Controller
- 해당 I/O device를 관리하는 일종의 작은 CPU
- control register, status register
- local buffer = 일종의 data register
- I/O는 실제 device와 local buffer 사이에서 일어남
- I/O가 끝났을 경우 interrupt로 CPU에 알림(Hardware interrupt)
- **device driver**: OS 코드 중 각 장치별 처리 루틴(handler) &rarr; Software
- **device controller**: 각 장치를 통제하는 작은 CPU &rarr; Hardware

## I/O Execution
- 모든 I/O instruction은 privileged instruction
- user program은 어떻게 I/O를 하는가?
   - **system call**: OS에게 I/O request를 보냄(Trap - software interrupt)
   - trap을 사용하여 interrupt vector의 특정 위치로 이동
   - 제어권이 interrupt vector가 가리키는 interrupt handler로 이동
   - 올바른 I/O request인지 확인 후 I/O 진행
   - I/O 완료 시 제어권을 system call 다음 instruction으로 넘김

## Interrupt
- interrupt 당한 시점의 register와 program counter(PC)를 save한 후 CPU의 제어를 interrupt handler에 넘긴다
- **Interrupt**(hardware interrupt): 하드웨어(키보드, 하드디스크..)가 발생시킨 interrupt
- **Trap**(software interrupt): Exception, System call(user program이 커널 함수 호출)
- interrupt 관련 용어
   - **interrupt vector**: 해당 interrupt handler의 주소를 가지고 있음
   - **interrupt handler** = interrupt service routine: 해당 interrupt를 처리하는 kernel 함수

## System Call
- user program이 OS의 서비스를 받기 위해 **커널 함수를 호출**
- **CPU 제어권이 OS에게** 넘어감


## Synchronous I/O & Asynchronous I/O
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b6cda4d5-78f7-413f-b482-afd8955a0278)
1. Synchronous I/O
   - I/O request 후 입출력 작업이 완료된 후에야 제어가 user program에 넘어감
   1. 구현 방법 1
      - I/O가 끝날 때까지 CPU를 낭비시킴
      - 매 시점 하나의 I/O만 일어날 수 있음
   2. 구현 방법 2
      - I/O가 완료될 때까지 해당 프로그램에게서 CPU를 빼앗음
      - I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
      - 다른 프로그램에게 CPU를 줌
2. Asynchronous I/O
   - I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 user program에 즉시 넘어감
- 두 경우 모두 I/O의 완료는 interrupt로 알려줌

## DMA Controller(Direct Memory Access)
- I/O interrupt가 자주 들어오는 경우, CPU에 Interrupt를 걸면 CPU의 overhead가 커짐
- CPU와 DMA 둘 다 Memory에 접근 가능
- Memory controller: CPU, DMA 동시에 접근할 경우 control
- 빠른 I/O device를 메모리에 가까운 속도로 처리하기 위해 사용
- CPU의 중재 없이 device controller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송
- 바이트 단위가 아니라 block 단위로 interrupt 발생시킴
- DMA controller가 I/O interrupt를 받아 메모리에 복사하고 CPU에는 한 번만 interrupt 발생시킴

## 저장장치 계층 구조
![image](https://github.com/Al9-Mor9/CS-study/assets/108309396/c46646cc-5a89-4353-a101-b656462dc1d7)
- 위로 갈 수록 speed&uarr;, cost&uarr;, 용량&darr;
- DRAM, Cache memory(SRAM), Registers &rarr; volatile
- Primary(executable) 계층: byte 단위로 접근 가능한, CPU가 직접 접근 가능
- Secondary 계층: sector 단위로 접근 가능, CPU가 직접 접근 불가
- caching: copying information into faster storage system

## Program Execution
- 실행파일 A, B 실행 시 각각 독자적인 virtual memory가 생성됨(각 프로세스 별 address space 존재)
- address translation을 통해 필요한 부분만 Physical memory에 올림
- Swap area: 경우에 따라서 프로그램이 종료되기 전까지 보관해야 할 부분은 disk의 swap area에 내려놓음, 메모리의 연장 공간

## Kernel Address Space contents
![image](https://github.com/Al9-Mor9/CS-study/assets/108309396/079e2885-d11f-4137-9fe1-5e93efbca0ef)
- PCB(Process Control Block)