# 5. CPU Scheduling
# 프로세스의 특성 분류
1. I/O-bound process: CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job(many shor CPU bursts)
2. CPU-bound process: 계산 위주의 job(few very long CPU bursts)

# CPU Scheduler & Dispatcher
1. CPU Scheduler
   - Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다
   - OS 안에서 scheduling하는 코드를 scheduler라고 부름
2. Dispatcher
   - CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다
   - == context switching
- CPU 스케줄링이 필요한 경우: 프로세스의 상태 변화가 다음과 같을 때
   1. Running &rarr; Blocked : I/O request system call
   2. Running &rarr; Ready : timer interrupt
   3. Blocked &rarr; Ready : I/O 완료 후 interrupt
   4. Terminate
- 1, 4에서의 스케줄링: nonpreemptive (=강제로 빼앗지 않고 자진반납)
- 나머지는 모두 preemptive (= 강제로 빼앗음)