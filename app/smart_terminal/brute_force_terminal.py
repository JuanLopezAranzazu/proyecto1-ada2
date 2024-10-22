
def brute_force(stringA, stringB, operations_dict, i=0, j=0):
  # Caso base cuando se recorren todas las letras de ambas cadenas
  if(i==len(stringA) and j==len(stringB)):
    return 0, []
  
  # Caso base cuando se recorren todas las letras de la cadena A
  if(i==len(stringA)):
    ops_insert=[]
    for k in range(j, len(stringB)):
      ops_insert.append(f"insert {stringB[k]}")
    return operations_dict["insert"] * (len(stringB) - j), ops_insert
  
  # Caso base cuando se recorren todas las letras de la cadena B
  if(j==len(stringB)):
    cost_delete = operations_dict["delete"] * (len(stringA) - i)
    ops_delete = ["delete"] * (len(stringA) - i)

    cost_kill = operations_dict["kill"]
    ops_kill = ["kill"]

    costs = [cost_delete, cost_kill]
    ops = [ops_delete, ops_kill]
    min_cost = min(costs)
    min_cost_index = costs.index(min_cost)

    return min_cost, ops[min_cost_index]

  # Operaciones
  cost_advance=float("inf")
  cost_replace=float("inf")
  ops_advance=[]
  ops_replace=[]

  # Caso en el que las letras son iguales
  if(stringA[i]==stringB[j]):
    cost_advance, ops_advance = brute_force(stringA, stringB, operations_dict, i+1, j+1)
    cost_advance+=operations_dict["advance"]
    ops_advance.insert(0,"advance")
  else:
    cost_replace, ops_replace = brute_force(stringA, stringB, operations_dict, i+1, j+1)
    cost_replace+=operations_dict["replace"]
    ops_replace.insert(0,f"replace {stringB[j]}")
  
  cost_delete, ops_delete = brute_force(stringA, stringB, operations_dict, i+1, j)
  cost_delete+=operations_dict["delete"]
  ops_delete.insert(0,"delete")

  cost_insert, ops_insert = brute_force(stringA, stringB, operations_dict, i, j+1)
  cost_insert+=operations_dict["insert"]
  ops_insert.insert(0,f"insert {stringB[j]}")

  costs=[cost_advance, cost_delete, cost_replace, cost_insert]
  ops=[ops_advance, ops_delete, ops_replace, ops_insert]
  min_cost=min(costs)
  min_cost_index=costs.index(min_cost)

  return min_cost, ops[min_cost_index]
