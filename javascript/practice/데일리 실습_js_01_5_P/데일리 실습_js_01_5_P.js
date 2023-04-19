const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// 3
// 100
// 62

function findkakdugi(people) {
  let count = {}
  for (let i = 0; i < people.length; i++) {
    if (count[people[i]]) {
      count[people[i]]++
    } else {
      count[people[i]] = 1
    }
  }
  for (let number in count) {
    if (count[number] === 1) {
      return number
    }
  }
}

for (people of participantNums) {
  console.log(findkakdugi(people))
}