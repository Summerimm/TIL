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