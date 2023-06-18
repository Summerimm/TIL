# 4. Process Management
# 프로세스 생성(Process Creation)
- 부모 프로세스(parent process)가 자식 프로세스(child process) 생성
- 프로세스의 트리 형성
- 프로세스는 자원을 필요로 함
  - 자원은 OS로부터 받음
- 자원의 공유
  1. 부모와 자식이 모든 자원을 공유하는 모델
  2. 일부를 공유하는 모델
  3. 전혀 공유하지 않는 모델: 원칙적으로는 서로 다른 프로세스이므로 자원을 부모와 공유하지 않음 
- execution
  1. 부모와 자식은 공존하며 수행되는 모델
  2. 자식이 종료(terminate)될 때까지 부모가 기다리는(wait) 모델
- Address space
  - 자식은 부모의 공간을 복사함(binary and OS data)
  - 자식은 그 공간에 새로운 프로그램을 올림
- UNIX의 예
  1. **fork()**: 복제단계
     - **fork()** system call이 새로운 프로세스를 생성
     - 부모를 그대로 복사(OS data except PID + binary) &rarr; context 복사
     - address space 할당
  2. **exec()**: 새로운 프로그램을 덮어씌우는 단계
     - fork() 다음에 이어지는 **exec()** system call을 통해 새로운 프로그램을 메모리에 올림
- Copy-On-Write(COW)
  - write 발생 전까지는 부모와 자원 공유
  - write 발생 시 부모 프로세스 복제 후 새로운 프로그램을 올림

# 프로세스 종료(Process Termination)
1. 자발적 종료: 프로세스가 마지막 명령을 수행한 후 OS에게 이를 알려줌(**exit()**)
   - 자식이 부모에게 Output data를 보냄(via **wait()**)
   - 프로세스의 각종 자원들이 OS에게 반납됨
2. 강제 종료:부모 프로세스가 자식의 수행을 종료시킴(**abort()**)
   - 자식이 할당 자원의 한계치를 넘어섬
   - 자식에게 할당시킬 task가 없거나 더 이상 필요하지 않음
   - 부모 프로세스가 종료(exit)되는 경우
     - OS는부모 프로세스가 exit하는 경우 자식이 더 이상 수행되도록 두지 않음
     - 단계적인 종료 

# 