# 4. Process Management
# 프로세스 생성(Process Creation)
- 부모 프로세스가 자식 프로세스를 생성함
- 프로세스 생성 시 트리(계층 구조) 형성
- 프로세스는 자원을 필요로 함 &rarr; 자원은 OS로부터 받음
- 자원의 공유에 따른 분류
  1. 부모와 자식이 모든 자원을 공유하는 모델
  2. 일부를 공유하는 모델
  3. 전혀 공유하지 않는 모델: 원칙적으로는 서로 다른 프로세스이므로 자원을 부모와 공유하지 않음 
- execution에 따른 분류
  1. 부모와 자식이 공존하며 수행되는 모델
  2. 자식이 종료(terminate)될 때까지 부모가 기다리는(wait) 모델
- Address space
  - 자식은 부모의 공간을 복사함(binary and OS data)
  - 자식은 그 공간에 새로운 프로그램을 올림

## 프로세스 생성 과정
- UNIX의 예
  1. **fork()**: 복제단계
     - **fork()**가 새로운 프로세스를 생성
     - 부모를 그대로 복사(OS data except PID + binary) &rarr; context 복사
     - address space 할당
  2. **exec()**: 새로운 프로그램을 덮어씌우는 단계
     - fork() 다음에 이어지는 **exec()**을 통해 새로운 프로그램을 메모리에 올림

## Copy-On-Write(COW)
- write 발생 전까지는 부모와 자원 공유
- write 발생 시 부모 프로세스 복제 후 새로운 프로그램을 올림

# 프로세스 종료(Process Termination)
1. 자발적 종료: 프로세스가 마지막 명령을 수행한 후 OS에게 이를 알려줌 **exit()**
   - 자식이 부모에게 Output data를 보냄(via **wait()**)
   - 프로세스의 각종 자원들이 OS에게 반납됨
2. 강제 종료:부모 프로세스가 자식의 수행을 종료시킴 **abort()**
   - 자식이 할당 자원의 한계치를 넘어섬
   - 자식에게 할당시킬 task가 없거나 더 이상 필요하지 않음
   - 부모 프로세스가 종료(exit)되는 경우
     - OS는부모 프로세스가 exit하는 경우 자식이 더 이상 수행되도록 두지 않음
     - 단계적인 종료 

# fork()
![image](https://github.com/Haaarimmm/TIL/assets/108309396/04660658-7154-46f0-ab76-9fd325b1d238)  
- Parent process: pid > 0
- Child process: pid = 0
- child process는 parent의 PC값을 복제하기 때문에 fork() 이후부터 실행 

# exec()
![image](https://github.com/Haaarimmm/TIL/assets/108309396/31a48cd0-12c6-4bf1-a10c-0f094f5697ac)  
- exec() 시 추가해준 해당 프로그램의 main 함수 처음부터 실시
- exec() 시 되돌리기는 불가능
- echo &rarr; 뒤에 나오는 argument를 그대로 화면에 출력함 

# wait()
- 프로세스 A가 wait() 시스템 콜을 호출하면
  - 커널은 child가 종료될 때까지 프로세스 A를 sleep시킨다 (blocked)
  - child process가 종료되면 커널은 프로세스 A를 깨운다 (ready)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/004ae769-e90c-4b95-b354-90cc3da68ae3)

# exit()
- 자발적 종료
  - 마지막 statement 수행 후 exit() 시스템 콜을 통해
  - 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌
- 비자발적 종료
  1. 부모 프로세스가 자식 프로세스를 강제 종료시킴
    - 자식 프로세스가 한계치를 넘어서는 자원 요청
    - 자식에게 할당된 태스크가 더 이상 필요하지 않음
  2. 키보드로 kill, break 등을 친 경우
  3. 부모가 종료하는 경우
    - 부모 프로세스가 종료하기 전에 자식들이 먼저 종료됨

# 프로세스와 관련된 System call
1. **fork()** - create a child(copy)
2. **exec()** - overlay new image
3. **wait()** - sleep until child is done
4. **exit()** - frees all the resources, notify parent

# 프로세스 간 협력
1. 독립적 프로세스(Independent process)
   - 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못 함
2. 협력 프로세스(Cooperating process)
   - 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음
3. 프로세스 간 협력 매커니즘(IPC: Interprocess Communication)
   - 메시지를 전달하는 방법
     - **message passing**: 커널을 통해 메시지 전달
   - 주소 공간을 공유하는 방법
     - **shared memory**: 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 shared memory
     - **thread**: 사실 상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 process를 구성하는 thread 간에는 주소 공간을 공유하므로 협력이 가능

# Message passing
- Message system
  - 프로세스 사이에 shared variable를 일체 사용하지 않고 통신하는 시스템
  - 반드시 kernel을 통해서 전달
1. Direct Communication
   - 통신하려는 프로세스의 이름을 명시적으로 표시
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/28a1004b-1f14-475e-a8b4-6fbd3dda8683)
2. Indirect Communication
   - mailbox(또는 port)를 통해 메시지를 간접 전달
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/1f22d4da-9f6f-4862-976b-5b37f636d872)

# Message passing vs Shared memory
![image](https://github.com/Haaarimmm/TIL/assets/108309396/9c145094-3d76-4d5f-8604-623b88d32724)