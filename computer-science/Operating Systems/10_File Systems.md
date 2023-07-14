# 10. File Systems
## File and File System
- **File**
  - 일반적으로 **비휘발성 보조기억장치**에 저장
  - OS는 다양한 저장 장치를 **file이라는 동일한 논리적 단위**로 볼 수 있게 해줌
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
### **Directory**
- 파일의 메타데이터 중 일부를 보관하고 있는 일종의 특별한 *파일*
- **디렉토리에 속한 파일 이름 및 파일 attribute들**
- Operation: search a file, create a file, delete a file

### **Partition(= Logical Disk)**
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


# File Protection - Access Control Method
## 1. Access control Matrix
   - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/642d185b-56db-47bc-b742-00e12c17d4d4)
   - Access control list: 파일 별로 누구에게 어떤 접근 권한이 있는지 표시
   - Capability: 사용자 별로 자신이 접근 권한을 가진 파일 및 해당 권한 표시
## 2. Grouping
   - 전체 user를 *owner, group, public*의 세 그룹으로 구분
   - 각 파일에 대해 세 그룹의 접근 권한(rwx)을 3비트씩으로 표시
   - ex) rwx(owner)r--(group)r--(other)
## 3. Password
   - 파일마다 password를 두는 방법(디렉토리 파일에 두는 방법도 가능)
   - 모든 접근 권한에 대해 하나의 password: all-or-nothing
   - 접근 권한 별 password: 암기 문제, 관리 문제

## Access Methods
- 시스템이 제공하는 파일 정보의 접근 방식
1. **Sequential access**: 읽거나 쓰면 *offset은 자동적으로 증가*
2. **Direct access or random access**: 파일을 구성하는 레코드를 *임의의 순서*로 접근 가능