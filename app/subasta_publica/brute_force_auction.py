
# Función que calcula la ganancia total de un conjunto de acciones asignadas
def calculate_profit(offers, current_assignment):
  profit=0
  for i in range(len(offers)):
    profit += current_assignment[i]*offers[i][0]
  return profit


def brute_force(A, B, offers, i=0, current_assignment=[]):

  # Caso cuando ya no hay más ofertas
  if(i == len(offers)):
    profit = calculate_profit(offers, current_assignment)
    if(A==0):
      return profit, current_assignment+[0]
    else:
      # Las acciones restantes se venden al precio B
      profit += A*B
      return profit, current_assignment+[A]
  
  # Acciones mínimas y máximas de la oferta actual
  min_qty=offers[i][1]
  max_qty=offers[i][2]

  best_profit=float("-inf")
  best_assignment=[]

  for qty in range(0, max_qty+1):
    if(qty == 0 or qty >= min_qty):

      if(A>=qty):

        profit, assignment = brute_force(A-qty, B, offers, i+1, current_assignment + [qty])

        if(profit > best_profit):
          best_profit = profit
          best_assignment = assignment

  return best_profit, best_assignment
