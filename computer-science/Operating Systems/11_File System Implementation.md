# 11. File System Implementation
# Allocation of File Data in Disk
## 1. Contiguous Allocation
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/b8aa20da-05d7-4340-84dd-8110686773b3)
  1. 단점
     - external fragmentation
     - File grow가 어려움
       - file 생성 시 얼마나 큰 hole을 배당할 것인가?
       - grow 가능 vs 낭비(internal fragmentation)
  2. 장점
     - Fast I/O
       - 파일의 용량과 관계없이 한 번의 seek/rotation으로 많은 바이트 transfer
       - realtime file용으로, 또는 이미 run 중이던 process의 swapping용
     - Direct access(=random access) 가능
## 2. Linked Allocation
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/4c19c792-61a2-4db3-b687-3823f6021b92)
   1. 장점
     - external fragmentation X
   2. 단점  
      - No random access  
      - Reliability 문제: 한 sector가 고장나 pointer가 유실되면 많은 부분을 잃음  
      - Pointer를 위한 공간이 block의 일부가 되어 공간 효율성&darr;
        - 512 bytes/sector, 4 bytes/pointer 
   3. File-Allocation Table(FAT) 파일 시스템
      - 포인터를 별도의 위치에 보관하여 reliability와 공간효율성 문제 해결
## 3. Indexed Allocation
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/15d70bd3-4542-4a2f-bc79-fae90352a7bb)
   1. 장점
      - external fragmentation X  
      - Direct access 가능
   2. 단점
      - small file: 공간 낭비(실제로 많은 file들이 small)
      - Too large file: 하나의 block으로 index를 저장하기에 부족
      - 해결방안: linked scheme, multi-level index

# UNIX File system의 구조
![image](https://github.com/Haaarimmm/TIL/assets/108309396/2aca0e44-0027-417c-8eb1-d5c6a6949245)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/305af9ee-0a40-4c8f-94e6-f2275ae2d1d1)
1. Boot block: 부팅에 필요한 정보
2. Superblock: 파일 시스템에 관한 총체적인 정보를 담고 있다
3. Inode: 파일 이름을 제외한 파일의 모든 메타 데이터를 저장
4. Data block: 파일의 실제 내용을 보관

# FAT File System
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/376e4d66-e247-4ef7-a0b0-2f9a7472141a)
  - FAT: 파일의 메타데이터 중 위치정보만을 FAT에 보관한다.
  - 나머지는 메타데이터는 디렉토리가 보관한다.
  - linked allocation 형태의 위치정보를 블록에 담고있는 것이 아니라, FAT에 저장한다.
  - 배열 형태로 각 블록의 다음 블록을 저장하고 있다.
- 장점
  - 배드섹터가 발생하더라도 FAT에서 pointer를 관리하므로 reliability 해결
  - FAT 테이블만 메모리에 올려두면 디스크의 block에 직접 접근이 가능하다.
  - 공간 효율성 문제 해결

# Free-Space Management
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b0ad42de-0014-45be-b8d3-7c3f20b937e7)  

## 1. Bit map of bit vector
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/0f8c8aa0-f9de-4e7f-b1e7-3637af6327d0)
- Bit map은 부가적인 공간을 필요로 함
- 연속적인 n개의 free block을 찾는데 효과적

## 2. Linked list
- 모든 free block들을 링크로 연결(free list)
- 연속적인 가용공간을 찾는 것은 쉽지 않다
- 공간 낭비X

## 3. Grouping
- linked list 방법의 변형
- 첫 번째 free block이 n개의 pointer를 가짐
  - n-1 pointer는 free data block을 가리킴
  - 마지막 pointer가 가리키는 block은 또 다시 n pointer를 가짐

## 4. Counting
   - 프로그램들이 종종 여러 개의 연속적인 block을 할당하고 반납한다는 성질에 착안
   - (first free block, # of contiguous free blocks)

# Directory Implementation
## 1. Linear list
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/496df533-7c5a-48af-979a-5bae2b102a78)
   - <file name, file의 metadata>의 list
   - 구현이 간단
   - 디렉토리 내에 파일이 있는지 찾기 위해서는 linear search 필요(time-consuming)

## 2. Hash Table
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/5565267d-0e3b-4b6d-b019-56ccdd149d4a)
   - linear list + hashing
   - Hash table은 file name을 이 파일의 linear list의 위치로 바꾸어줌
   - 직접 접근이 가능하므로 search time을 없앰
   - Hash collision 발생 가능

### File의 metadata의 보관 위치
  - 디렉토리 내에 직접 보관
  - 디렉토리에는 포인터를 두고 다른 곳에 보관: inode, FAT 등

