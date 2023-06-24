# 6. Process Synchronization
## 데이터의 접근
![image](https://github.com/Haaarimmm/TIL/assets/108309396/6c0291c2-dcfe-4101-99be-9e353603db4f)

## Race condition
![image](https://github.com/Haaarimmm/TIL/assets/108309396/7e148c85-2e21-4b42-9f45-3592cb5e9673)
- 여러 프로세스들이 동시에 공유 데이터를 접근하는 상황
- 데이터의 최종 연산 결과는 마지막에 그 데이터를 다룬 프로세스에 따라 달라짐

## Race condition이 발생하는 경우
1. Kernel 수행 중 interrupt 발생 시
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/af55e189-a555-4ed4-955b-1cd3b7389409)
2. Process가 system call을 하여 kernel mode로 수행 중인데 context switching이 일어나는 경우
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/c4e11d3b-93a6-4df7-a4de-acc7be3a0d2b)
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/5fe54edc-379c-463d-98e1-65df73772846)
3. Multiprocessor에서 shared memory 내의 kernel data
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/f5f27c79-7ac9-49ef-99d7-834f8b879ce8)

# Process Synchronization 문제
- shared data의 동시접근(concurrent access)은 데이터의 불일치 문제(inconsistency)를 발생시킬 수 있음
- consistency 유지를 위해서는 협력 프로세스(cooperating process)간의 실행 순서(orderly execution)를 정해주는 메커니즘 필요
- **race condition을 막기 위해서는 concurrent process가 synchronize되어야 함**

# The Critical-Section Problem
- n개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우
- 각 프로세스의 code section에는 공유 데이터를 접근하는 코드인 **critical section**이 존재
- Problem
  - 하나의 프로세스가 critical section에 있을 때 다른 모든 프로세스는 critical section에 들어갈 수 없어야 한다
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/18dd3919-4528-4ccc-9870-b1369c93384b)

# Initial Attempts to Solve Problem
- 두 개의 프로세스가 있다고 가정 $P_0, P_1$
- 프로세스들의 일반적인 구조  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/3cc61b81-dc82-44f3-87ba-93e2fa773d97)  
- 프로세스들은 수행의 동기화를 위해 몇몇 변수를 공유할 수 있다 &rarr; synchronization variable

# 프로그램적 해결법의 충족 조건
1. **Mutual Exclusion**(상호 배타)
   - 프로세스 Pi가 critical section 부분을 수행 중이면 다른 모든 프로세스들은 그들의 critical section에 들어가면 안 된다
2. **Progress**
   - 아무도 critical section에 있지 않은 상태에서 critical section에 들어가고자 하는 프로세스가 있으면 들어가게 해주어야 한다
3. **Bounded Waiting**
   - 프로세스가 critical section에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 critical section에 들어가는 횟수에 한계가 있어야 한다
   - 기다리는 시간이 유한해야 한다
- 가정
  - 모든 프로세스의 수행 속도는 0보다 크다
  - 프로세스들 간의 상대적인 수행 속도는 가정하지 않는다

# Algorithm 1
- Synchronization variable(`int i`, initially turn = 0)
- $P_i$ can enter its critical section if `(turn == i)`
- Process $P_0$  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/47413929-3545-4783-949c-535e70b70d10)  
- Satisfy *mutual exclusion*, but not *progress*
- 즉, 과잉양보: 반드시 한 번씩 교대로 들어가야만 함(swap-turn). 그가 turn을 내 값으로 바꿔줘야만 내가 들어갈 수 있음. 특정 프로세스가 더 빈번히 critical section을 들어가야 한다면?

# Algorithm 2
- Synchronization variable
  - `boolean flag[2]`, initially `flag[모두] = false` &rarr; no one is in CS
  - $P_i$ ready to enter its CS if `flag[i] == true`
- Process $P_i$  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/56c89871-b1a5-4191-8abc-2327a7b42c2f)
- Satisfy *mutual exclusion*, but not *progress*
- 둘 다 2행까지 수행 후 끊임없이 양보하는 상황 발생 가능

# Algorithm 3 (Peterson's Algorithm)
- Combined synchronization variables of algorithms 1 and 2
- Process $P_i$  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/3ad54988-256c-4eac-a46a-e5c53e038d98)
- meets all three requirements &rarr; solves the critical section problem for 2 processes
- **Busy waiting(= Spin lock)**(계속 CPU와 memory를 쓰면서 wait)

# Synchronization Hardware
- 하드웨어적으로 **Test & modify**를 **atomic하게** 수행할 수 있도록 지원하는 경우 앞의 문제는 간단히 해결  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/a142c5cf-0d02-4edf-bf72-93e408a618a1)  
- Mutual Exclusion with Test & Set  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/fa643a71-7695-4a28-a85d-f35645697961)

# Semaphores