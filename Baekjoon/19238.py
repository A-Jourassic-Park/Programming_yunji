from collections import deque

#택시이동
def bfs(x,y,a,b):
    visited=[[0 for _ in range(n)] for _ in range(n)]
    board_dist=[[-1 for _ in range(n)] for _ in range(n)]
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    board_dist[x][y]=0
    while q:
        x,y=q.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<n and 0<=ny<n:
                if nx==a and ny==b:
                    return board_dist[x][y]+1
                if visited[nx][ny]==0 and board[nx][ny]!=1:
                    visited[nx][ny]=1
                    board_dist[nx][ny]=board_dist[x][y]+1
                    q.append((nx,ny))
    return -1

#최단거리
def bfs2(x,y):
    visited=[[0 for _ in range(n)] for _ in range(n)]
    board_dist=[[-1 for _ in range(n)] for _ in range(n)]
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    board_dist[x][y]=0

    while q:
        x,y=q.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and board[nx][ny]!=1:
                    visited[nx][ny]=1
                    board_dist[nx][ny]=board_dist[x][y]+1
                    q.append((nx,ny))
    return board_dist

#승객이랑 택시 거리 탐색
def search_dist():
    board_list=bfs2(tx,ty)
    for p in people:
        #계산한 적 있으면 갱신
        if len(p)==6:
            p[5]=board_list[p[1]][p[2]]
        #처음 계산이면 dist 추가
        else:
            p.append(board_list[p[1]][p[2]])
    return board_list

#택시->승객 출발 위치
def move_taxi_to_start():
    global f,tx,ty
    #연료 가능한지
    if f-people[0][5]<=0:
        return -1
    else:
        #연료 감소
        f-=people[0][5]
        #택시-> 출발 위치
        tx,ty=people[0][1],people[0][2]
        return 1
    
#택시->승객 도착 위치
def move_taxi_to_final():
    global f,tx,ty
    total_dist=bfs(tx,ty,people[0][3],people[0][4])
    if total_dist==-1 or f-total_dist<0:
        return -1
    else:
        #연료 계산
        f=f-total_dist+(total_dist*2)
        #택시-> 도착 위치
        tx,ty=people[0][3],people[0][4]
        return 1
   
dx=[1,-1,0,0]
dy=[0,0,-1,1]

#행렬, 승객 수, 연료
n,m,f=map(int,input().split())
board=[[] for _ in range(n)]
people=deque()

for i in range(0,n):
    board[i]=list(map(int,input().split()))

#택시 초기 위치 
tx,ty=map(int,input().split())
tx-=1
ty-=1

for i in range(m):
    #승객 출발 위치, 승객 도착 위치
    sx,sy,fx,fy=map(int,input().split())
    people.append([i+1,sx-1,sy-1,fx-1,fy-1])


cnt=0
# 승객이 존재하는 경우
while people:
    search_dist()
    #거리 오름차순 -> 행 번호 작은거 -> 열 번호 작은거
    people=list(people)
    people.sort(key=lambda x:(x[5],x[1],x[2]))
    people=deque(people)
    board2=bfs2(tx,ty)
    # 승객-택시 사이의 거리 확인
    if people[0][5]<0:
        cnt+=1
    else:
        if move_taxi_to_start()==-1:
            f=-1
            break
        if move_taxi_to_final()==-1:
            f=-1
            break
    people.popleft()

if cnt>=1:
    f=-1
print(f)