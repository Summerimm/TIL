# 3. Process
- **"Process is a program in execution"**
- Context? 현재 시점의 상태를 규명하기 위해 필요한 요소들(timesharing 구현을 위해 필요)
  1. CPU 수행 상태를 나타내는 hardware context: Program Counter, 각종 register
  2. 프로세스의 address space: code, data, stack
  3. 프로세스 관련 kernel data structure: PCB, kernel stack(프로세스 별로 보유)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/0b9d2f45-ddc5-4ade-84c5-f7c87b075b61)

# Process Control Block(PCB)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/742c2a5b-3e8f-4dde-a9aa-54a5bd2fd801)  
- OS가 각 프로세스를 관리하기 위해 프로세스 당 유지하는 정보
- 구조체로 유지
1. OS가 관리 상 사용하는 정보: Process state, PID, scheduling information, priority
2. CPU 수행 관련 하드웨어 값: PC, registers
3. 메모리 관련: code, data, stack의 위치 정보
4. 파일 관련: Open file descriptors

# Kernel Stack
- **Kernel Stack**이란?
  - kernel mode에서 실행되는 code와 data를 저장하는 stack
- Kernel stack의 목적
  1. 커널 함수 호출: 함수가 실행되는 동안 필요한 데이터와 정보를 스택에 저장
  2. interrupt 처리: interrupt 처리에 필요한 데이터 및 register 상태 등을 저장
  3. context switching: 현재 실행 중인 프로세스의 state 정보를 저장하고 다음 작업의 state 정보를 로드

# Process State
- 프로세스는 state가 변경되며 수행됨
1. **Running**: CPU 소유권을 가지고 instruction을 수행 중인 상태
2. **Ready**: CPU를: CPU를 기다리는 상태(메모리 등 다른 조건 모두 만족)
3. **Blocked**(wait, sleep)
   - CPU를 주어도 당장 instruction을 수행할 수 없는 상태
   - Process 자신이 요청한 event(I/O 등)이 즉시 만족되지 않아 이를 기다리는 상태
   - ex) 디스크에서 file을 읽어와야 하는 경우
4. **Suspended**(stopped)
   - 외부적인 이유로 프로세스의 수행이 정지된 상태
   - 프로세스는 통째로 디스크에 swap out된다
   - ex) 사용자가 프로그램을 일시 정지시킨 경우(break key)
   - ex) 시스템이 여러 이유로 프로세스를 잠시 중단시킴(메모리에 너무 많은 프로세스가 올라와 있을 때) 
5. New: 프로세스가 생성 중인 상태
6. Terminated: execution이 끝난 상태 

## Blocked vs Suspended
- Blocked: 자신이 요청한 event가 만족되면 Ready
- Suspended: 외부에서 resume해주어야 active

## Process State Diagram
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/7be4d252-fb31-446b-b80d-b4f7ca3d5e8d)  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/57675129-62ad-43ee-b4a9-774363ced87c)  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/554ddfd7-da46-4a3a-a723-e4ca12137f2f)  

# Context Switching
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/b332724e-54f9-4db0-8a7c-6dbb551bcb1f)  
- Context Switching: CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
  1. CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
  2. CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴
- Memory map의 역할
   - 현재 실행 중인 프로세스의 address space를 저장하고 새로운 프로세스의 address space을 로드함으로써
→ logical address와 physical address 간의 매핑 유지
   - 페이지 테이블 갱신
   - 보호 및 권한 설정 → 메모리 보호와 가상 메모리 관리

