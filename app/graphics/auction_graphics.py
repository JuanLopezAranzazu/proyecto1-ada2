import matplotlib.pyplot as plt
import timeit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from public_auction import brute_force_auction, dynamic_programming_auction, greedy_auction

output_dir = "data_outputs"

def graph_all_cases():
  os.makedirs(output_dir, exist_ok=True)

  # Casos de prueba
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
    {
      "A": 2000,
      "B": 150,
      "offers": [[500, 100, 600], [450, 400, 800], [600, 500, 1000]],
    },
    {
      "A": 2000,
      "B": 100,
      "offers": [[450, 100, 300], [400, 280, 412], [500, 550, 618]],
    }
  ]

  # Resultados de los algoritmos
  results = {
    'brute_force': [],
    'dynamic_programming': [],
    'greedy': [],
  }

  # Ejecución de los algoritmos
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

  test_cases = [f'Caso {i + 1}' for i in range(len(test_cases))]
  plt.xticks(range(len(test_cases)), test_cases)

  plt.yscale('log')
  plt.xlabel('Casos de prueba')
  plt.ylabel('Tiempo de ejecución (s)')
  plt.title('Comparación de algoritmos de la subasta pública')
  plt.legend()
  plt.grid(True)
  # Guardar gráfico
  plt.savefig(os.path.join(output_dir, "public_auction_all_cases.png"))
  plt.close()

def graph_single_case():
  os.makedirs(output_dir, exist_ok=True)

  # Caso de prueba
  test_case = {
    "A": 1000,
    "B": 100,
    "offers": [[450, 100, 400], [400, 100, 400], [500, 400, 550]],
  }

  # Resultados de los algoritmos
  results = {
    'brute_force': 0,
    'dynamic_programming': 0,
    'greedy': 0,
  }

  # Ejecución de los algoritmos
  A = test_case["A"]
  B = test_case["B"]
  offers = test_case["offers"]

  print(f'Caso de prueba: A={A}, B={B}, offers={offers}')

  print('Fuerza bruta')
  time = timeit.timeit(lambda: brute_force_auction.brute_force(A, B, offers), number=1)
  results['brute_force'] = time
  print(f'Tiempo de ejecución: {time}s')

  print('Programación dinámica')
  time = timeit.timeit(lambda: dynamic_programming_auction.dynamic_programming(A, B, offers), number=1)
  results['dynamic_programming'] = time
  print(f'Tiempo de ejecución: {time}s')

  print('Algoritmo voraz')
  time = timeit.timeit(lambda: greedy_auction.greedy(A, B, offers), number=1)
  results['greedy'] = time
  print(f'Tiempo de ejecución: {time}s')

  plt.figure(figsize=(10, 5))
  plt.bar(results.keys(), results.values(), color=['blue', 'orange', 'green'])
  
  for i, v in enumerate(results.values()):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

  plt.xlabel('Algoritmos')
  plt.ylabel('Tiempo de ejecución (s)')
  plt.title('Comparación de algoritmos de la subasta pública')
  plt.yscale('log')
  # Guardar gráfico
  plt.savefig(os.path.join(output_dir, "public_auction_single_case.png"))
  plt.close()

if __name__ == '__main__':
  graph_all_cases()
  graph_single_case()
