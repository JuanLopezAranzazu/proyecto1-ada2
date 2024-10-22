
def dynamic_programming(A, B, offers):
  n = len(offers)

  dp = [[float("-inf") for _ in range(A + 1)] for _ in range(n + 1)]
  assignments = [[-1 for _ in range(A + 1)] for _ in range(n + 1)]

  # Caso cuando el gobierno compra todas las acciones al precio B
  for a in range(A + 1):
    dp[n][a] = a * B
    assignments[n][a] = a

  # Llenar la matriz con la máxima ganancia
  for i in range(n - 1, -1, -1):
    price, min_qty, max_qty = offers[i]

    for a in range(A + 1):
      # Si no asignamos ninguna acción a este oferente, heredamos el valor anterior
      dp[i][a] = dp[i + 1][a]
      assignments[i][a] = 0

      # Consideramos todas las cantidades posibles entre min_qty y max_qty
      for qty in range(min_qty, max_qty + 1):
        
        if(a >= qty):  # Solo si tenemos suficientes acciones para asignar
          profit = dp[i + 1][a - qty] + price * qty

          if(profit > dp[i][a]):
            dp[i][a] = profit
            assignments[i][a] = qty

  # Máxima ganancia
  max_profit = dp[0][A]

  # Reconstruir las asignaciones
  X = [0] * n
  remaining = A

  for i in range(n):
    X[i] = assignments[i][remaining]
    remaining -= X[i]

  X.append(remaining)

  return max_profit, X
