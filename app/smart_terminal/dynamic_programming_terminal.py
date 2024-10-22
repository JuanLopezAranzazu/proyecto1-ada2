
def dynamic_programming(stringA, stringB, operations_dict):
  n = len(stringA)
  m = len(stringB)

  dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
  ops = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

  dp[n][m] = 0

  # Llenar la matriz con el minimo costo
  for i in range(n, -1, -1):
    for j in range(m, -1, -1):
      # Caso base cuando se recorren todas las letras de ambas cadenas
      if(i == n and j == m):
        continue

      # Caso cuando la cadena A es vacía
      if(i == n):
        dp[i][j] = operations_dict["insert"] * (m - j)

        for k in range(j, m):
          ops[i][j].append(f"insert {stringB[k]}")

        continue

      # Caso cuando la cadena B es vacía
      if(j == m):
        cost_delete = operations_dict["delete"] * (n - i)
        cost_kill = operations_dict["kill"]
        
        if(cost_kill < cost_delete):
          dp[i][j] = cost_kill
          ops[i][j] = ["kill"]
        else:
          dp[i][j] = cost_delete
          for k in range(i, n):
            ops[i][j].append("delete")
        
        continue

      # Operaciones
      cost_advance = float("inf")
      cost_replace = float("inf")

      # Caso en el que las letras son iguales
      if(stringA[i] == stringB[j]):
        cost_advance = dp[i + 1][j + 1] + operations_dict["advance"]
      else:
        cost_replace = dp[i + 1][j + 1] + operations_dict["replace"]

      cost_delete = dp[i + 1][j] + operations_dict["delete"]
      cost_insert = dp[i][j + 1] + operations_dict["insert"]

      # Costo de usar kill e insertar lo que queda de la cadena B
      cost_kill = operations_dict["kill"] + operations_dict["insert"] * (m - j)

      # Seleccionar la operacion con menor costo
      costs = [cost_advance, cost_delete, cost_replace, cost_insert, cost_kill]
      min_cost = min(costs)
      min_cost_index = costs.index(min_cost)

      if(min_cost_index == 0):
        dp[i][j] = cost_advance
        ops[i][j] = ops[i + 1][j + 1] + ["advance"]
      elif(min_cost_index == 1):
        dp[i][j] = cost_delete
        ops[i][j] = ops[i + 1][j] + ["delete"]
      elif(min_cost_index == 2):
        dp[i][j] = cost_replace
        ops[i][j] = ops[i + 1][j + 1] + [f"replace {stringB[j]}"]
      elif(min_cost_index == 3):
        dp[i][j] = cost_insert
        ops[i][j] = ops[i][j + 1] + [f"insert {stringB[j]}"]
      else:
        dp[i][j] = cost_kill
        ops[i][j] = ["kill"] + ["insert " + stringB[k] for k in range(j, m)]
  
  return dp[0][0], ops[0][0][::-1]
