from collections import deque

dir=0 #0:동, 1:서, 2:남, 3:북
dice=[1,2,4,5,3,6]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
result=0
x=0
y=0

def move(dir):
    if dir==0:
        dice[0],dice[2],dice[4],dice[5]=dice[2],dice[5],dice[0],dice[4]
    elif dir==1:
        dice[0],dice[2],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[2]
    elif dir==2:
        dice[0],dice[1],dice[3],dice[5]=dice[1],dice[5],dice[0],dice[3]
    elif dir==3:
        dice[0],dice[1],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[1]

def change_opposite_dir(dir):
    if dir==0 or dir==2:
        dir+=1
    else:
        dir-=1
    return dir

#시계 방향
def change_left_dir(dir):
    if dir==0:
        dir=2
    elif dir==2:
        dir=1
    elif dir==1:
        dir=3
    else:
        dir=0
    return dir

#시계 반대 방향
def change_right_dir(dir):
    if dir==0:
        dir=3
    elif dir==2:
        dir=0
    elif dir==1:
        dir=2
    else:
        dir=1
    return dir

def a_vs_b(a,b,dir):
    if a>b:
        dir=change_left_dir(dir)
    elif a<b:
        dir=change_right_dir(dir)
    return dir 

def bfs(b,x,y):
    cnt=1
    visited=[[0 for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and board[nx][ny]==b:
                    visited[nx][ny]=1
                    cnt+=1
                    q.append((nx,ny))
    return cnt
                
n,m,k=map(int,input().split())
board=[[]for _ in range(n)]

for i in range(n):
    board[i]=list(map(int,input().split()))


for i in range(k):
    score,b,c=0,0,0
    while True:
        nx=x+dx[dir]
        ny=y+dy[dir]
        if 0<=nx<n and 0<=ny<m:
            chk=1
            x,y=nx,ny
            break
        else:
            dir=change_opposite_dir(dir)
    move(dir)
    b=board[x][y]
    dir=a_vs_b(dice[5],b,dir)
    c=bfs(b,x,y)
    score=b*c
    result+=score
          
print(result)
        