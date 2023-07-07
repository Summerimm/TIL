# 9. Virtual Memory
## Demand Paging
- 대부분의 시스템은 Paging 사용 중
- Demand Paging? 실제로 필요할 때 Page를 메모리에 올리는 것
- 장점
  - I/O 양의 감소
  - Memory 사용량 감소
  - 빠른 응답 시간 &rarr; 한정된 메모리 공간을 더 잘 쓰기 때문, Disk I/O 감소 등
  - 더 많은 프로그램, 사용자 수용
- Valid/Invalid bit 사용
  - Invalid의 의미
    - 사용되지 않는 주소 영역
    - 페이지가 물리적 메모리에 없는 경우
  - 초기에는 모든 PTE가 invalid로 초기화
  - address translation 시 invalid로 set되어 있으면 &rarr; **Page fault**

## Memory에 없는 Page의 Page Table
![image](https://github.com/Haaarimmm/TIL/assets/108309396/304de973-f7c4-4528-9fd5-1b47699fb1cf)

## Page Fault
- Invalid page에 접근하면 MMU가 *page fault trap* 발생시킴
- Kernel mode로 들어가서 page fault handler가 invoke됨
- Page fault 처리 순서
  1. Invalid reference? (eg. bad address, protection violation) &rarr; abort process
  2. 빈 page frame을 가져온다. 없으면 다른 page frame을 뺏어온다.
  3. 해당 페이지를 디스크에서 메모리로 읽어온다
     1. 디스크 I/O가 끝나기까지 이 프로세스는 CPU를 preempt당함(blocked)
     2. 디스크 read가 끝나면 PTE에 frame number 기록 후 valid로 set
     3. ready queue에 프로세스를 삽입 &rarr; dispatch later
  4. 프로세스가 CPU를 잡고 다시 running
  5. 중단되었던 instruction을 재개

## Steps in Handling a Page Fault
![image](https://github.com/Haaarimmm/TIL/assets/108309396/a1aae29e-7da8-4ad2-9884-df21195b1518)

## Performance of Demand Paging
- Page Fault rate $0 \le p \le 1$
  - $p = 0$, no page faults
  - $p = 1$, every reference is a fault
- Effective Access Time = $(1 - p) \times$memory access + $p \times$(OS & HW page fault overhead + [swap page out if needed] + swap page in + OS & HW restart overhead)

## Free frame이 없는 경우
- Page replacement
  - 어떤 frame을 빼앗아올지 결정해야 함
  - 곧바로 사용되지 않을 page를 쫓아내는 것이 좋음
  - 동일한 페이지가 여러 번 메모리에서 쫓겨났다가 다시 들어올 수 있음
- Replacement Algorithm
  - page-fault rate을 최소화하는 것이 목표
  - 알고리즘 성능: 주어진 page reference string에 대해 page fault를 얼마나 내는지
  - reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/72999df8-aa97-44e7-9558-affb4c1953f8)

# Optimal Algorithm
- MIN(OPT): 가장 먼 미래에 참조되는 page를 replace
- 4 frames example  
