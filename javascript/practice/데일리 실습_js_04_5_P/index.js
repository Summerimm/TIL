const sbutton = document.querySelector('#scissors-button')
const rbutton = document.querySelector('#rock-button')
const pbutton = document.querySelector('#paper-button')
const player1 = document.querySelector('#player1-img')
const player2 = document.querySelector('#player2-img')
let countp1 = document.querySelector('#p1count')
let countp2 = document.querySelector('#p2count')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')


function disable() {
  sbutton.disabled = true
  rbutton.disabled = true
  pbutton.disabled = true
}

function showModal(result) {
  modalContent.textContent = result
  modal.style.display = 'flex'

  setTimeout(() => {
    modal.style.display = 'none'
  }, 3000)
}

function randomChoice() {
  const choices = ['rock', 'paper', 'scissors']
  const randomIndex = Math.floor(Math.random() * 3)
  return choices[randomIndex]
}

function showResult() {
  // 0.1초 간격으로 컴퓨터의 선택이 바뀌도록 설정
  const intervalId = setInterval(function() {
    player2.setAttribute('src', './img/' + randomChoice() + '.png')
  }, 100)

  // 3초 후에 결과 모달 창을 표시하고, intervalId를 clearInterval하여 중지  
  setTimeout(() => {
    clearInterval(intervalId)
    let result
    const player2Weapon = randomChoice()
    player2.setAttribute('src', './img/' + player2Weapon + '.png')
    if (player1.getAttribute('src') === './img/scissors.png') {
      if (player2Weapon === 'rock') {
        result = 'Player2 wins!'
        countp2.textContent = parseInt(countp2.textContent) + 1
      } else if (player2Weapon === 'paper') {
        result = 'Player1 wins!'
        countp1.textContent = parseInt(countp1.textContent) + 1
      } else {
        result = 'Draw!'
      }
    } else if (player1.getAttribute('src') === './img/rock.png') {
      if (player2Weapon === 'paper') {
        result = 'Player2 wins!'
        countp2.textContent = parseInt(countp2.textContent) + 1
      } else if (player2Weapon === 'scissors') {
        result = 'Player1 wins!'
        countp1.textContent = parseInt(countp1.textContent) + 1
      } else {
        result = 'Draw!'
      }
    } else {
      if (player2Weapon === 'scissors') {
        result = 'Player2 wins!'
        countp2.textContent = parseInt(countp2.textContent) + 1
      } else if (player2Weapon === 'rock') {
        result = 'Player1 wins!'
        countp1.textContent = parseInt(countp1.textContent) + 1
      } else {
        result = 'Draw!'
      }
    }
    showModal(result)
    sbutton.disabled = false
    rbutton.disabled = false
    pbutton.disabled = false
  }, 3000)
}


sbutton.addEventListener('click', function() {
  player1.setAttribute('src', './img/scissors.png')
  disable()
  showResult()
})

rbutton.addEventListener('click', function() {
  player1.setAttribute('src', './img/rock.png')
  disable()
  showResult()
})

pbutton.addEventListener('click', function() {
  player1.setAttribute('src', './img/paper.png')
  disable()
  showResult()
})

