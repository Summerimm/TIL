
/* 
1. 게임개발자가 Monster class 를 작성중이다. 다음 명세에 따라 생성자(constructor) 함수를 작성하자.
Monster 는 생성될 때 health 가 100 이다.
constructor() 는 options 라는 object 를 받으며 name 이라는 key 를 가지고 있다. 생성되는 Monster에게 name 을 선언하자.

2. Monster class 가 생성되었다. 이번에는 Monster class를 상속받은 Snake class 를 생성해 보자.
  Snake 의 생성자는 Monster 와 똑같다. 추가되는 코드는 없으며, 마찬가지로 options 라는 이름의 object 를 받는다.
  Snake 는 bite() 라는 메서드를 갖는다. 필요한 인자는 다른 Snake 객체 뿐이다.
  bite() 를 통과한 다른 Snake 객체는 체력(health)이 10 깎인다.
*/

// 아래에 Monster 와 Snake class를 생성합니다.
class Monster {
  constructor(options) {
    this.name = options.name
    this.health = 100;
  }
}

class Snake extends Monster {
  constructor(options) {
    super(options)
  }

  bite(snake) {
    snake.health -= 10
  }
}


// 아래 코드는 확인용 입니다.
const conda = new Snake({ name: 'conda' })
const boa = new Snake({ name: 'boa' })

console.log(conda.health)  // 100
boa.bite(conda)
console.log(conda.health)  // 90

