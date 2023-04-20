function findQueens(n) {
  let answer = 0;
  const col = Array(n).fill(false); // 각 열의 사용 여부를 저장하는 배열
  const leftDiagonal = Array(2 * n - 1).fill(false); // 왼쪽 대각선 사용 여부를 저장하는 배열
  const rightDiagonal = Array(2 * n - 1).fill(false); // 오른쪽 대각선 사용 여부를 저장하는 배열

  // row: 현재 탐색 중인 행, count: 현재까지 놓인 퀸의 수
  function backtrack(row, count) {
    if (row === n) { // 모든 행에 퀸을 놓은 경우
      answer++;
      return;
    }

    for (let i = 0; i < n; i++) {
      // 현재 열과 대각선 방향으로 공격할 수 있는 열이 아니면
      if (!col[i] && !leftDiagonal[row + i] && !rightDiagonal[row - i + n - 1]) {
        col[i] = leftDiagonal[row + i] = rightDiagonal[row - i + n - 1] = true; // 해당 열과 대각선 방향을 사용 중으로 변경
        backtrack(row + 1, count + 1);
        col[i] = leftDiagonal[row + i] = rightDiagonal[row - i + n - 1] = false; // 다시 사용하지 않는 상태로 변경
      }
    }
  }

  backtrack(0, 0);
  return answer;
}

console.log(findQueens(4)); // 2
