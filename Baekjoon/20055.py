from collections import deque

def rotate():
    a.rotate(1)
    robot.rotate(1)
    
def move():
    if robot.count(1)>0:
        #먼저 올라간 로봇부터 이동
        for i in range(n-2,-1,-1):
            #내리는 칸에 로봇은 바로 내리기
            if robot[n-1]==1:
                robot[n-1]=0
                
            #다음 칸에 로봇이 없는지 확인+ 내구도 >=1
            if robot[i]==1 and robot[i+1]==0 and a[i+1]>=1:
                robot[i+1]=1
                a[i+1]-=1
                robot[i]=0
            
def up_robot():   
    if a[0]>=1:
        robot[0]=1
        a[0]-=1  
        
def check_all():
    if a.count(0)>=k:
        return 1
    else:
        return 0      
    
n,k=map(int,input().split())
a=deque(map(int,input().split()))
robot=deque(0 for _ in range(n))
cnt=1

while True:
    rotate()
    move()
    up_robot()
    if check_all()==1:
        print(cnt)
        break
    cnt+=1