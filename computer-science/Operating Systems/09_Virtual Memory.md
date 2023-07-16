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

# Page Fault
- Invalid page에 접근하면 MMU가 *page fault trap* 발생시킴
- Kernel mode로 들어가서 page fault handler가 invoke됨
- Page fault 처리 순서
  1. Invalid reference? (eg. bad address, protection violation) &rarr; abort process
  2. 빈 page frame을 가져온다. 없으면 다른 page frame을 뺏어온다. (page replacement)
  3. 해당 페이지를 디스크에서 메모리로 읽어온다 (Disk I/O)
     1. 디스크 I/O가 끝나기까지 이 프로세스는 CPU를 preempt당함(blocked)
     2. 디스크 read가 끝나면 PTE에 frame number 기록 후 valid로 set
     3. ready queue에 프로세스를 추가 &rarr; dispatch later
  4. 프로세스가 CPU를 잡고 다시 running
  5. 중단되었던 instruction을 재개

## Steps in Handling a Page Fault
![image](https://github.com/Haaarimmm/TIL/assets/108309396/86874e9c-dca2-4ece-aae3-a9b76c0960ba)

## Performance of Demand Paging
- Page fault rate $0 \le p \le 1$
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
- 다른 알고리즘의 성능에 대한 upper bound 제공
  - Belady's optimal algorithm, MIN, OPT 등으로 불림
- Offline algorithm: 미래의 참조를 아는 알고리즘
- 4 frames example  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/c7e185a2-17d8-48b1-9f25-aaf7ea82f10c)

# FIFO Algorithm
- FIFO: First In First Out  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/72184d04-3ea7-431d-a362-f7bc03154965)
- FIFO Anomaly(Belady's Anomaly)
  - more frames != less page faults

# LRU Algorithm
- LRU: Least Recently Used  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/8ec9940b-eec3-4366-8e3f-02927d666aec)

# LFU Algorithm
- LFU: Least Frequently Used
- 최저 참조 횟수인 page가 여럿 있는 경우
  - LFU 알고리즘 자체에서는 여러 page 중 임의로 선정
  - 성능 향상을 위해 LRU한 page를 지우게 구현할 수 있음
- 장단점
  - LRU처럼 직전 참조 시점만 보는 것이 아니라 장기적인 시간 규모를 보기 때문에 page의 인기도를 좀 더 정확히 반영 가능
  - 참조 시점의 최근성을 반영하지 못 함
  - LRU보다 구현이 복잡함

# LRU와 LFU 알고리즘의 구현
- LRU
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/ee3448dc-dd51-40ac-b216-50ea199da0f6)
  - $O(1)$
- LFU
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/a12a0937-dad6-4aa3-b556-58704e03c11d)
  - $O(n)$
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/b6fa07ac-3454-4779-88aa-e775eb846b60)
  - $O(log n)$

# 다양한 Caching 환경
- Caching
  - 한정된 빠른 공간(캐시)에 요청된 데이터를 저장해두었다가 후속 요청 시 캐시로부터 직접 서비스하는 방식
- Cache 운영의 시간 제약
  - 교체 알고리즘에서 삭제할 항목을 결정하는 일에 지나치게 많은 시간이 걸리는 경우 실제 시스템에서 사용할 수 없음
  - Buffer caching이나 Web caching의 경우 O(1)에서 O(log n)정도까지 허용
  - Paging system의 경우
    - **page fault인 경우에만 OS가 관여**
    - 페이지가 이미 메모리에 존재하는 경우 참조시각 등의 정보를 OS가 알 수 없음

# Clock Algorithm
- LRU의 근사 알고리즘 (= Second chance algorithm = NRU(Not Recently Used))
- Reference bit을 사용해서 교체 대상 페이지 선정(circular list)
- reference bit가 0인 것을 찾을 때까지 포인터를 하나씩 앞으로 이동
- 포인터 이동하는 중에 reference bit 1은 모두 0으로 바꿈
- Reference bit이 0인 것을 찾으면 그 페이지를 교체
- 한 바퀴를 돌아와서도(=second chance) 0이면 replace
- 자주 사용되는 페이지라면 second chance가 올 때도 1  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/ef167583-cae3-4ddb-b141-49d60672590b)


## Clock algorithm의 개선
  - reference bit과 modified bit(dirty bit)을 함께 사용
  - reference bit = 1: 최근에 참조된 페이지
  - modified bit = 1: 최근에 변경된 페이지(disk I/O 필요함)
    - modified bit = 0일 경우 disk I/O 없이 memory에서만 삭제하면 됨(내용이 동일하므로)

# Page Frame의 Allocation
- 실제로 프로그램이 원활하게 실행되기 위해서는 일련의 page들이 메모리에 같이 올라와 있어야 효율적임
- Allocation problem: 각 process에 얼마만큼의 page frame을 할당할 것인가?
- Allocation의 필요성
  - 메모리 참조 명령어 수행 시 명령어, 데이터 등 여러 페이지 동시 참조
    - 명령어 수행을 위해 최소한 할당되어야 하는 frame의 수가 있음
  - Loop를 구성하는 page들은 한꺼번에 allocate되는 것이 유리함
    - 최소한의 allocation이 없으면 매 loop마다 page fault
