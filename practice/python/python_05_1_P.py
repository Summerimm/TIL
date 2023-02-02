# 문제
# 김코딩과 이싸피는 카드 게임을 하기로 했다. 아래와 같은 카드 list를 만들었을 때, 조건을 맞춰서 게임을 진행하고 승자를 출력하라.

# # trump_card_list
# [('spade', 'A'), ('spade', 2), ('spade', 3), ('spade', 4), ('spade', 5), ('spade', 6), ('spade', 7),
# ('spade', 8), ('spade', 9), ('spade', 10), ('spade', 'J'), ('spade', 'Q'), ('spade', 'K'),
# ('heart', 'A'), ('heart', 2), ('heart', 3), ('heart', 4), ('heart', 5), ('heart', 6), ('heart', 7),
# ('heart', 8), ('heart', 9), ('heart', 10), ('heart', 'J'), ('heart', 'Q'), ('heart', 'K'),
# ('diamond', 'A'), ('diamond', 2), ('diamond', 3), ('diamond', 4), ('diamond', 5), ('diamond', 6), ('diamond', 7),
# ('diamond', 8), ('diamond', 9), ('diamond', 10), ('diamond', 'J'), ('diamond', 'Q'), ('diamond', 'K'),
# ('clover', 'A'), ('clover', 2), ('clover', 3), ('clover', 4), ('clover', 5), ('clover', 6), ('clover', 7),
# ('clover', 8), ('clover', 9), ('clover', 10), ('clover', 'J'), ('clover', 'Q'), ('clover', 'K')]

# 카드를 먼저 무작위로 섞어야 한다.
# trump_card_list에서 한 장을 뽑아 player1에 할당하고, list에서 그 카드를 제외한 뒤 다시 한 장을 뽑아 player2에 할당한다.
# player 들의 카드를 비교하여 더 높은 가치의 카드를 가진 player가 승리한다.
# 높은 숫자일수록 더 높은 가치를 가진다.
# 알파벳은 숫자보다 가치가 높다.
# 알파벳은 A > K > Q > J 순으로 가치가 높다.
# 문양은 spade > diamond > heart > clover 순으로 가치가 높다.
# 동일한 숫자(or 알파벳)인 경우, 문양의 가치를 비교한다.
# 각각 선택된 카드와 승자를 출력하라.
# 승자를 결정한 뒤, 카드를 다시 섞어 한 사람이 6번 이길 때까지 게임을 반복한다. 제외한 카드는 다시 집어넣지 않는다.
# 최종 승자가 결정되면, 스코어와 최종 승자를 출력하라.
# Hint: random 모듈을 활용하라.


# 출력예시
# ('spade', 4) ('clover', 10) player2 win!
# ('clover', 7) ('heart', 4) player1 win!
# ('heart', 8) ('spade', 3) player1 win!
# ('heart', 5) ('diamond', 2) player1 win!
# ('heart', 2) ('heart', 'J') player2 win!
# ('clover', 6) ('clover', 'A') player2 win!
# ('heart', 'A') ('clover', 2) player1 win!
# ('heart', 10) ('diamond', 4) player1 win!
# ('spade', 2) ('diamond', 9) player2 win!
# ('clover', 'Q') ('diamond', 'Q') player2 win!
# ('heart', 9) ('diamond', 7) player1 win!
# 6:5 Finally player1 win

import random

def making_card_list() -> list:
	card_list = []
	for shape in ["spade", "heart", "diamond", "clover"]:
		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
			card_list.append((shape, number))

	return card_list

def alphatonum(x):
    if x == "J":
        x = 11
    elif x == "Q":
        x = 12
    elif x == "K":
        x = 13
    elif x == "A":
        x = 14
    else:
        x = x
    return x

def symbol(x):
    if x == "clover":
        x = 0
    elif x == "heart":
        x = 1
    elif x == "diamond":
        x = 2
    elif x == "spade":
        x = 3


trump_card_list = making_card_list()
wincount1, wincount2 = 0, 0

while(wincount1 < 6 and wincount2 < 6):
    player1 = random.choice(trump_card_list)
    player2 = random.choice(trump_card_list)
    trump_card_list.remove(player1)
    trump_card_list.remove(player2)

    num1 = alphatonum(player1[1])
    num2 = alphatonum(player2[1])

    if num1 > num2:
        print(f"{player1} {player2} player1 win!")
        wincount1 += 1
    elif num1 < num2:
        print(f"{player1} {player2} player2 win!")
        wincount2 += 1
    else:
        sym1 = symbol(player1[0])
        sym2 = symbol(player2[0])
        if sym1 > sym2:
            print(f"{player1} {player2} player1 win!")
            wincount1 += 1
        else:
            print(f"{player1} {player2} player2 win!")
            wincount2 += 1

if wincount1 == 6:
    winner = 'player1'
else:
    winner = 'player2'

print(f'{wincount1}:{wincount2} Finally {winner} win')