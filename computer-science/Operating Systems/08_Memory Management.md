# 8. Memory Management
## Logical vs Physical Address
1. **Logical address(=virtual address)**
   - 프로세스마다 독립적으로 가지는 주소 공간
   - 각 프로세스마다 0번지부터 시작
   - **CPU가 보내는 주소는 logical address**
2. **Physical address**
   - 메모리에 실제 올라가는 위치
- 주소 바인딩(=address translation): 주소를 결정하는 것
   - Symbolic address &rarr; Logical address &rarr; Physical address

# Address Binding
![image](https://github.com/Haaarimmm/TIL/assets/108309396/dca76ed1-fd6f-4f6a-a63c-1aa10c9fcfc5)  
### 1. **Compile time binding**
- physical address가 컴파일 시 알려짐
- 시작 위치 변경 시 재컴파일
- 컴파일러는 absolute code 생성
### 2. **Load time binding**
- Loader의 책임 하에 물리적 메모리 주소 부여
- 컴파일러가 relocatable code를 생성한 경우 가능
### 3. **Execution time binding(=Run time binding)**
- 수행이 시작된 이후에도 프로세스의 메모리 상 위치를 옮길 수 있음
- CPU가 주소를 참조할 때마다 binding을 점검(address mapping table)
- 하드웨어적인 지원이 필요(base and limit registers, MMU)

# Memory-Management Unit(MMU)
- MMU: **logical address를 physical address로 매핑해주는 hardware device**
- MMU Scheme: 사용자 프로세스가 CPU에서 수행되며 생성해내는 모든 주소값에 대해 base register의 값을 더한다
- user program: logical address만을 다루며 physical address를 볼 수 없음

## Dynamic Relocation
![image](https://github.com/Haaarimmm/TIL/assets/108309396/7d496363-f5d7-4717-80b5-4a2552905eb4) 

## Hardware Support for Address Translation
![image](https://github.com/Haaarimmm/TIL/assets/108309396/f1c7ac89-2093-4d7f-b522-3d07ae7c2fec)  
- OS 및 사용자 프로세스 간의 메모리 보호를 위해 사용하는 레지스터
  - **Base register**(=relocation register): 접근할 수 있는 물리적 메모리 주소의 최소값
  - **Limit register**: 논리적 주소의 범위

# Terminologies
## Dynamic Loading
- 프로세스 전체를 메모리에 미리 다 올리는 것이 아니라 **해당 루틴이 불려질 때 메모리에 load하는 것**
- memory utilization&uarr;
- 가끔씩 사용되는 많은 양의 코드의 경우 유용(예: 오류 처리 루틴)
- OS의 특별한 지원 없이 프로그램 자체에서 구현 가능(OS는 라이브러리를 통해 지원 가능)
- Loading: 메모리로 올리는 것
- Paging처럼 OS가 지원해주는 것이 아닌, 프로그래머가 직접 구현하는 부분

## Overlays
- 메모리에 프로세스의 부분 중 실제 필요한 정보만을 올림
- 프로세스의 크기가 메모리보다 클 때 유용
- OS의 지원없이 사용자에 의해 구현
- 작은 공간의 메모리를 사용하던 초창기 시스템에서 수작업으로 프로그래머가 구현
  - Manual Overlay
  - 프로그래밍이 매우 복잡
- OS의 지원없음

## Swapping
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/0c8d3a2c-1ed0-4e08-b0da-e78ffa3d737b)
- **Swapping**: 프로세스를 일시적으로 메모리에서 backing store로 쫒아내는 것
- **Backing store(=swap area)**
  - 디스크: 많은 사용자의 프로세스 이미지를 담을 만큼 충분히 빠르고 큰 저장 공간
- Swap in / Swap out
  - 일반적으로 중기 스케줄러(swapper)에 의해 swap out 시킬 프로세스 선정
  - priority-based CPU scheduling algorithm
    - 우선순위가 낮은 프로세스를 swapped out, 높은 프로세스를 swapped in
  - Compile time 혹은 load time binding에서는 원래 메모리 위치로 swap in 해야 함
  - Execution time binding에서는 추후 빈 메모리 영역 아무 곳에나 올릴 수 있음
  - swap time은 대부분 tranfer time(swap되는 양에 비례하는 시간)

## Dynamic Linking
- Linking을 execution time까지 미루는 기법
- *Static linking*
  - 라이브러리가 프로그램의 **실행 파일 코드에 포함**됨
  - 실행 파일의 **크기가 커짐**
  - 동일한 라이브러리를 각각의 프로세스가 메모리에 올리므로 **메모리 낭비**
- *Dynamic Linking*
  - 라이브러리가 **실행 시 linking됨**
  - **라이브러리 호출 부분에** 라이브러리 루틴의 위치를 찾기 위한 **stub**이라는 작은 코드를 둠
  - 라이브러리가 이미 메모리에 **있으면 그 루틴의 주소로 가고 없으면 디스크에서 읽어옴**
  - OS의 지원 필요
  - windows: dll

# Allocation of Physical Memory
- 메모리는 일반적으로 두 영역으로 나뉨
  - **OS 상주 영역(kernel space)**: interrupt vector와 함께 낮은 주소 영역 사용
  - **사용자 프로세스 영역(user space)**: 높은 주소 영역 사용
- 사용자 프로세스 영역의 할당 방법
  1. *Contiguous allocation*: 메모리에 연속적으로 적재
     - Fixed partition allocation, Variable partition allocation
  2. *Noncontiguous allocation*: 하나의 프로세스가 메모리의 여러 영역에 분산
     - Paging, Segmentation, Paged Segmentation

# Contiguous allocation
![image](https://github.com/Haaarimmm/TIL/assets/108309396/42aa617f-ae48-4937-a93a-afe2c14188d1)  
## 1. 고정 분할 방식(Fixed partition allocation)
- 물리적 메모리를 몇 개의 영구적 분할로 나눔
- 분할의 크기가 모두 동일한 방식과 서로 다른 방식이 존재
- 분할 당 하나의 프로그램
- 융통성 X
  - 동시에 메모리에 load되는 프로그램의 수가 고정됨
  - 최대 수행 가능 프로그램 크기 제한
- **Internal fragmentation, External fragmentation 발생**
## 2. 가변 분할 방식(Variable partition allocation)
- 프로그램의 크기를 고려해 할당
- 분할의 크기, 개수가 동적으로 변함
- 기술적 관리 기법 필요
- **External fragmentation도 발생**

## External fragmentation vs Internal fragmentation
1. External fragmentation
   - 프로그램의 크기보다 분할의 크기가 작은 경우
2. Internal fragmentation
   - 프로그램의 크기보다 분할의 크기가 큰 경우
   - 하나의 분할 내부에서 발생하는 사용되지 않는 메모리 조각
   - 특정 프로그램에 배정되었지만 사용되지 않는 공간

## Hole
- 가용 메모리 공간
- 다양한 크기의 hole들이 메모리 여러 곳에 흩어져 있음
- 프로세스가 도착하면 수용가능한 hole을 할당
- OS는 할당공간과 가용공간(hole)의 정보를 유지  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/72b35f09-b541-4767-bee4-37968200a1cc)

## Dynamic Storage-Allocation Problem
- 가변 분할 방식에서 size n인 요청을 만족하는 가장 적절한 hole을 찾는 문제
1. **First-fit**
   - size가 n 이상인 것 중 **최초로 찾아지는 hole에 할당**
2. **Best-fit**
   - **size가 n 이상인 가장 작은 hole에 할당**
   - hole이 크기 순으로 정렬되지 않은 경우 모든 hole의 리스트를 탐색해야 함
   - 많은 수의 아주 작은 hole들이 생성됨
3. **Worst-fit**
   - **size가 n 이상인 가장 큰 hole에 할당**
   - 모든 리스트를 탐색해야 함
   - 상대적으로 아주 큰 hole들이 생성됨

## Compaction
- external fragmentation 문제를 해결하는 한 가지 방법
- 사용 중인 메모리 영역을 한 군데로 몰아 큰 block을 만드는 것
- 비용이 많이 듦
- Execution time binding인 경우에만 수행 가능

# Noncontiguous allocation - 1. Paging
- Process의 virtual memory를 **동일한 사이즈의 page 단위로 나눔**
- virtual memory의 내용이 page 단위로 noncontiguous하게 저장됨
- 일부는 backing storage에, 일부는 physical memory에 저장  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/94c16d85-5bd6-4239-8b5a-76b25513f49e)

## Address Translation Architecture
![image](https://github.com/Haaarimmm/TIL/assets/108309396/95e2ce5b-2312-42e0-8578-2f9453dfbec1)

## Implementation of Page Table
- Page Table은 main memory에 상주
- **Page-Table Base Register(PTBR)**: page table을 가리킴
- **Page-Table Length Register(PTLR)**: 테이블 크기를 보관
- 모든 메모리 접근 연산에는 2번의 memory access 필요
  - page table 접근 1번, 실제 date/instruction 접근 1번
- 속도 향상을 위해 Translation Look-aside Buffer(**TLB**)라 불리는 고속의 lookup hardware *cache* 사용

# Paging Hardware with TLB
![image](https://github.com/Haaarimmm/TIL/assets/108309396/622afbac-8806-4f3c-a578-02096ce52d89)

## TLB
- TLB(=Associative registers): parallel search가 가능
  - TLB에는 일부 page table이 존재
- Address Translation
  - 만약 해당 VPN가 TLB에 있는 경우 곧바로 PFN을 얻음
  - 없다면 main memory에 있는 page table로부터 PFN을 얻음
  - **TLB는 context switching 때 flush(프로세스마다 TLB를 다르게 가짐)**

## Effective Access Time
- TLB lookup time = $\epsilon$
- Memory access time = 1
- Hit ratio = $\alpha$
- EAT = (1 + $\epsilon$)$\alpha$ + (2 + $\epsilon$)(1 - $\alpha$) = 2 + $\epsilon$ - $\alpha$

# Two-Level Page Table
![image](https://github.com/Haaarimmm/TIL/assets/108309396/5f998c46-3168-43e7-986e-ae6ab6bb9b62)  
- 현대의 컴퓨터는 address space가 매우 큰 프로그램 지원
  - 32 bit address 사용 시 : $2^{30}$ = G, 4GB의 address space
    - page size가 4k 시 1M개의 PTE가 필요
    - 각 PTE가 4B시 프로세스 당 4M의 Page table 필요
    - but 대부분 프로그램은 4G 중 극히 일부분만 사용하므로 공간 낭비
  - page table 자체를 page로 구성
  - 사용되지 않는 주소 공간에 대한 outer page table의 entry 값은 NULL(대응하는 inner page table이 없음)
- Example
  - logical address: 20bit page number, 12bit page offset
  - 20bit 중 10bit page directory number, 10bit page directory offset  
  ![image](https://github.com/Haaarimmm/TIL/assets/108309396/3b81fd00-70f8-4890-a4ed-f05a5f2e9168)
  - $P_1$: outer page table의 index
  - $P_2$: outer page table의 offset
- Address-Translation Scheme    
![image](https://github.com/Haaarimmm/TIL/assets/108309396/c942a499-a90a-4a65-abb2-78bc119f00b8)

## Multilevel Paging and Performance
- Address space가 더 커지면 다단계 페이지 테이블 필요
- 각 단계의 페이지 테이블이 메모리에 존재하므로 Logical addressdml physical address **변환에 더 많은 메모리 접근 필요**
- TLB를 통해 메모리 접근 시간을 줄일 수 있음
- ex) 4단계 페이지 테이블을 사용하는 경우: 메모리 접근 5번 필요

## Valid(v) / Invalid(i) Bit in a Page Table
![image](https://github.com/Haaarimmm/TIL/assets/108309396/3989a344-34fe-41a2-ab59-e555c8ac59f5)  
- 6, 7번 page가 현재 사용되지 않지만 만들어놓고 invalid bit을 통해 check
- PTE마다 가지는 bit
  - *Protection bit*: page에 대한 접근 권한(read/write/read-only)
  - *Valid/Invalid bit*
    - valid: 해당 주소의 frame에 그 프로세스를 구성하는 유효한 내용이 있음을 뜻함(접근 허용)
    - invalid: 프로세스가 주소 부분을 사용하지 않는 경우, 해당페이지가 메모리에 올라와 있지않고 Swap area에 있는 경우(접근  불허)

# Inverted Page Table
![image](https://github.com/Haaarimmm/TIL/assets/108309396/05e125d6-af91-4873-9985-b1a38d7089a5)  
- page table이 매우 큰 이유
  - 모든 process별로 logical address에 대응되는 모든 page에 대해 PTE가 존재
  - 대응하는 page가 메모리에 있든 아니든 간에 page table에는 entry로 존재
- **Inverted Page Table**
  - **Page frame 하나 당 page table에 하나의 entry를 둔 것**(system-wide)
  - 각 PTE는 각각의 물리적 메모리의 PFN이 담고 있는 내용 표시(PID, process의 logical address)
  - 단점: 테이블 전체를 탐색해야 함
  - 조치: Base register 사용(expensive)

# Shared Page
![image](https://github.com/Haaarimmm/TIL/assets/108309396/894b5f26-be76-4b1f-8a16-ce8cab96034d)   
- Shared Page 조건
  1. Shared code(=Re-entrant, pure code)가 read-only여야 한다.
  2. 하나의 code만 메모리에 올린다.
  3. Shared code는 모든 프로세스에서 logical address가 동일해야 한다.
  - ex. text editors, window systems, compilers)
- Private code and data(↔ Shared code)
  - 각 프로세스들은 독자적으로 메모리에 올림
  - Private data는 logical address가 달라도 무방

# Noncontiguous allocation - 2. Segmentation
- 프로그램은 의미 단위인 여러 개의 segment로 구성
  - 일반적으로는 code, stack, data 부분이 하나씩의 세그먼트로 정의됨
- Segment = logical unit
  - main(), function, global variables, stack, symbol table, arrays...

## Segmentation Artchitecture
- Logical address: **<segment-number, offset>**
- Segment table
  - base - **starting physical address** of the segment
  - limit - **length** of the segment
- **Segment-Table Base Register(STBR)**: 물리적 메모리에서의 segment table의 위치
- **Segment-Table Length Register(STLR)**: 프로그램이 사용하는 segment의 수
- 장점: Segment는 의미 단이기 때문에 Sharing과 Protection에 있어 paging보다 훨씬 효과적
  - Sharing
    - shared segment
    - same segment number
    - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/d5656343-841a-481a-9ccf-d83dcd04c919)
  - Protection bit: segment별로 존재
    - Valid bit = 0 &rarr; illegal segment
    - Read/Write/Execution 권한 bit
- 단점: Segment의 길이가 동일X &rarr; 가변 분할 방식에서와 동일한 문제점들이 발생
  - Allocation
    - first fit / best fit
    - external fragmentation 발생

## Segmentation Hardware
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b48f5b1a-b5c3-4cbd-9b95-3cd0f0c2f938)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/03df8303-6a4a-43c8-8170-ac30f1437d86)

# Segmentation with Paging
![image](https://github.com/Haaarimmm/TIL/assets/108309396/9b61931d-4e71-46e1-8b15-402e424522c0)  
- Outer Table이 Segmentation, Inner Table이 Paging 기법 사용 
- pure segmentation과의 차이점
  - segment-table entry가 segment의 base address를 가지고 있는 것이 아니라 segment를 구성하는 page table의 base address를 가지고 있음
- segment offset이 segment length 이내일 경우만 valid

## Physical address 계산법
![image](https://github.com/Haaarimmm/TIL/assets/108309396/9fa1982d-76c9-4632-831f-6e858d1c3c16)  
- Logical address
  - s : Segment number
  - d : displacement(offset)
  - p : Page number
  - d' == d (if valid)
  - f : Frame number
1. STBR + s 를 통해 Segment Table Entry 찾음
2. Segment Length가 d(offset)보다 크면 통과(valid)
3. Page Table Base + p를 통해 Page Table Entry 찾음
4. PTE의 f 와 d'을 합치면 physical address