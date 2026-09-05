WIDTH=12
HEIGHT=12
obstacles=[
  
    (2, 1), (2, 2), (2, 3),
    (5, 1), (5, 2), 
    (8, 1), (8, 2), (8, 3),

    
    (1, 5), (2, 5), (3, 5),
    (5, 4), (5, 5), (5, 6),
    (9, 4), (9, 5), (9, 6),


    (3, 8), (3, 9), (3, 10),
    (6, 8), (7, 8), (8, 8),
    (10, 9), (10, 10)
]
mud = [
    (3, 1), (4, 1),
    (6, 2), (7, 2),

    (3,11), (2,11),
    (6, 5), (7, 5), (8, 5),
  
    (5, 8), (10, 7), (9, 7),
    (5, 9), (8, 10), (9, 10)
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
import matplotlib.pyplot as plt

frontier = []
heapq.heappush(frontier, (0, start))

cost_so_far={}
cost_so_far[start]=0

came_from={}
came_from[start] = None

evaluated=[]

while frontier:
    current_cost, current=heapq.heappop(frontier)
   
    evaluated.append(current)

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

explored_not_chosen=[]

for node in evaluated:
    if node not in path:
        explored_not_chosen.append(node)

# print(explored_not_chosen)

fig, ax = plt.subplots()
ax.set_xlim(-0.5, WIDTH - 0.5)
ax.set_ylim(HEIGHT - 0.5, -0.5)

ax.set_xticks(range(WIDTH))
ax.set_yticks(range(HEIGHT))
ax.grid(True)

for x, y in obstacles:
    ax.scatter(x, y, marker='s', s=500, color='black')

for x, y in mud:
    ax.scatter(x, y, marker='s', s=500, color='lime')

for x, y in explored_not_chosen:
    ax.scatter(x, y, marker='s', s=500, color='lightcoral')

ax.scatter(start[0], start[1], marker='s', s=500)
ax.scatter(finish[0], finish[1], marker='s', s=500)

x_coords = [node[0] for node in path]
y_coords = [node[1] for node in path]

ax.plot(x_coords, y_coords, linewidth=3, color='blue')

plt.show()
