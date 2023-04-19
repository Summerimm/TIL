const n = 5
let stars = ''

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n - i - 1; j++) {
    stars += ' '
  }

  for (let j = 0; j < 2 * i + 1; j++) {
    stars += '*'
  }

  for (let j = 0; j < n - i - 1; j++) {
    stars += ' '
  }
  stars += '\n'
}

console.log(stars);

// 4/1/4
// 3/3/3
// 2/5/2
// 1/7/1
// 0/9/0