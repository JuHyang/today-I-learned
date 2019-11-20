visited = [0] * 200
def dfs (start, computers, n) :
    visited[start] = 1
    for i in range (n) :
        if visited[i] == 0 and computers[start][i] == 1 :
            dfs (i, computers, n)

def bfs (start, computers, n) :
    visited[start] = 1
    for i in range (n) :
        if visited[i] == 0 and computers[start][i] == 1 :
            bfs (i, computers, n)

def solution(n, computers):
    answer = 0
    for i in range (n) :
        if visited[i] == 0 :
            answer += 1
            dfs (i, computers, n)
        
    return answer