### Long file name의 지원
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/92ebcc43-2b22-443a-9ece-d4f463897590)
   - <file name, file의 metadata>의 list에서 각 entry는 일반적으로 고정 크기
   - file name이 고정 크기의 entry 길이보다 길어지는 경우 entry의 마지막 부분에 이름의 뒷부분이 위치한 곳의 포인터를 두는 방법
   - 이름의 나머지 부분은 동일한 directory file의 일부에 존재

# VFS and NFS
![image](https://github.com/Haaarimmm/TIL/assets/108309396/74b7f77d-938e-42c9-9a20-e7f357e3c886)  
## 1. Virtual File System(VFS)
   - 서로 다른 다양한 file system에 대해 동일한 시스템 콜 인터페이스(API)를 통해 접근할 수 있게 해주는 OS의 layer

## 2. Network File System(NFS)
   - 분산 시스템에서는 네트워크를 통해 파일 공유 가능
   - NFS는 분산 환경에서의 대표적인 파일 공유 방법

# Page Cache and Buffer Cache
## Page Cache
- Virtual memory의 paging system에서 사용하는 page frame을 caching의 관점에서 설명하는 용어
- Memory-Mapped I/O를 쓰는 경우 file의 I/O에서도 page cache 사용

## Memory-Mapped I/O
- File의 일부를 virtual memory에 mapping 시킴
- 매핑시킨 영역에 대한 메모리 접근 연산은 파일의 입출력을 수행하게 함

## Buffer Cache
- 파일 시스템을 통한 I/O 연산은 OS가 메모리의 특정 영역인 buffer cache 사용
- File 사용의 locality 활용
  - 한 번 읽어온 block에 대한 후속 요청 시 buffer cache에서 즉시 전달
- 모든 프로세스가 공용으로 사용
- Replacement algorithm 필요(LRU, LFU 등)

## Unified Buffer Cache
- 최근의 OS에서는 기존의 buffer cache가 page cache에 통합됨

# Page Cache and Buffer Cache
![image](https://github.com/Haaarimmm/TIL/assets/108309396/05982d51-fb8f-4abd-a1de-a8a226bf1243)![image](https://github.com/Haaarimmm/TIL/assets/108309396/f519f422-8ec7-458f-8cf3-1385c76ee223)
- read(), write() system call - 반드시 OS를 거쳐 buffer cache에 있으면 바로 전달
- memory-mapped I/O system call - buffer cache에 읽어온 후 page cache에 copy함
  - OS 간섭없이 memory 접근을 통해 file 입출력 가능
- Unified buffer cache 사용 시 경로가 단순해짐

# Program Execution
- 프로그램 실행 &rarr; File system에 저장된 실행파일을 실행하여 프로세스가 됨 &rarr; 프로세스만의 독자적인 주소 공간이 생성
- 실행할 부분은 실제 메모리에 올라가고, 나머지는 swap area에 보관됨
- 하지만 주소공간 중 **code 영역**은 이미 실행파일 형태로 *read-only 형태로 저장*되어 있음
- 메모리 주소 공간이 만들어질 때 data, stack 영역은 만들어져서 메모리에 올라가고 사용되지 않으면 swap area로 내려감
- 하지만 code 영역은 이미 실행파일에 들어있기 때문에 page를 삭제해버리고 필요해지면 file system으로부터 이 영역을 불러옴
- 이는 메모리에 프로세스를 올리는 loader가 쓰는 memory-mapped I/O의 일종: 프로세스의 주소공간 중 code 영역을 실행파일에 mapping


# Memory-mapped I/O를 통해 데이터 파일을 사용하는 과정
- 어떤 프로세스가 데이터 파일을 memory-mapped I/O를 통해 사용하고자 할 때, `mmap()` 시스템 콜을 통해 해당 파일을 자신의 주소공간에 매핑
- 그럼 실제 메모리 상의 페이지에도 파일에 매핑된 페이지가 존재할 것
- 이 페이지를 조회하고자 하면 아직 매핑만 된 상태이고 파일이 올라오지 않았으므로 page fault가 발생함
- 이 때는 swap area에서 page를 불러오는 것이 아니라 file system에 가서 파일의 내용을 메모리에 올려야 함

# Read-Write system call을 통해 읽는 과정
- 어떤 프로세스가 데이터 파일을 사용하고자 할때, `read()` 시스템콜을 통해 운영체제가 현재 buffer cache(page cache)에 올라와있지 않은 데이터 파일을 buffer cache(page cache)에 등록한다. 
- 그리고 사용자 프로세스 주소공간에 복사하여 사용할 수 있도록 해준다.