import matplotlib.pyplot as plt
import timeit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from public_auction import brute_force_auction, dynamic_programming_auction, greedy_auction

def plot_time_complexity():
  test_cases = [
    {
      "A": 1000,
      "B": 100,
      "offers": [[450, 100, 400], [400, 100, 400], [500, 400, 550]],
    },
    {
      "A": 1000,
      "B": 100,
      "offers": [[150, 375, 385], [200, 250, 265], [300, 250, 345]],
    },
    {
      "A": 1000,
      "B": 100,
      "offers": [[500, 100, 600], [450, 400, 800]],
    },
  ]

  results = {
    'brute_force': [],
    'dynamic_programming': [],
    'greedy': [],
  }

  for test_case in test_cases:
    A = test_case["A"]
    B = test_case["B"]
    offers = test_case["offers"]

    print(f'Caso de prueba: A={A}, B={B}, offers={offers}')

    print('Fuerza bruta')
    time = timeit.timeit(lambda: brute_force_auction.brute_force(A, B, offers), number=1)
    results['brute_force'].append(time)
    print(f'Tiempo de ejecución: {time}s')

    print('Programación dinámica')
    time = timeit.timeit(lambda: dynamic_programming_auction.dynamic_programming(A, B, offers), number=1)
    results['dynamic_programming'].append(time)
    print(f'Tiempo de ejecución: {time}s')

    print('Algoritmo voraz')
    time = timeit.timeit(lambda: greedy_auction.greedy(A, B, offers), number=1)
    results['greedy'].append(time)
    print(f'Tiempo de ejecución: {time}s')

  plt.figure(figsize=(10, 5))
  for algorithm, times in results.items():
    plt.plot(times, marker='o', linestyle='-', label=algorithm)

  test_cases = ['Caso 1', 'Caso 2', 'Caso 3']
  plt.xticks(range(len(test_cases)), test_cases)

  plt.yscale('log')
  plt.xlabel('Casos de prueba')
  plt.ylabel('Tiempo de ejecución (s)')
  plt.title('Comparación de algoritmos de la subasta pública')
  plt.legend()
  plt.grid(True)
  plt.show()

if __name__ == '__main__':
  plot_time_complexity()