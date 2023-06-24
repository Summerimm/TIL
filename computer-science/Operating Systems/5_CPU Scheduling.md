# 5. CPU Scheduling
## Bursts
- continued actions, 한 번에 전송되는 data block, Period
- 프로세스 관점에서
   1. CPU Burst - CPU를 사용할 때 
   2. I/O Burst - 입출력 대기할 때
- CPU-I/O Burst Cycle이 존재

# 프로세스의 특성 분류
1. I/O-bound process: CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job(many short CPU bursts)
2. CPU-bound process: 계산 위주의 job(few very long CPU bursts)

# CPU Scheduler & Dispatcher
1. CPU Scheduler
   - **Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다**
   - OS 안에서 scheduling하는 코드를 scheduler라고 부름
2. Dispatcher
   - **CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다**
   - OS 안에서 dispatch하는 코드를 dispatcher라고 부름
   - == context switching
   - dispatch latency: context switching에 소요되는 시간
- CPU 스케줄링이 필요한 경우: 프로세스의 상태 변화가 다음과 같을 때
   1. Running &rarr; Blocked : I/O request system call
   2. Running &rarr; Ready : timer interrupt
   3. Blocked &rarr; Ready : I/O 완료 후 interrupt
   4. Terminate
- 1, 4에서의 스케줄링: 바로 Ready Queue의 새로운 프로세스를 실행 &rarr; Nonpreemptive (=강제로 빼앗지 않고 자진반납)
- 나머지는 모두 Preemptive (= 스케줄링하여 강제로 빼앗음)

# Scheduling Criteria
## Performance Measure 성능 척도
- 매 CPU burst마다 계산하는 것
1. 시스템 관점에서의 성능 척도
   - **CPU utilization(이용률)**: 전체 시간 중 CPU가 일한 시간 &rarr; UNIX 시스템에서 top 명령을 사용하여 CPU 이용률을 얻을 수 있음
   - **Throughput(처리량)**: 단위 시간 당 완료한 프로세스의 수
2. 프로세스 관점에서의 성능 척도
   - **Turnaround time(소요 시간, 반환 시간)**: 총 대기 시간 + 수행하는 데 걸린 시간
   - **Waiting time(대기 시간)**
   - **Response time(응답 시간)**: Ready Queue에 들어와서 처음 CPU를 얻기까지 걸린 시간
     - for time-sharing environment

# Scheduling Algorithms
## 1. FCFS(First-Come First-Served) 
- **먼저 온 프로세스를 먼저 처리**
- Nonpreemptive
- problem. **Convoy effect** - short process behind long process

## 2. SJF(Shortest-Job-First)
- **CPU burst time이 가장 짧은 프로세스를 가장 먼저 스케줄링**
- Nonpreemptive: 일단 CPU를 잡으면 더 짧은 CPU burst time을 가지는 process가 오더라도 완료될 때까지 넘기지 않음
- Preemptive: 더 짧은 CPU burst time을 가지는 process가 오면 CPU를 빼앗김 &rarr; SRTF(Shortest-Remaining-Time-First)
- *SRTF is optimal*: minimum avereage waiting time을 보장
- problem 1. **Starvation** CPU burst time이 긴 프로세스는 영원히 CPU를 얻지 못 함
- problem 2. **CPU burst time을 미리 알 수 없음** - 과거 사용 이력을 통해 예측은 가능(exponential averaging 사용)

### Exponential Averaging
- $t_n$ = actual length of $n^th$ CPU burst
- $\tau_{n+1}$ = predicted value for the next CPU burst
- $0 \le \alpha \le 1$
- Define: $\tau_{n+1} = \alpha t_n + (1-\alpha)\tau_n$
- $\alpha = 0$ 
   - $\tau_{n+1} = \tau_n$: Recent history does not count
- $\alpha = 1$
   - $\tau_{n+1} = t_n$: Only the actual last CPU burst counts
- 식을 풀면 다음과 같다
  - $\tau_{n+1} = \alpha t_n + (1-\alpha)\alpha t_{n-1} + ... + (1-\alpha)^j \alpha t_{n-j} + ... + (1-\alpha)^{n+1}\tau_0$
- $\alpha$ 와 $(1-\alpha)$가 둘다 1 이하이므로 후속 term은 선행 term보다 적은 가중치 값을 가진다
- 요약하면 최근 실행된 CPU burst를 오래된 CPU burst보다 많이 반영

## 3. Priority Scheduling
- **highest priority를 가진 프로세스에게 CPU 할당**(smallest integer - highest priority)
- Nonpreemtive: 일단 우선순위 높은 프로세스에게 CPU를 주면 더 높은 우선순위의 프로세스가 와도 뺏지 않음
- Preemptive: 중간에 들어온 우선순위가 더 높은 프로세스에게 CPU를 준다
- problem: **Starvation** low priority processes may **never execute**
- solution: **Aging** as time progresses **increases the priority** of the process
- priority 기준 예시: 작업의 중요도, 요청된 서비스의 종류, 프로세스의 실행 시간