## Context Switching 주의사항
- System call이나 interrupt 발생 시 반드시 context switching이 일어나는 것 X
![image](https://github.com/Haaarimmm/TIL/assets/108309396/94ca7922-226c-4336-a3c0-ea622e7bbdc5)
- (1)의 경우에도 CPU 수행 정보 등 context의 일부를 PCB에 save
- But! context switching을 하는 (2)의 경우 부담이 훨씬 큼(cache memory flush)
  - cache memory flush: A 프로세스를 위해 사용하던 캐시 메모리를 모두 비우는 것 &rarr; 다시 프로세스 A로 돌아왔을 때 비어있음

# Queue for Process Scheduling
1. Job queue: 현재 시스템 내에 있는 모든 프로세스의 집합
2. Ready queue: 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합
3. Device queue: I/O device의 처리를 기다리는 프로세스의 집합

## Ready queue와 device queue
![image](https://github.com/Haaarimmm/TIL/assets/108309396/8a5eb98b-54cf-418e-8607-1fc4c43091c3)  
- 실제 시스템에서 큐가 어떻게 관리되는지를 자료구조의 형태로 나타낸 그림
- ready queue에 process들이 순서대로 대기 중
- magetic tape는 대기엹X, disk에 process 대기 중
- PCB에는 pointer 존재 &rarr; 포인터를 연결하여 큐 생성
- head : Queue에서 데이터가 제거되는 위치를 가리키는 포인터
- tail : Queue에서 데이터가 추가되는 위치를 가리키는 포인터

## Process Scheduling Queue
![image](https://github.com/Haaarimmm/TIL/assets/108309396/4de2666d-22ed-4bfc-a70d-92f2a139e906)
- 프로그램이 실행되면 Ready Queue가서 줄 섬
- 언젠가 자기 차례가 되어 CPU를 얻음
- I/O와 같이 시간이 오래걸리는 작업을 수행하면 해당 작업을 수행하는 Queue로 가서 줄서서 처리(Blocked)
- 완료 후 돌아와서 다시 Ready Queue
- CPU를 얻은 상황에서 timer interrupt 발생 시 다시 Ready Queue에 가서 줄 섬
- fork() 자식 프로세스가 생성 &rarr; 본인은 CPU를 놓고 ready queue로 가서 줄 섬
- interrupt 발생 시 Interrupt Service Routine 호출 및 처리 완료 시 실행 재개
- interrupt 처리 중 다른 프로세스가 CPU를 사용할 수도 있음
- 본인의 작업이 끝나면 CPU 밖으로 빠져나감

# Scheduler
1. **Long-term scheduler**(job scheduler)
   - new 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
   - *프로세스에 memory(및 각종 resource)를 주는 문제*
   - degree of multiprogramming(메모리에 여러 프로세스를 올림)을 제어
   - timesharing system에는 보통 장기 스케줄러가 없음(무조건 ready)
   - 요새는 이런 스케줄러가 없고 메모리에 다 올리는데 너무 많아지면 중기 스케줄러에서 제어함
2. **Short-term sceduler**(CPU scheduler)
   - 어떤 프로세스를 다음 번에 running시킬 지 결정
   - *프로세스에 CPU를 주는 문제*
   - 충분히 빨라야 함(ms 단위)
3. **Medium-Term Scheduler**(Swapper)
   - 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫒아냄
   - *프로세스에게서 memory를 뺏는 문제*
   - degree of multiprogramming을 제어

# 현대 OS에서 Long-term Scheduler를 사용하지 않는 이유
1. 다중 사용자와 다중 프로그래밍 환경
   - 현대의 OS는 다중 사용자 환경을 지원하며, 여러 개의 프로세스가 동시에 실행될 수 있음
   - 이러한 환경에서는 중간 단계의 스케줄링이 필요하지 않을 수 있음
   - 따라서 대부분의 OS는 중기 스케줄러를 사용하여 실행 가능한 프로세스를 선택하고 실행
2. 시분할 시스템
   - 현대의 운영 체제는 대부분 시분할 시스템을 지원
   - 이를 위해 단기 스케줄러가 사용되며, 장기 스케줄러의 역할은 상대적으로 줄어들었음

# Thread
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/2749c5ef-3d84-47e1-9d4e-0e368801f7bb)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/11e7ca31-ce5c-4da4-9397-a3f4dd5ec9d1)  
- **"A thread(or lightweight process) is a basic unit of CPU utilization"**
- Thread란?
  - 프로세스의 컨텍스트 내에서 돌아가는 논리흐름
  - 프로세스 내부에 여럿 있을 수 있는, **프로세스보다 작은 CPU 수행 단위**
- 같은 일을 하는 프로세스가 여러 개 필요한 경우, 한 프로세스에 여러 쓰레드를 두어 서로 다른 부분을 수행할 수 있게 한다.
  - 하나의 스레드만 가지는 프로세스: heavyweight process
  - 여러 개의 스레드를 가지는 프로세스: lightweight process
  - 현대 시스템은 다수의 쓰레드가 한 프로세스에서 동시에 돌아가는 프로그램을 작성할 수 있게 해준다.

# Thread의 구조
- 한 프로세스 안의 여러 쓰레드들은 최대한 공유할 수 있는 부분들을 공유한다.
  - PCB는 하나만 만들어진다.
  - 공유하는 부분: code, data section, OS resources, process state
  - 독립적인 부분: PC, register set, stack space
    - 고유의 TID, 스택, 스택 포인터, PC, 범용 레지스터, 조건 코드 등을 포함하는 자신만의 thread context를 가짐
- main thread: 맨 처음에 만들어지는 thread
- peer thread: 다른 thread들에 의해 만들어지는 thread
- *부모-자식의 계층 구조를 가지는 프로세스와 달리 각 쓰레드들은 서로 동등한 위치에 있음*

# TCB와 Thread Context Switching
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/893d6697-0494-4930-8edc-ee410d07dd6d)
- Thread Context Switching이란? 한 프로세스 내에서 thread의 TCB(Thread Control Block)를 바꾸는 것
- Process Context Switching과 달리 공유되는 하나의 virtual memory space에서 이루어진다
- Thread Context Switching은 Kernel에 의해 스케쥴링되거나, 혹은 라이브러리에 의해 스케쥴링됨

