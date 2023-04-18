// 1번
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
for (const i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 답: const 변수는 재선언 및 재할당이 불가능하다. 하지만 for 구문에서 매번 const i의 값이 재할당되고 있으므로 오류가 발생한다.
// 아래 코드와 같이 const를 let으로 변경하면 해결된다.
for (let i = 0; i < nums.length; i++){
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()


// 2번
console.log('2번 출력 결과')
for (num of nums) {
  console.log(num, typeof num)
  // 출력 결과
  // 1 number
  // 2 number
  // 3 number
  // 4 number
  // 5 number
  // 6 number
  // 7 number
  // 8 number
}

// 답: for...in이 아닌 for...of를 사용하면 된다. for...in은 "속성 이름"을 통해 반복, for...of는 "속성 값"을 통해 반복되기 때문.
