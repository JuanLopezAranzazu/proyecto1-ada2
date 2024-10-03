
def greedy(A, B, offers):
  best_profit=0
  best_assignment=[0]*(len(offers)+1)

  # Indice a cada oferta
  offers = [(i, *offer) for i, offer in enumerate(offers)]
    
  # Ordenar ofertas por precio de forma descendente
  offers = sorted(offers, key=lambda x: -x[1])

  for i, price, min_qty, max_qty in offers:
    for qty in range(max_qty, min_qty-1, -1):
      if(A>=qty):
        A-=qty
        best_profit += qty*price
        best_assignment[i]=qty
        break

  best_assignment[-1]=A
  best_profit += A*B

  return best_profit, best_assignment