- Allocation Scheme
  - **Equal allocation**: 모든 프로세스에 똑같은 갯수 할당
  - **Proportional allocation**: 프로세스 크기에 비례하여 할당
  - **Priority allocation**: 프로세스의 priority에 따라 다르게 할당

## Global vs Local Replacement
1. Global replacement
  - replace 시 다른 process에 할당된 frame을 빼앗아 올 수 있다
  - process별 할당량을 조절하는 또 다른 방법
  - FIFO, LRU, LFU 등의 알고리즘을 global replacement로 사용 시에 해당
  - working set, PFF 알고리즘 사용
2. Local replacement
  - 자신에게 할당된 frame 내에서만 replacement
  - FIFO, LRU, LFU 등의 알고리즘을 process 별로 운영 시

# Thrashing
![image](https://github.com/Haaarimmm/TIL/assets/108309396/a81c897e-88b9-4c22-a6cc-264d16068167)  
- 많은 프로그램이 동작 &rarr; 각 프로그램에 할당된 메모리가 적어짐
- 프로세스의 원활한 수행에 필요한 최소한의 page frame 수를 할당 받지 못한 경우 발생
- Page fault rate이 매우 높아짐
- CPU utilization이 낮아짐
- OS는 MPD(Multiprogramming degree)를 높여야 한다고 판단
- 또 다른 프로세스가 시스템에 추가됨(higher MPD)
- 프로세스 당 할당된 frame의 수가 더욱 감소
- 프로세스는 page의 swap in/swap out으로 매우 바쁨(page fault 자주 발생)
- 대부분의 시간에 CPU는 한가함
- low throughput

## Thrashing의 해결방법
# 1. Working-Set Model
![image](https://github.com/Haaarimmm/TIL/assets/108309396/206946b0-1cdf-43da-90f9-2001dbe1737b)  
- Locality of reference
  - 프로세스는 특정 시간동안 일정 장소만을 집중적으로 참조함
  - **locality set**: 집중적으로 참조되는 해당 page들의 집합
- Working-set model
  - **Working set**: Locality에 기반하여 프로세스가 일정 시간동안 원활하게 수행되기 위해 한꺼번에 메모리에 올라와 있어야 하는 page들의 집합
  - Working set 모델에서는 process의 working set 전체가 메모리에 올라와 있어야 수행되고 그렇지 않을 경우 모든 frame을 반납한 후 swap out(suspended)
  - Thrashing을 방지함
  - MPD를 조절함

## Working-Set Algorithm
- Working set의 결정
  - Working set window를 통해 알아냄
  - winodw size가 $\Delta$인 경우
    - 시각 $t_i$에서의 working set WS($t_i$): Time interval [$t_i - \Delta , t_i$] 사이에 참조된 서로 다른 페이지들의 집합
  - Working set에 속한 page는 메모리에 유지, 속하지 않은 것은 버림
  - 즉, 참조된 후 $\Delta$시간 동안 해당 page를 메모리에 유지한 후 버림
- Working-Set algorithm
  - process들의 working set size의 합이 page frame의 수보다 큰 경우
    - 일부 process를 swap out시켜 남은 process의 working set을 우선적으로 충족시켜 줌(MPD를 줄임)
  - working set을 다 할당하고도 page frame이 남는 경우
    - swap out되었던 프로세스에게 working set을 할당(MPD를 늘림)
- Window size $\Delta$
  - working set을 제대로 탐지하기 위해서는 window size를 잘 결정해야 함
  - $\Delta$값이 너무 작으면 locality set을 모두 수용하지 못할 우려
  - $\Delta$값이 너무 크면 여러 규모의 locality set 수용
  - $\Delta$값이 $\infty$이면 전체 프로그램을 구성하는 page를 working set으로 간주

# 2. PFF(Page-Fault Frequency) Scheme
![image](https://github.com/Haaarimmm/TIL/assets/108309396/6ad07a85-a87c-417b-8a21-96b446827a57)  
- page-fault rate의 상한값과 하한값을 둔다
  - page-fault rate이 상한값 이상이면 frame을 더 할당함
  - page-fault rate이 하한값 이하이면 할당 frame 수를 줄임
- Free frame이 없으면 일부 프로세스를 swap out

# Page Size의 결정
- Page size &darr;
  - 페이지 수 증가
  - 페이지 테이블 크기 증가
  - Internal fragmentation 감소
  - Disk transfer의 효율성 감소
    - Seek/rotation vs transfer
  - 필요한 정보만 메모리에 올라와 메모리 이용이 효율적
    - Locality의 활용 측면에서는 좋지 않음
- Trend - Larger page size