from collections import deque

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# BFS 메서드
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 출력 리스트
    result = []
    # 큐가 빌 때까지 반복(# c++의 while(!q.empty())와 같은 의미)
    while queue:
        v = queue.popleft()  # 큐에서 노드 꺼내기(# c++의 q.front()와 같은 의미)
        result.append(v)  # 결과 리스트에 노드 추가
        # 아직 방문하지 않은 인접 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    # 출력 형식 맞추기
    print(" -> ".join(map(str, result)))  # 리스트를 " -> "로 연결하여 출력

bfs(graph, 1, visited)
