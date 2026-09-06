# [S  .  .  .  .  .  .  .  .  .  .  .]          (The # represent the obstacles)
# [.  .  #  .  .  #  .  .  #  .  .  .]          (The + represent the mud squares which cost 5pts)
# [.  .  #  M  M  #  .  M  #  .  .  .]          (The rest of the squares are normal with travel cost of 1)
# [.  .  .  M  .  #  M  M  .  .  .  .]
# [.  .  .  .  .  .  #  .  .  M  .  .]
# [.  #  #  #  M  .  #  .  M  M  .  .]
# [.  .  .  M  M  .  .  .  .  #  #  .]
# [.  .  .  M  .  .  M  M  .  .  .  .]
# [.  .  .  #  .  M  .  #  #  #  .  .]
# [.  .  .  #  .  M  .  .  .  M  .  .]
# [.  .  .  .  .  #  #  .  M  M  .  .]
# [.  .  .  .  .  .  .  .  .  .  .  G]

WIDTH=12
HEIGHT=12
obstacles=[
    (2,1), (5,1), (8,1),
    (2,2), (5,2), (8,2),
    (5,3), (6,4), (1,5), 
    (2,5), (3,5), (6,5),
    (9,6), (10,6), (3,8), 
    (7,8), (8,8), (9,8),
    (3,9), (5,10), (6,10)
]
mud = [
    (3,2), (4,2), (7,2),
    (3,3), (6,3), (7,3),
    (9,4), (4,5), (8,5),
    (9,5), (3,6), (4,6),
    (3,7), (6,7), (7,7),
    (5,8), (5,9), (9,9),
    (8,10), (9,10)
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

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start=(0,0)
finish=(11,11)

import heapq

frontier = []
heapq.heappush(frontier, (0, start))

cost_so_far={}
cost_so_far[start]=0

came_from={}
came_from[start] = None

while frontier:
    current_cost, current=heapq.heappop(frontier)
    if current==finish:
        break

    for next_node in neighbours(current):
         if next_node in mud:
             movement_cost=5
         else:
             movement_cost=1
         
         new_cost = cost_so_far[current] + movement_cost

         if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
              cost_so_far[next_node] = new_cost
              came_from[next_node] = current

              priority=new_cost + heuristic(next_node,finish)

              heapq.heappush(frontier, (priority, next_node))

            

  
path = []
current=finish
while current is not None:
    path.append(current)
    current = came_from[current]

path.reverse()
print(path)



