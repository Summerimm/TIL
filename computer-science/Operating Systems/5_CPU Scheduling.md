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
   - Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다
   - OS 안에서 scheduling하는 코드를 scheduler라고 부름
2. Dispatcher
   - CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다
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
1. 시스템 관점에서의 성능 척도
   - CPU utilization(이용률): 전체 시간 중 CPU가 일한 시간
   - Throughput(처리량): 단위 시간 당 완료한 프로세스의 수
2. 프로세스 관점에서의 성능 척도
   - Turnaround time(소요 시간, 반환 시간): 총 대기 시간 + 수행하는 데 걸린 시간
   - Waiting time(대기 시간)
   - Response time(응답 시간): Ready Queue에 들어와서 처음 CPU를 얻기까지 걸린 시간
     - for time-sharing environment

# Scheduling Algorithms
## 1. FCFS(First-Come First-Served) 
- 먼저 온 프로세스를 먼저 처리
- problem: **Convoy effect** short process behind long process

## 2. SJF(Shortest-Job-First)
- CPU burst time이 가장 짧은 프로세스를 가장 먼저 스케줄링
- Nonpreemptive: 일단 CPU를 잡으면 더 짧은 CPU burst time을 가지는 process가 오더라도 완료될 때까지 넘기지 않음
- Preemptive: 더 짧은 CPU burst time을 가지는 process가 오면 CPU를 빼앗김 &rarr; SRTF(Shortest-Remaining-Time-First)
- SRTF is optimal: minimum avereage waiting time을 보장
- problem 1. **Starvation** CPU burst time이 긴 프로세스는 영원히 CPU를 얻지 못 함
- problem 2. CPU burst time을 미리 알 수 없음 - 과거 사용 이력을 통해 예측은 가능(exponential averaging 사용)

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

## 3. Priority Scheduling
- highest priority를 가진 프로세스에게 CPU 할당(smallest integer - highest priority)
- Nonpreemtive: 일단 우선순위 높은 프로세스에게 CPU를 주면 더 높은 우선순위의 프로세스가 와도 뺏지 않음
- Preemptive: 중간에 들어온 우선순위가 더 높은 프로세스에게 CPU를 준다
- problem: **Starvation** low priority processes may **never execute**
- solution: **Aging** as time progresses **increases the priority** of the process

## 4. Round Robin(RR)
- 현대적인 CPU scheduling
- 각 프로세스는 동일한 크기의 **time quantum**을 가짐(일반적으로 10~100ms)
- 할당 시간이 끝나면 프로세스는 preempted 당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다
- n개의 프로세스가 ready queue에 있고 할당 시간이 q time unit인 경우 각 프로세스는 최대 q단위로 CPU 시간의 1/n을 얻는다.
  - 어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다.
  - **response time이 빨라짐**
- Performance
  - q &uarr; FCFS
  - q &darr; context switching overhead가 커짐