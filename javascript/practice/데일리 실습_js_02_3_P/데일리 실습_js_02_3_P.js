/* 
  1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
  2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
  3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
*/

// 1-1
const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}

function fileSummary({ name, extension, size }) {
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}
fileSummary(savedFile);

// 1-2
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

const username = data
const password = data
const email = data

// 2
function addNumbers(...numbers) {
  return numbers.reduce((sum, number) => { 
    return sum + number
  }, 0)
}

// 3-1
const defaultColors = ['red', 'green', 'blue'];
const favoriteColors = ['navy', 'black', 'gold', 'white']
const palette = defaultColors.concat(myFavoriteColors);

// 3-2
const info1 = { name: 'Tom', age: 30 }
const info2 = { isMarried: true, balance: 3000 }
const fullInfo = Object.assign(info1, info2)
