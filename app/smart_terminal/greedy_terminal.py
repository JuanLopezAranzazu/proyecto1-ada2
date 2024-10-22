
def greedy(stringA, stringB, operations_dict):
  i,j = 0,0
  cost=0
  ops=[]

  while(i<len(stringA) and j<len(stringB)):
    cost_advance=float("inf")
    cost_replace=float("inf")

    # Caso cuando los caracteres son iguales
    if(stringA[i]==stringB[j]):
      cost_advance=operations_dict["advance"]
    else:
      cost_replace=operations_dict["replace"]

    cost_delete=operations_dict["delete"]
    cost_insert=operations_dict["insert"]

    # Seleccionar la operacion con menor costo
    costs=[cost_advance, cost_delete, cost_replace, cost_insert]
    min_cost=min(costs)
    min_cost_index=costs.index(min_cost)

    cost+=min_cost

    if(min_cost_index==0):
      ops.append("advance")
      i+=1
      j+=1
    elif(min_cost_index==1):
      ops.append("delete")
      i+=1
    elif(min_cost_index==2):
      ops.append(f"replace {stringB[j]}")
      i+=1
      j+=1
    elif(min_cost_index==3):
      ops.append(f"insert {stringB[j]}")
      j+=1
  
  # Caso en el que se recorren todas las letras de la cadena B
  if(i<len(stringA)):
    cost_delete=operations_dict["delete"]*(len(stringA)-i)
    ops_delete=["delete"]*(len(stringA)-i)
    cost_kill=operations_dict["kill"]
    ops_kill=["kill"]

    if(cost_delete<cost_kill):
      cost+=cost_delete
      ops+=ops_delete
    else:
      cost+=cost_kill
      ops+=ops_kill
  
  # Caso en el que se recorren todas las letras de la cadena A
  if(j<len(stringB)):
    cost_insert=operations_dict["insert"]*(len(stringB)-j)
    operations_insert=[f"insert {stringB[k]}" for k in range(j, len(stringB))]
    cost+=cost_insert
    ops+=operations_insert

  # Caso donde se usa kill y se insertan las letras restantes
  cost_kill = operations_dict["kill"] + operations_dict["insert"]*len(stringB)

  if(cost_kill<cost):
    cost=cost_kill
    ops=["kill"]+[f"insert {stringB[k]}" for k in range(len(stringB))]

  return cost, ops
