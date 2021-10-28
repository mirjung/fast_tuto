def dfs(computers, idx, visited):
    visited[idx] = True
    for i, v in enumerate(computers[idx]):
        if v == 1 and idx < i+1:
            dfs(computers, i+1, visited)

def solution(n, computers):
    computers = [[]] + computers
    visited = [False] * (n + 1)
    answer = 0 
    for i in range(1, len(visited)):
        if not visited[i]:
            answer += 1
            dfs(computers, i, visited)
    return answer

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution(n, computers)
    print(result)
    
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    result = solution(n, computers)
    print(result)