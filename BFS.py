# grid=[
#     ['.', '.', '.', '.', '.']
#     ['.', '#', '.', '.', '.']
#     ['.', '#', '.', '.', '.']
#     ['.', '#', '#', '#', '.']
#     ['.', '.', '.', '.', '.']
  
# ]
WIDTH=5
HEIGHT=5
obstacles=[
     (1,1), (1,2), (1,3), (2,3), (3,3)
]
def neighbours(node):
    x,y = node
    possible=[
        (x+1,y),
        (x,y+1),
        (x-1,y),
        (x,y-1)
    ]

    valid=[]
    for n in possible:
        nx,ny =n

        if 0<=nx<WIDTH and 0<=ny<HEIGHT:
                if n not in obstacles:
                 valid.append(n)

    return valid

start=(0,0)
finish=(4,4)

from collections import deque 
frontier=deque()
frontier.append(start)

came_from={}
came_from[start] = None

while frontier:
    current=frontier.popleft()

    for next_node in neighbours(current):
        if next_node not in came_from:
            frontier.append(next_node)
            came_from[next_node]=current

    if current==finish:
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()

        print(path)

    if current==finish:
        break
    

