# 6. Process Synchronization(Concurrency Control)
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
- **Busy waiting(=Spin lock)**(계속 CPU와 memory를 쓰면서 wait)

# Synchronization Hardware
- 하드웨어적으로 **Test & modify**를 **atomic하게** 수행할 수 있도록 지원하는 경우 앞의 문제는 간단히 해결  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/a142c5cf-0d02-4edf-bf72-93e408a618a1)  
- Mutual Exclusion with Test & Set  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/fa643a71-7695-4a28-a85d-f35645697961)

# Semaphores
- 앞의 방식들을 추상화시킴
- Semaphore S
  - integer variable = 자원의 개수와 같음
  - 아래의 두 가지 atomic 연산에 의해서만 접근 가능  
  ![image](https://github.com/Haaarimmm/TIL/assets/108309396/91e44ca4-0253-40ed-ba8f-9a2ae75c8bbd)
  - **P(S): lock을 얻음, V(S): lock을 반납함**

# Critical Section of n Processes
![image](https://github.com/Haaarimmm/TIL/assets/108309396/45a1c296-b81e-4c73-8a8c-67bc16f16b6e)
- busy-wait(=spin lock)는 효율적이지 못 함
- Block(Sleep) & Wakeup(=sleep lock) 방식의 구현

# Block / Wakeup Implementation
- Semaphore를 다음과 같이 정의
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/3cd9aade-f59c-40ec-83c3-7960ae03eab7)
- block과 wakeup을 다음과 같이 가정
- **block**: 커널은 block을 호출한 프로세스를 suspend시킴. 이 프로세스의 PCB를 semaphore에 대한 wait queue에 넣음
- **wakeup(P)**: block된 프로세스 P를 wakeup시킴. 이 프로세스의 PCB를 ready queue로 옮김
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/cd01d8cb-9d55-4fef-961f-320ed6f37dde)

# Implementation P() & V()
![image](https://github.com/Haaarimmm/TIL/assets/108309396/602935f0-7bbd-494a-878f-57c133a2d7f1)
- P()에서 미리 S를 1빼고 음수면 sleep
- V()에서 S에 1을 더하고 0이하면 wakeup

# Which is better?
- Block/wakeup overhead vs Critical section 길이
  - critical section 길이가 긴 경우 Block/Wakeup이 적당
  - critical section 길이가 매우 짧은 경우 Block/Wakeup overhead가 busy-wait overhead보다 더 커질 수 있음
  - 일반적으로는 Block/wakeup 방식이 better!

# Two Types of Semaphores
1. Counting semaphore
   - 도메인이 0 이상인 임의의 정수값
   - 주로 resource counting에 사용
2. Binary semaphore(=mutex)
   - 0 또는 1 값만 가질 수 있는 semaphore
   - 주로 mutual exclusion(lock/unlock)에 사용

# Problem: Deadlock and Starvation
1. Deadlock
   - 둘 이상의 프로세스가 서로 상대방에 의해 충족될 수 있는 event를 무한히 기다리는 현상
   - S와 Q가 1로 초기화된 semaphore라 하자.
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/1371a01a-8f05-43d0-98b5-87dd92219c05)
2. Starvation
   - Indefinite blocking: 프로세스가 suspend된 이유에 해당하는 세마포어 큐에서 빠져나갈 수 없는 현상

