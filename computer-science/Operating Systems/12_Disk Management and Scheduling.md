# 12. Disk Management and Scheduling
## Disk Structure
- **logical block**
  - 디스크의 외부에서 보는 디스크의 단위 정보 저장 공간들
  - 주소를 가진 1차원 배열처럼 취급
  - 정보를 전송하는 최소 단위
- **sector**
  - 디스크 관리의 최소 단위
  - logical block이 물리적인 디스크에 매핑된 위치
  - sector 0은 최외곽 실린더의 첫 트랙에 있는 첫 번째 섹터이다

## Disk Management
### 1. physical formatting(Low-level formatting)
- 디스크를 컨트롤러가 읽고 쓸 수 있도록 섹터들로 나누는 과정
- 각 섹터는 **header + 실제 data(512 bytes) + trailer**로 구성
- header와 trailer는 sector number, ECC(Error-Correcting Code) 등의 정보가 저장되며 controller가 직접 접근 및 운영

### 2. Partitioning
- 디스크를 하나 이상의 실린더 그룹으로 나누는 과정
- OS는 이것을 *독립적 disk*로 취급(logical disk)

### 3. logical formatting
- 파일 시스템을 만드는 것
- FAT, inode, free space 등의 구조 포함

### 4. Booting
- ROM에 있는 small bootstrap loader의 실행
- sector 0(boot block)을 load하여 실행
- sector 0은 full Bootstrap loader program
- OS를 디스크에서 load하여 실행 

# Disk Scheduling
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/5014b1ad-0ab0-4ae4-b207-08abe278d2e2)

- Access time의 구성
  1. Seek time: 헤드를 해당 실린더로 움직이는데 걸리는 시간
  2. Rotational latency: 헤드가 원하는 섹터에 도달하기까지 걸리는 회전 지연시간
  3. Transfer time: 실제 데이터의 전송 시간
- Disk bandwidth: 단위 시간 당 전송된 바이트의 수
- Disk Scheduling: seek time을 최소화하는 것이 목표, seek time = seek distance

# Disk Scheduling Algorithm
### 1. FCFS(First Come First Served)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/27cf7735-befb-4166-b7ca-7e9624012ae8)

### 2. SSTF(Shortest Seek Time First)
- starvation 문제 발생  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/0bc79153-a87c-4a9d-b90a-cac4de6a073e)

### 3. SCAN  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/b63435c4-1819-4a51-8294-6180d013a045)  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/4671c4d7-df1f-43ab-84d0-e963c96501c0)
- disk arm이 디스크의 한 쪽 끝에서 다른 쪽 끝으로 이동$하며 가는 길목에 있는 모든 요청을 처리
- 다른 쪽 끝에 도달하면 역방향으로 이동하며 똑같이 처리
- 문제점: 실린더 위치에 따라 대기 시간이 다름

### 4. C-SCAN(Circular SCAN)  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/59ab75b3-3a52-4af6-a03c-61eadd188cf8)  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/362f6b14-b2ab-40d0-8e25-4b4074285ccb)
- 헤드가 한쪽 끝에서 다른 쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리
- 다른 쪽 끝에 도달했으면 요청을 처리하지 않고 곧바로 출발점으로 다시 이동
- SCAN보다 균일한 대기 시간 제공

### 5. N-SCAN
- 일단 arm이 한 방향으로 움직이기 시작하면 그 시점 이후에 도착한 job은 되돌아올 때 service

### 6. LOOK and C-LOOK
- 헤드가 진행 중이다가 그 방향에 더 이상 기다리는 요청이 없으면 헤드의 이동방향을 즉시 반대로 이동  
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/de016786-455d-4a84-b77d-254fb7d938df)

# Disk-Scheduling Algorithm의 결정
- SCAN, C-SCAN 및 그 응용 알고리즘은 LOOK, C-LOOK 등이 일반적으로 디스크 입출력이 많은 시스템에서 효율적인 것으로 알려져 있음
- File의 할당 방법에 따라 디스크 요청이 영향을 받음
- 디스크 스케줄링 알고리즘은 필요할 경우 다른 알고리즘으로 쉽게 교체할 수 있도록 OS와 별도의 모듈로 작성되는 것이 바람직함

# Swap-Space Management
- Disk를 사용하는 두 가지 이유
  1. memory의 volatile한 특성 &rarr; file system
  2. 프로그램 실행을 위한 memory 공간 부족 &rarr; swap space(swap area)
- Swap-space
  - Virtual memory system에서는 디스크를 memory의 연장 공간으로 사용
  - 파일시스템 내부에 둘 수도 있으나 별도 partition 사용이 일반적
    - 공간효율성보다는 속도 효율성이 우선
    - 일반 파일보다 훨씬 짧은 시간만 존재하고 자주 참조됨
    - 따라서, block의 크기 및 저장 방식이 일반 파일시스템과 다름
    - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/d53133e6-efab-4b61-bf7a-62ee8eb0585e)

# RAID
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/47ee10c1-042b-470a-b97d-0f3ae38e4a26)
- Redundant Array of Independent Disks: 여러 개의 디스크를 묶어서 사용
- RAID의 사용 목적
   1. 디스크 처리 속도 향상 
      - 여러 디스크에 block의 내용을 분산 저장 &rarr; 동시 액세스 가능
      - 병렬적으로 읽어 옴(interleaving, striping)
   2. 신뢰성(reliability) 향상
      - 동일 정보를 여러 디스크에 중복 저장
      - 하나의 디스크가 고장 시 다른 디스크에서 읽어옴(Mirroring, shadowing)
        - Disk mirroring: 디스크에 저장된 데이터들은 짝을 이루고 있는 미러 디스크의 같은 위치에 복사
      - 단순한 중복 저장이 아니라 일부 디스크에 parity를 저장하여 공간의 효율성을 높일 수 있다
        - parity bit $p = b1 ⊕ b2 ⊕ b3 ⊕ b4$ 
        - 단점: 쓰기 동작 때마다 parity bit 갱신 필요 &rarr; 시간 지연 발생
        - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/4ef55884-0be8-4e31-97b3-dfa10aa7d63e)