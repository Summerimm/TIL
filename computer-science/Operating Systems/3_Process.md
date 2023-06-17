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

# Blocked vs Suspended
- Blocked: 자신이 요청한 event가 만족되면 Ready
- Suspended: 외부에서 resume해주어야 active

# Process State Diagram
![image](https://github.com/Haaarimmm/TIL/assets/108309396/7be4d252-fb31-446b-b80d-b4f7ca3d5e8d)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/57675129-62ad-43ee-b4a9-774363ced87c)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/554ddfd7-da46-4a3a-a723-e4ca12137f2f)  


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
- System call이나 interrupt 발생 시 반드시 context switching이 일어나는 것 X
![image](https://github.com/Haaarimmm/TIL/assets/108309396/94ca7922-226c-4336-a3c0-ea622e7bbdc5)
- (1)의 경우에도 CPU 수행 정보 등 context의 일부를 PCB에 save해야 하지만 context switching을 하는 (2)의 경우 부담이 훨씬 큼(cache memory flush)
  - cache memory flush: A 프로세스를 위해 사용하던 캐시 메모리를 모두 비우는 것 &rarr; 다시 프로세스 A로 돌아왔을 때 비어있음

# Queue for Process Scheduling
1. Job queue: 현재 시스템 내에 있는 모든 프로세스의 집합
2. Ready queue: 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합
3. Device queue: I/O device의 처리를 기다리는 프로세스의 집합

# Ready queue와 device queue
![image](https://github.com/Haaarimmm/TIL/assets/108309396/8a5eb98b-54cf-418e-8607-1fc4c43091c3)  
- ready queue에 process들이 순서대로 대기 중
- magetic tape는 대기엹X, disk에 process 대기 중

# Process Scheduling Queue
![image](https://github.com/Haaarimmm/TIL/assets/108309396/4de2666d-22ed-4bfc-a70d-92f2a139e906)

# Scheduler
1. **Long-term scheduler**(job scheduler)
   - 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
   - 프로세스에 memory(및 각종 resource)를 주는 문제
   - degree of multiprogramming(메모리에 여러 프로세스를 올림)을 제어
   - timesharing system에는 보통 장기 스케줄러가 없음(무조건 ready)
2. **Short-term sceduler**(CPU scheduler)
   - 어떤 프로세스를 다음 번에 running시킬 지 결정
   - 프로세스에 CPU를 주는 문제
   - 충분히 빨라야 함(ms 단위)
3. **Medium-Term Scheduler**(Swapper)
   - 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫒차냄
   - 프로세스에게서 memory를 뺏는 문제
   - degree of multiprogramming을 제어

# Thread
![image](https://github.com/Haaarimmm/TIL/assets/108309396/2749c5ef-3d84-47e1-9d4e-0e368801f7bb)
![image](https://github.com/Haaarimmm/TIL/assets/108309396/11e7ca31-ce5c-4da4-9397-a3f4dd5ec9d1)  
- **"A thread(or lightweight process) is a basic unit of CPU utilization"**
- CPU의 수행 단위
- Thread의 구성: PC, register set, stack space &rarr; thread별로 가짐
  Thread가 동료 thread와 공유하는 부분(=task): code, data section, OS resources, process state
- 전통적인 개념의 heavyweight process는 하나의 thread를 가지고 있는 task로 볼 수 있음

## Thread의 장점
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있음
- 스레드를 사용하면 병렬성을 높일 수 있음(multiprocessor computer 한정)
1. Responsiveness(응답성)
   - multi-threaded Web: if one thread is blocked(network) another thread continues(display)
2. Resource Sharing(자원 절약)
   - n threads can share binary code, data, resource of the process
3. Economy(빠르다)
   - creating & CPU switching thread (rather than a process)
   - Solaris의 경우 위 두 가지 overhead가 각각 30배, 5배
4. Utilization of MP(Multiprocessor) Architectures
   - each thread may be running in parallel on a different processor

## Implementation of Threads
1. Kernel Threads: 하나의 thread에서 다른 thread로 CPU 제어권이 넘어가는 것을 OS가 제어함
2. User Threads: OS는 thread의 존재를 모르고 User program이 스스로 thread의 CPU를 제어함
3. real-time threads