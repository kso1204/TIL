# N-Queen

# 문제 설명

1. 가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.

2. 예를 들어서 n이 4인경우 다음과 같이 퀸을 배치하면 n개의 퀸은 서로를 한번에 공격 할 수 없습니다.

3. 체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때,

4. n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.

# 제한 사항

```

퀸(Queen)은 가로, 세로, 대각선으로 이동할 수 있습니다.

n은 12이하의 자연수 입니다.

입출력 예

n	result

4	2

```

# 해결 방안

1. 백트래킹 문제.. 

2. 1번 위치에 놓았을 때 놓을 수 있는 2번 위치에 놓고.. 1, 2번 위치에 놓았을 때 3번 위치에 놓고.. 해서 n번까지 놓으면 카운트 + 1

3. n번까지 놓기전에 실패했으면 그 전으로 돌아가서 위치변경 <-- 백트래킹의 원리

4. 백트래킹의 원리를 알면 짤 수 있는가..?

# 풀이

1. https://st-lab.tistory.com/118

2. 백트래킹에 대해 알고 있는지..?

3. https://st-lab.tistory.com/118

4. 2차원 배열을 1차원 배열 형태로 표현하여 row, col에 값을 저장하고 이 값으로 row와 col의 차이를 둘 다 구한다.

5. https://idea-sketch.tistory.com/29

```

arr[1] = 1;

arr[3] = 3;

Math.abs(arr[1]-arr[3]) == Math.abs(1-3) <-- 대각선에 놓여져 있다.

arr[2] = 1;
arr[1] = 1;

arr[2] == arr[1] -> 같은 행에 놓여져있다.

arr[row] = col <- row는 col인 이 상황에 대해 이해를 하면 수월하고

조건에 맞는 경우에만 다음 스텝으로 가는 백트레킹에 

```

- 좋은 풀이



```

import java.util.*;

class Solution {
    
    int[] board;
    
    int answer = 0;
    
    int end;
    
    public int solution(int n) {
        
        board = new int[n];
        
        end = n;
        
        backTracking(0);
        
        return answer;
    }
    
    void backTracking(int depth)
    {
        if(depth==end) {
            answer++;
            return;
        }
        
        for(int i=0; i<end; i++) {
            board[depth] = i;
            
            if(check(depth)) {
                backTracking(depth+1);
            }
        }
    }
    
    boolean check(int col) {
        
        for (int i=0;i<col;i++) {
            
            if(board[col] == board[i] || Math.abs(col - i) == Math.abs(board[col] - board[i])) {
                return false;
            }
            
        }
        
        return true;
        
    }
}

```

- 리스트에 pair형태로 row, col을 저장해서 구한 백트래킹

```

import java.util.ArrayList;
import java.util.List;

class Cell {
    int r;
    int c;

    public Cell(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Solution {
    static List<Cell> cellList;
    static int casesCount;

    public int solution(int n) {
        cellList = new ArrayList<>();
        casesCount = 0;
        nQueen(0, n);
        return casesCount;
    }

    static void nQueen(int row, int n) {
        if (row == n) {
            casesCount++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (checkAvail(row, col)) {
                Cell cell = new Cell(row, col);
                cellList.add(cell);
                nQueen(row + 1, n);
                cellList.remove(cell);
            }
        }
    }

    static boolean checkAvail(int r, int c) {
        for (Cell cell : cellList) {
            if (r == cell.r || c == cell.c || cell.r + cell.c == r + c || cell.r - cell.c == r - c)
                return false;
        }
        return true;
    }
}


```




- 나의 처음 접근방법

```

class Solution {
    
    int[][] visited;
    
    int answer = 0;
    
    
    public int solution(int n) {
        
        
        visited = new int[n][n];
        
        
        for(int i=0;i<n;i++) {
            
            bfs(0,i,n);
        }
        
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                System.out.print(visited[i][j]);
            }
            System.out.println();
        }
        
        
        return answer;
    }
    
    void bfs(int x, int y, int N)
    {
        
        if(!visit(x,y,N)) return;
        
        if(x==N-1) {
            answer++;
            return;
        }
        
        for(int i=0;i<N;i++) {
            bfs(x+1,y+i,N);
        }
    }
    
    
    boolean visit(int x, int y, int N)
    {
        if(visited[x][y] == 1) {
            return false;
        }
        int nextX=0;
        int nextY=0;
        
        // - y 라인
        // | x 라인
        // / x 는 감소 플러스 y는 플러스
        // \ x 는 증가 y는 증가
        
        for(int i=0;i<N;i++) {
            
            nextX = (x+i)%N;
            nextY = (y+i)%N;
            
            visited[nextX][y] = 1;
            visited[x][nextY] = 1;
            visited[nextX][nextY] = 1;
            
        }
        
        for (int i=0;i<N;i++) {
            
            nextX = x-i;
            
            nextY = (y+i)%N;
            
            if(nextX<0) {
                nextX = N + nextX;
            }
            
            visited[nextX][nextY] = 1;
        }
        
        
        visited[x][y] = 2;
        
        return true;
        
    }
}

```