## 4. Round Robin(RR)
- 현대적인 CPU scheduling
- 각 프로세스는 동일한 크기의 **time quantum**을 가짐(일반적으로 10~100ms)
- 할당 시간이 끝나면 프로세스는 preempted 당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다
- n개의 프로세스가 ready queue에 있고 할당 시간이 q time unit인 경우 각 프로세스는 최대 q단위로 CPU 시간의 1/n을 얻는다.
  - 어떤 프로세스도 q(n-1) time unit 이상 기다리지 않는다.
  - **response time이 빨라짐**
- Performance
  - q &uarr; FCFS
  - q &darr; context switching overhead가 커짐

# Multilevel Queue
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/44153c1d-992e-4e0c-add0-159fef41c90e)
- **Ready Queue를 여러 개로 분할**
  - foreground(interactive)
  - background(batch - no human interaction)
- 각 큐는 *독립적인* 스케줄링 알고리즘을 가짐
  - foreground - RR
  - background - FCFS
- 큐에 대한 스케줄링이 필요
  - Fixed priority scheduling
    - serve all from foreground then from background
    - Possibility of starvation
  - Time slice
    - 각 큐에 CPU time을 적절한 비율로 할당
    - ex. 80% to foreground in RR, 20% to background in FCFS

# Multilevel Feedback Queue
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/da0f8234-69bd-4b00-810b-39b060552835)
  - 3 Queues: 8ms, 16ms, FCFS &rarr; $Q_0, Q_1, Q_2$
  - Scheduling
    - new job이 $Q_0$로 들어감
    - CPU를 잡아서 할당 시간 8ms동안 수행
    - 8ms동안 다 끝내지 못하면 $Q_1$으로 내려감
    - $Q_1$에 줄서서 기다렸다가 CPU를 잡아서 16ms동안 수행
    - 16ms동안 끝내지 못하면 $Q_2$로 내려감
- **프로세스가 다른 큐로 이동 가능**
- ex) **aging**
- Multilevel-feedback-queue scheduler를 정의하는 parameters
  - Queue의 수
  - 각 큐의 scheduling algorithm
  - process를 상위 큐, 하위 큐로 보내는 기준
  - 프로세스가 CPU 서비스를 받으려 할 때 들어갈 큐를 결정하는 기준
- Multilevel Feedback Queue에서 상위 큐로 올라가는 방법
  1. 시간 할당량 제한
     - 보통 하위 큐에서 실행중인 프로세스가 시간 할당량을 모두 소모한 경우, 해당 프로세스는 하위 큐에 남게 되지만 MFQ에서는 상위 큐로 올라가는 기회를 주는 경우도 있음
  2. 우선순위 상승
     - 하위 큐에서 실행 중인 프로세스가 우선순위 상승 조건을 충족하는 경우, 해당 프로세스는 상위 큐로 올라갈 수 있음
     - 상승 조건은 운영체제 마다 다를 수 있지만 일반적인 두 가지 조건   
     a. 실행 시간 초과: 하위 큐에서 실행 중인 프로세스가 시간 할당량을 초과한 경우에는 상위 큐로 올라갈 수 있음   
     b. I/O 요청의 유무: 하위 큐에서 실행 중인 프로세스가 I/O 작업을 요청하는 경우, 해당 프로세스는 상위 큐로 올라갈 수 있음  

# Multiple-Processor Scheduling
- CPU가 여러 개인 경우 스케줄링은 더욱 복잡해짐
- Homogeneous processor인 경우
  - Queue에 한 줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다
  - 반드시 특정 프로세서에게 수행되어야 하는 프로세스가 있는 경우는 복잡해짐
- Load sharing
  - 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
  - 별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법
- Symmetric Multiprocessing(SMP)
  - 각 프로세서가 각자 알아서 스케줄링 결정
- Asymmetric multiprocessing
  - 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

# Real-Time Scheduling
1. **Hard real-time systems**: 정해진 시간 안에 반드시 끝내도록 스케줄링해야 함 ex) 미사일, 원자력 발전소 시스템
2. **Soft real-time computing**: 일반 프로세스에 비해 높은 priority를 갖도록 해야 함 ex) PC, 휴대폰

# Thread Scheduling
1. **Local Scheduling**: User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정
2. **Global Scheduling**: kernel level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를 스케줄할지 결정

# Algorithm Evaluation
1. Deterministic Modeling
   - 이미 주어졌다고 가정된 특정 workload를 가지고서 각 알고리즘들을 평가하는 방법
   - 쉽고 빠른 분석이 가능하지만, 주어지지 않은, 다른 종류의 workload에 대해서도 마찬가지일지는 알 수 없다.
2. **Queueing models**: 이론적인 방법
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/ffe96ee2-675c-47ca-90bc-c0a2c534aa01)
   - 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 performance index(성능 척도) 값을 계산
3. **Implementation & Measurement**
   - 실제 시스템에 알고리즘을 구현하여 실제 작업(workload)에 대해서 성능을 측정 비교
4. **Simulation**
   - 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과 비교
   - trace files란? 
     - 실제 시스템을 모니터링하고 그 이벤트의 순서를 기록함으로써 만들어 낸 파일
     - 완전히 같은 입력 집합을 가지고서 여러 알고리즘들을 비교할 수 있으므로 매우 유용하다.
   - 시뮬레이션 또한 수 시간이 걸릴 수 있을 만큼 비용이 비싸고, trace files 또한 매우 큰 저장 용량을 필요로 할 수 있다.