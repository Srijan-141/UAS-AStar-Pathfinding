# grid=[
#     ['.', '.', '+', '+', '.']         (The # represent the obstacles)
#     ['.', '#', '.', '+', '.']         (The + represent the mud squares which cost 5pts)
#     ['+', '#', '.', '.', '+']         (The rest of the squares are normal with travel cost of 1)
#     ['.', '#', '#', '#', '.']
#     ['.', '+', '.', '.', '.']

WIDTH=5
HEIGHT=5
obstacles=[
     (1,1), (1,2), (1,3), (2,3), (3,3)
]
mud = [
    (0,2), (1,4), (2,0), (3,0), (3,1), (4,2)
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

              heapq.heappush(frontier, (new_cost, next_node))

            #   print(new_cost)

  
path = []
current=finish
while current is not None:
    path.append(current)
    current = came_from[current]

path.reverse()
print(path)

   

    
