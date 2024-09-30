from collections import deque

# Clase nodo
class Node:
  def __init__(self, value, cost, parent, operation):
    self.value=value
    self.cost=cost
    self.parent=parent
    self.operation=operation

  def __repr__(self):
    return f"{self.operation}"
  
  def get_path(self):
    path=[]
    current=self
    while(current):
      path.insert(0,current)
      current=current.parent
    return path

def uniform_cost(stringA, stringB, operations_dict):
  root_node=Node((0,0), 0, None, None)
  queue=deque([root_node])
  visited=set()

  while(queue):
    current_node=queue.popleft()

    if(current_node.value in visited):
      continue

    visited.add(current_node.value)

    i,j=current_node.value

    # Si se encontró una solución
    if(i==len(stringA) and j==len(stringB)):
      return current_node.cost, current_node.get_path()

    # Operaciones
    if(i<len(stringA) and j<len(stringB)):
      if stringA[i]==stringB[j]:
        queue.append(Node((i+1,j+1), current_node.cost+operations_dict["advance"], current_node, "advance"))
      else:
        queue.append(Node((i+1,j+1), current_node.cost+operations_dict["replace"], current_node, f"replace {stringB[j]}"))

    if(i<len(stringA)):
      queue.append(Node((i+1,j), current_node.cost+operations_dict["delete"], current_node, "delete"))
    
    if(j<len(stringB)):
      queue.append(Node((i,j+1), current_node.cost+operations_dict["insert"], current_node, f"insert {stringB[j]}"))

    if(i<len(stringA) and j==len(stringB)):
      queue.append(Node((len(stringA),len(stringB)), current_node.cost+operations_dict["kill"], current_node, "kill"))

    # Ordenar la cola
    queue=deque(sorted(queue, key=lambda x: x.cost))

  # Si no se encontró una solución
  return 0, []
