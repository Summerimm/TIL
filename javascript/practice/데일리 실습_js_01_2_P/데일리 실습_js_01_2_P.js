words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

// 1. split(), reverse(), join()
function palindrome(word) {
    return word === word.split("").reverse().join("")
  }

// 2. for문 + string concatnation
function palindrome2(word) {
  let newString = ""
  for (let i = word.length - 1; i > -1; i--) {
    newString += word[i]
  }

  return word === newString
}

// 3. substring(), charAt()
function palindrome3(word) {
  if (word === "")
    return "";

  else
    return palindrome3(word.substring(1)) + word.charAt(0)

}

// 4. 조건부 삼항 연산자
function palindrome4(word) {
  return (word === '') ? '' : palindrome3(word.substring(1)) + word.charAt(0)
}

for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
