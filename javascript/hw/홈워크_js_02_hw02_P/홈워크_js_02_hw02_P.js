// 이곳에 코드를 작성합니다.
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  let bus = 1 + K   // 1 지점에서 K만큼 더함, 최초 도착 가능 지점
  let tmp = bus     // 도착 가능 지점
  let tmp2 = tmp
  let cnt = 0       // 충전 횟수
  while (bus < N) { // bus가 N에 도착하거나 넘어가면 종료
    let flag = 1
    for (let i = 0; i < M; i++) {
      if (chargers[i] <= bus) {
        tmp = chargers[i]
        flag = 0
      }
    }
    if (tmp2 == tmp) {
      console.log('#' + 0)
      return
    }
    bus = tmp   // 버스 충전 지점을 tmp로 변경
    tmp2 = tmp  // tmp 복사
    cnt++       // 충전 횟수 + 1
    bus += K    // 버스 충전 후 도착 가능 지점
  }
  console.log('#' + cnt)
  return
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}