# Thread의 장점
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있음
- 스레드를 사용하면 병렬성을 높일 수 있음(multiprocessor computer 한정)
1. Responsiveness(응답성)
   - multi-threaded Web: if one thread is blocked(network) another thread continues(display)
   - 다중 스레드로 구성된 태스크 구조에서, 한 스레드가 BLOCKED 상태인 동안에도 동일한 태스크의 다른 스레드는 RUNNING 상태가 되어 빠른 처리가 가능하다.
2. Resource Sharing(자원 절약)
   - n threads can share binary code, data, resource of the process
3. Economy(빠르다)
   - creating & CPU switching thread (rather than a process)
   - thread context는 process context보다 훨씬 더 작기 때문에 thread context switching은 process보다 더 빠르다.
4. Utilization of MP(Multiprocessor) Architectures
   - each thread may be running in parallel on a different processor

# Thread의 단점
- 공유 변수, 전역 변수 등에 대해 동시에 접근하는 쓰레드들이 있다면 동기화 문제(Concurrency)가 발생할 수 있다.
  - 예를 들어, 쓰레드 간에 공유되는 변수 a == 0가 있고, 각 쓰레드에서 처리될 어떤 함수는 a에 1을 더하는 함수라 하자.
  - 100개의 쓰레드를 통해 a == 100이라는 결과를 얻고 싶다.
  - 그러나 쓰레드는 동시에 작동하므로, 특정 시점에 여러 쓰레드가 같은 a값을 가질 수도 있다.
  - 이 경우 100개의 쓰레드를 거치더라도 a == 100이라는 결과를 얻지 못할 수도 있다.
- 한 쓰레드에서의 문제가 전체 프로세스의 문제로 이어질 수도 있다.


# Implementation of Threads
1. Kernel Threads
   - Kernel에 의해 지원되는 thread
   - 커널이 프로세스에 여러 thread가 있음을 앎
   - 하나의 thread에서 다른 thread로 CPU 제어권이 넘어가는 것을 OS가 제어함
2. User Threads
   - Library에 의해 지원되는 thread
   - 커널은 여러 thread의 존재를 모름
   - User program이 스스로 thread의 CPU를 제어함
3. real-time threads

# Kernel-level Threads
- thread를 생성하고 스케쥴링하는 주체가 커널이다.
- 장점 
  1. 커널이 각 스레드를 개별적으로 관리
  2. 동작 중인 스레드가 System Call(커널 호출)해도 해당 프로세스 내 다른 스레드가 계속 실행될 수 있다.
- 단점
  1. 스케쥴링과 동기화를 위해 System Call(커널 호출)하는데 오래 걸린다.
  2. 유저 모드와 커널 모드 간 전환이 빈번하여 성능 저하로 이어질 수 있다.
  3. 구현이 어렵고 자원을 더 많이 소비하는 경향이 있다.

# User-level Threads
- 커널에 의존하지 않으면서 thread의 기능을 제공하는 라이브러리들을 이용해 구현된다.
- 따라서 커널은 이 thread들의 존재를 알지 못한다.
- 장점
  1. 커널이 thread들의 존재를 알지 못하므로 커널에 의한 context switching도 일어나지 않는다. (한 프로세스로 보기에)
  2. 따라서 모드 전환도 이루어지지 않고, overhead도 적으며 성능에서의 이득을 얻을 수 있다.
- 단점
  1. 커널에 의한 스케줄링 우선 순위가 제공되지 않아서 어떤 thread가 먼저 실행될지 알 수 없다.
  2. 커널의 입장에서는 이 모든 thread들이 하나의 프로세스이기에, 한 thread에서 System Call이 발생하면 모든 thread들이 멈추게 된다.
