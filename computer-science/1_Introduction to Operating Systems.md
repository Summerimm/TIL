# 1 Introduction to Operating Systems
- OS: 컴퓨터 시스템의 **자원을 효율적으로 관리**
  - resource(자원): CPU, Memory, I/O Device

# 운영체제란?
- 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층
- 협의의 운영체제(커널): OS의 핵심부분으로 메모리에 상주하는 부분
- 광의의 운영체제: 커널 뿐 아니라 각종 주변 시스템 유틸리티를 포함한 개념

# 운영체제의 목적
1. 자원 관리
  - CPU, Memory, I/O Device 등의 효율적 관리
    - 사용자 간의 형평성 있는 자원 분배
    - 최대한의 성능
   - 사용자 및 OS 자신의 보호
   - Process, File, 메시지 등을 관리
2. 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공
   - **Virtualization(가상화): 각 프로그램들이 독자적 컴퓨터에서 수행되는 것 같은 환상을 제공**
   - 하드웨어를 직접 다루는 복잡한 부분은 OS가 대행

# 운영체제의 분류
1. 동시 작업 가능 여부
   - Single tasking: 한 번에 하나의 작업만 처리 ex) MS-DOS
   - Multi tasking: 동시에 두 개 이상의 작업 처리 &rarr; 현재 대부분의 OS ex) UNIX
2. 사용자의 수
   - Single user: MS-DOS
   - Multi user: UNIX
3. 처리 방식
   - 일괄 처리(Batch processing)
   - **시분할(Timesharing)**: 여러 작업을 수행할 때 OS가 시간 단위로 분할하여 사용
     - interactive service 가능
   - 실시간(Realtime OS): 정해진 시간 안에 어떠한 일이 반드시 종료됨이 보장되어야 함

# 운영체제의 예
1. UNIX
   - 서버를 위해 만들어짐
   - 코드의 대부분을 C언어로 작성
   - 높은 이식성
   - 최소한의 커널 구조
   - 복잡한 시스템에 맞게 확장 용이
   - 소스 코드 공개
   - 프로그램 개발에 용이
   - 다양한 버전: Linux, Solaris..
2. MS Windows
   - MS사의 다중 작업용 GUI 기반 운영 체제
   - 네트워크 환경 강화
   - DOS용 응용 프로그램과 호환성 제공
   - 불안정성(초창기)
   - 풍부한 지원 소프트웨어