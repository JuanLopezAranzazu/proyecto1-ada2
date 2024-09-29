
def dynamic_programming(stringA, stringB, operations_dict):
  n = len(stringA)
  m = len(stringB)

  dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
  ops = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

  # Caso en que la cadena B es vacía
  for i in range(1, n + 1):
    dp[i][0]=dp[i-1][0]+operations_dict["delete"]
    ops[i][0]=ops[i-1][0]+["delete"]
  
  # Caso en que la cadena A es vacía
  for j in range(1,m+1):
    dp[0][j]=operations_dict["insert"]*j
    for k in range(j):
      ops[0][j].append(f"insert {stringB[k]}")

  # Llenar la matriz con el minimo costo
  for i in range(1, n+1):
    for j in range(1, m+1):
      cost_advance=float("inf")
      cost_replace=float("inf")

      if(stringA[i-1]==stringB[j-1]):
        cost_advance=dp[i-1][j-1]+operations_dict["advance"]
      else:
        cost_replace=dp[i-1][j-1]+operations_dict["replace"]

      cost_delete=dp[i-1][j]+operations_dict["delete"]
      cost_insert=dp[i][j-1]+operations_dict["insert"]

      cost_kill=float("inf")

      # Caso cuando hay caracteres en la cadena A que no están en la cadena B
      if(i>0 and j==m):
        cost_kill=dp[i-1][j]+operations_dict["kill"]

      # Seleccionar la operacion con menor costo
      costs=[cost_advance,cost_replace,cost_delete,cost_insert,cost_kill]
      min_cost=min(costs)
      min_cost_index=costs.index(min_cost)

      if(min_cost_index==0):
        dp[i][j]=cost_advance
        ops[i][j]=ops[i-1][j-1]+["advance"]
      elif(min_cost_index==1):
        dp[i][j]=cost_replace
        ops[i][j]=ops[i-1][j-1]+[f"replace {stringB[j-1]}"]
      elif(min_cost_index==2):
        dp[i][j]=cost_delete
        ops[i][j]=ops[i-1][j]+["delete"]
      elif(min_cost_index==3):
        dp[i][j]=cost_insert
        ops[i][j]=ops[i][j-1]+[f"insert {stringB[j-1]}"]
      else:
        dp[i][j]=cost_kill
        ops[i][j]=ops[i-1][j]+["kill"]

        return dp[i][j], ops[i][j]
      
  return dp[n][m], ops[n][m]

