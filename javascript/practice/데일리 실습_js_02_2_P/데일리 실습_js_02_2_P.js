/* 
  1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
  2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
  3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
  4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
  5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
*/

const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]


console.log('1번')
users.forEach(function (user) {
  console.log(user.name)
} )
console.log('\n')


console.log('2번')
const married = users.filter((user) => {
  return user.isMarried === true
})
console.log(married)
console.log('\n')


console.log('3번')
const tom = users.find((user) => {
  return user.name === 'Tom'
})
console.log(tom)
console.log('\n')


console.log('4번')
const newUsers = users.map(user => (
  {...user, isAlive: true}
))
console.log(newUsers)
console.log('\n')


console.log('5번')
const totalBalance = users.reduce((total, user) =>
  total + user.balance, 0)
console.log(totalBalance)
console.log('\n')