# 7. Deadlocks
## The Deadlock Problem
- **Deadlock**: 일련의 프로세스들이 서로가 가진 자원을 기다리며 block된 상태
- Resource(자원)
  - 하드웨어, 소프트웨어 등을 포함
  - I/O device, CPU cycle, memory space, semaphore 등
  - 프로세스가 자원을 사용하는 절차: request &rarr; allocate &rarr; use &rarr; release

# Deadlock 발생의 4가지 조건
1. **Mutual exclusion**: 매 순간 *하나의 프로세스만이 자원을 사용 가능*
2. **No preemption**: 프로세스는 자원을 스스로 내어놓고 *강제로 빼앗기지 않음*
3. **Hold and wait**: 자원을 가진 프로세스가 다른 자원을 기다릴 때 *보유자원을 놓지 않고 계속 가지고 있음*
4. **Circular wait**: 자원을 기다리는 프로세스 간에 *사이클이 형성*됨

# Resource-Allocation Graph(자원 할당 그래프)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/9c491ffb-ca41-4417-82f9-d607856ee0e3)  
- Vertex: process P, resource R
- Edge: 
   - request edge $P_i$ &rarr; $R_j$
   - assignment edge $R_j$ &rarr; $P_i$
- 그래프에 cycle이 없으면 deadlock 아님
- 그래프에 cycle이 있으면
   - if *only one instance* per resource type, then *deadlock*
   - if *several instances* per resource type, *possibility of deadlock*

# Deadlock의 처리 방법
1. **Deadlock Prevention**
   - 자원 할당 시 deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 방지
   - Utilization &darr;, throughput &darr;, starvation problem
2. **Deadlock Avoidance**
   - 자원 요청에 대한 부가 정보를 이용해 deadlock 가능성 없는 경우에만 자원 할당
   - 시스템 state가 원래 state로 돌아올 수 있는 경우에만 자원 할당
3. **Deadlock Detection and recovery**
   - deadlock 발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견 시 recover
4. **Deadlock Ignorance**
   - Deadlock을 시스템이 책임X
   - 대부분의 OS가 채택
   -  deadlock은 자주 발생하는 이벤트가 아니기 때문에 데드락을 방지하기 위해 많은 오버헤드를 두는 것이 비효율적

# Deadlock Prevention
1. Mutual exclusion
   - 배제 불가: 공유해서는 안 되는 자원의 경우 반드시 성립해야 함
2. Hold and wait
   - 프로세스가 자원을 요청할 때 다른 어떤 자원도 가지고 있지 않아야 함
   - sol 1) 프로세스 시작 시 모든 필요한 자원을 할당받게 함
   - sol 2) 자원이 필요한 경우 보유 자원을 모두 놓고 다시 요청
3. No preemption
   - 프로세스가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨(강제로 빼앗길 수 있음)
   - 모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작됨
   - state를 쉽게 save하고 다시 restore할 수 있는 자원에서 주로 사용(CPU, memory)
4. Circular wait
   - 모든 자원 유쳥에 할당 순서를 정하여 정해진 순서대로만 자원 할당

# Deadlock Avoidance
- 가장 단순하고 일반적인 모델은 프로세스들이 필요로 하는 각 자원별 최대 사용량을 미리 선언하도록 하는 방법
- **safe state**
   - 시스템 내의 프로세스들에 대한 safe sequence가 존재하는 상태
- **safe sequence**
   - 프로세스의 sequence가 safe하려면 $P_i$의 자원 요청이 "가용 자원 + 모든 $P_j$의 보유 자원"에 의해 충족되어야 함
   - 조건을 만족하면 다음 방법으로 모든 프로세스의 수행 보장
     - $P_i$의 자원 요청이 즉시 충족될 수 없으면 모든 $P_j$가 종료될 때까지 기다림
     - $P_{i-1}$이 종료되면 $P_i$의 자원요청을 만족시켜 수행 
- 시스템이 safe state에 있으면 &rarr; no deadlock
- 시스템이 unsafe state에 있으면 &rarr; possibility of deadlock
- Avoidance algorithm
   - Single instance per resource types: **Resource Allocation Graph Algorithm**  
   - Multiple instances per resource types: **Banker's Algorithm**

## Resource Allocation Graph Algorithm
- Clamin edge $P_i$ &rarr; $R_j$
   - 프로세스 $P_i$가 미래에 자원 $R_j$를 요청할 수 있음을 뜻함(점선)
   - 프로세스가 해당 자원 요청 시 request edge로 바뀜(실선)
   - $R_j$가 release되면 assignment edge는 다시 claim edge로 변경
- request edge의 assignment edge 변경 시 (점선을 포함하여) cycle이 생기지 않는 경우에만 요청 자원 할당
- Cycle 생성 여부 조사 시 프로세스의 수가 n일 때 $O(n^2)$ 시간이 걸림
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/d6e9845f-fef3-43f3-be52-6fd847199d19)

## Banker's Algorithm
- $P_0, P_1, P_2, P_3, P_4$
- A(10), B(5), C(7) instances
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/f3c2c9c2-1f97-437b-8ad5-1f085f79a663)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/3df0f9c8-7c60-46dd-86b8-86d1a8a040fc)


# Deadlock Detection and Recovery
- Deadlock Detection
  1. single instance per resource type: 자원 할당 그래프에서의 cycle이 곧 deadlock을 의미
  2. multiple instance per resource type: Banker's algorithm과 유사한 방법 활용
- Wait-for graph algorithm
  - single instance per resource type
  - Wait-for graph
    - 자원할당 그래프의 변형
    - 프로세스만으로 node 구성
    - $P_j$가 가지고 있는 자원을 $P_k$가 기다리는 경우 $P_k$ &rarr; $P_j$
  - algorithm
    - Wait-for graph에 *사이클이 존재하는 지*를 주기적으로 조사
    - $O(n^2)$
- Recovery
  1. **Process termination**
     - Abort all deadlocked processes
     - Abort one process at a time until the deadlock cycle is eliminated
  2. **Resource Preemption**
     - 비용을 최소화할 victim의 선정
     - safe state로 rollback하여 process를 restart
     - Starvation 문제
        - 동일한 프로세스가 게속해서 victim으로 선정되는 경우
        - cost factor에 rollback 횟수도 같이 고려

## Single instance per resource type
![image](https://github.com/Haaarimmm/TIL/assets/108309396/4e2ef6ba-b4d0-4ef8-b225-8386309a7d9a)

## Multiple instance per resource type
![image](https://github.com/Haaarimmm/TIL/assets/108309396/f2aafbc4-cb79-4497-8a8c-5f7da9d2d31a)

