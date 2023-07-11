# 10. File Systems
## File and File System
- **File**
  - 일반적으로 비휘발성의 보조기억장치에 저장
  - OS는 다양한 저장 장치를 file이라는 동일한 논리적 단위로 볼 수 있게 해줌
  - Operation: create, read, write, reposition, delete, open, close 등
- **File attribute(파일의 metadata)**
  - 파일을 관리하기 위한 각종 정보들
    - 파일 이름, 유형, 저장된 위치, 파일 사이즈
    - 접근 권한(r/w/x), 시간(생성/변경/사용), 소유자 등
- **File system**
  - OS에서 파일을 관리하는 부분
  - 파일 및 파일의 메타데이터, 디렉토리 정보 등을 관리
  - 파일의 저장 방법 결정
  - 파일 보호 등

## Directory and Logical Disk
- **Directory**
  - 파일의 메타데이터 중 일부를 보관하고 있는 일종의 특별한 *파일*
  - 디렉토리에 속한 파일 이름 및 파일 attribute들
  - Operation: search a file, create a file, delete a file
- **Partition(= Logical Disk)**
  - 하나의 물리적 디스크 안에 여러 파티션을 두는 게 일반적
  - 여러 개의 물리적인 디스크를 하나의 파티션으로 구성하기도 함
  - 물리적 디스크를 파티션으로 구성한 뒤 각각의 파티션에 file system을 깔거나 swapping 등 다른 용도로 사용 가능

# `open()`
![image](https://github.com/Haaarimmm/TIL/assets/108309396/0285140d-8901-42b9-91ed-76fd47025fc2)
- ex) open("/a/b/c")
- 디스크로부터 파일 c의 메타데이터를 메모리로 가지고 온다.
- 이를 위해 directory path를 search 한다.
- 과정
  1. 루트 디렉토리("/")를 open하고 그 안에서 파일 "a"의 위치를 획득한다.
  2. 파일 "a"를 open한 후 read하여 그 안에서 파일 "b"의 위치를 획득한다.
  3. 파일 "b"를 open한 후 read하여 그 안에서 파일 "c"의 위치를 획득한다.
  4. 파일 "c"를 open한다.
- 과정에서 알 수 있듯이, Directory path의 search에 너무 많은 시간이 소요된다.
  - open을 read/write과 별도로 두는 이유이다.
  - 한 번 open한 파일은 read/write 시 directory search 불필요하도록 한다.
- Open file table
  - 현재 open 된 파일들의 metadata 보관소 (in memory)
  - 디스크의 metadata보다 몇 가지 정보가 추가됨
    - Open한 프로세스의 수
    - File offset : 파일 어느 위치 접근 중인지 표시 (별도 테이블 필요)
- File descriptor (file handle, file control block)
  - Open file table에 대한 위치 정보 (프로세스별)


# File Protection()
- Access Control 방법
1. Access control Matrix
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/642d185b-56db-47bc-b742-00e12c17d4d4)
   - Access control list: 파일 별로 누구에게 어떤 접근 권한이 있는지 표시
   - Capability: 사용자 별로 자신이 접근 권한을 가진 파일 및 해당 권한 표시
2. Grouping
   - 전체 user를 owner, group, public의 세 그룹으로 구분
   - 각 파일에 대해 세 그룹의 접근 권한(rwx)을 3비트씩으로 표시
   - ex) rwx(owner)r--(group)r--(other)
3. Password
   - 파일마다 password를 두는 방법(디렉토리 파일에 두는 방법도 가능)
   - 모든 접근 권한에 대해 하나의 password: all-or-nothing
   - 접근 권한 별 password: 암기 문제, 관리 문제

# Access Methods
- 시스템이 제공하는 파일 정보의 접근 방식
1. Sequential access: 읽거나 쓰면 offse은 자동적으로 증가
2. Direct access or random access: 파일을 구성하는 레코드를 임의의 순서로 접근 가능

# Allocation of File Data in Disk
1. Contiguous Allocation
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
2. Linked Allocation
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/4c19c792-61a2-4db3-b687-3823f6021b92)
   1. 장점
     - external fragmentation X
   2. 단점
     - No random access
     - Reliability 문제: 한 sector가 고장나 pointer가 유실되면 많은 부분을 잃음
     - Pointer를 위한 공간이 block의 일부가 되어 공간 효율성&darr;
       - 512bytes/sector, 4bytes/pointer 
   3. File-Allocation Table(FAT) 파일 시스템
      - 포인터를 별도의 위치에 보관하여 reliability와 공간효율성 문제 해결
3. Indexed Allocation
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
![image](https://github.com/Haaarimmm/TIL/assets/108309396/376e4d66-e247-4ef7-a0b0-2f9a7472141a)

# Free-Space Management
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b0ad42de-0014-45be-b8d3-7c3f20b937e7)  
1. Bit map of bit vector
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/0f8c8aa0-f9de-4e7f-b1e7-3637af6327d0)
   - Bit map은 부가적인 공간을 필요로 함
   - 연속적인 n개의 free block을 찾는데 효과적
2. Linked list
   - 모든 free block들을 링크로 연결(free list)
   - 연속적인 가용공간을 찾는 것은 쉽지 않다
   - 공간 낭비X
3. Grouping
   - linked list 방법의 변형
   - 첫 번째 free block이 n개의 pointer를 가짐
     - n-1 pointer는 free data block을 가리킴
     - 마지막 pointer가 가리키는 block은 또 다시 n pointer를 가짐
4. Counting
   - 프로그램들이 종종 여러 개의 연속적인 block을 할당하고 반납한다는 성질에 착안
   - (first free block, # of contiguous free blocks)을 유지

# Directory Implementation
- Linear list
  - <file name, file의 metadata>의 list
  - 구현이 간단
  - 디렉토리 내에 파일이 있는지 찾기 위해서는 linear search 필요(time-consuming)
- Hash Table
  - linear list + hashing
  - Hash table은 file name을 이 파일의 linear list의 위치로 바꾸어줌
  - search time을 없앰
  - collision 발생 가능