# Classical Problems of Synchronization
## 1. Bounded-Buffer Problem(Producer-Consumer Problem)
![image](https://github.com/Haaarimmm/TIL/assets/108309396/ffbe53b1-781b-4413-8e86-ec3b25202e29)  
- Shared data: buffer 자체 및 buffer 조작 변수(empty/full buffer의 시작 위치)
- Synchronization variables
   - mutual exclusion &rarr; Need binary semaphore(shared data의 mutual exclusion을 위해)
   - resource count &rarr; Need integer semaphore(남은 full/empty buffer의 수 표시)
   - `semaphore full = 0`(full buffer의 개수 count), `empty = n`(empty buffer의 개수 count), `mutex = 1`(lock을 걸기 위한 변수)
- pseudo-code   
![image](https://github.com/Haaarimmm/TIL/assets/108309396/d0cd4e7f-75cf-44c2-a7bb-489de3631819)

## 2. Readers and Writers Problem
- 한 process가 DB에 write 중일 때 다른 process가 접근하면 안 됨
- read는 동시에 여럿이 해도 됨
- solution
  - Writer가 DB에 접근 허가를 아직 얻지 못한 상태에서는 모든 대기 중인 Reader들을 다 DB에 접근하게 해준다
  - Writer는 대기 중인 Reader가 하나도 없을 때 DB 접근이 허용된다
  - 일단 Writer가 DB에 접근 중이면 Reader들은 접근이 금지된다
  - Writer가 DB에서 빠져나가야만 Reader의 접근이 허용된다
- Shared data: `DB 자체, int readcnt = 0(현재 DB에 접근 중인 Reader의 수)`
- Synchronization variables
  - `semaphore mutex = 1`: 공유 변수 readcnt를 접근하는 critical section의 mutual exclusion 보장을 위해 사용
  - `db = 1`: Reader와 Writer가 공유 DB 자체를 올바르게 접근하게 하는 역할
- pseudo-code    
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b4900a5b-bc23-4a25-99ce-ef76429ccd44)

## 3. Dining-Philosophers Problem
- Synchronization variables: semaphore chopstick[5](initially all values are 1)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/2e729995-cf99-4ebe-9cc7-877260d451b2)
![image](https://github.com/Haaarimmm/TIL/assets/108309396/8a5d17ad-2d4f-4014-ac3c-4d9d42d9ff95)
- problem
  - Deadlock의 가능성 존재
  - 모든 철학자가 동시에 배가 고파져 왼쪽 젓가락을 집어버린 경우
- solution
  - 4명의 철학자만이 테이블에 동시에 앉을 수 있도록 한다
  - 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다
    ![image](https://github.com/Haaarimmm/TIL/assets/108309396/fee18782-7ab7-4b46-81c4-c87cc57f44c0)
  - 비대칭: 짝수(홀수)철학자는 왼쪽(오른쪽) 젓가락부터 집도록

# Semaphore의 문제점
- 구현 어려움
- 정확성 입증이 어려움
- 자발적 협력이 필요
- 한 번의 실수가 모든 시스템에 치명적 영향
- example  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/6496d079-92f8-4663-a70e-fa9f3aed4113)

# Monitor(Condition Variable)
- 동시 수행 중인 프로세스 사이에서 abstract data type의 안전한 공유를 보장하기 위한 high-level synchronization construct  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/e21a0429-717f-49f0-b28f-cddc34b7866e)
- 모니터 내에서는 한 번에 하나의 프로세스만이 활동 가능
- 프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요없음
- 프로세스가 모니터 안에서 기다릴 수 있도록 하기 위해 condition variable 사용(`condition x, y`)
- Condition variable은 **wait**과 **signal**연산에 의해서만 접근 가능
  - `x.wait()`: `x.wait()`을 invoke한 프로세스는 다른 프로세스가 `x.signal()`을 invoke하기 전까지 suspend된다
  - `x.signal()`: `x.signal()`은 정확하게 하나의 suspend된 프로세스를 resume한다. suspend된 프로세스가 없으면 아무 일도 일어나지 않음
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/f1a3cb5d-795b-463d-bd16-a271739a017c)

## Condition Variable: Bounded-Buffer Problem
![image](https://github.com/Haaarimmm/TIL/assets/108309396/177ee093-4e7d-4a89-a034-d7d824e1fcba)

## Condition Variable: Dining Philosophers Problem
![image](https://github.com/Haaarimmm/TIL/assets/108309396/ef79bf48-2bc3-450a-be93-0ede0672adce)

# Semaphore vs Monitor
- 세마포어
  - 주로 공유 자원의 동시 접근을 제어하기 위해 사용
  - 여러 프로세스가 공유 자원에 접근하는 순서를 조정하고, 상호 배제와 동기화를 달성할 수 있음
  - 세마포어는 저수준의 동기화 메커니즘이며, 개발자가 직접 세마포어를 조작해야 함
- 모니터
  - 고급 프로그래밍 언어에서 제공되는 동기화 추상화입니다.
  - 모니터는 더 추상화된 수준에서 동기화를 처리하며, 개발자는 모니터 내에서 프로시저를 작성하여 상호 배제와 동기화를 자동으로 처리할 수 있음
- 요약
  - 세마포어는 저수준의 원시 동기화 도구로서 다양한 동기화 문제를 해결하는 데 사용
  - 모니터는 고수준의 추상화로서 모듈화와 코드의 가독성을 향상시키는 데 중점을 둠
  - 따라서, 세마포어는 프로세스 간의 동기화에 더 많은 유연성을 제공, 모니터는 모듈 수준에서의 동기화와 추상화를 제공