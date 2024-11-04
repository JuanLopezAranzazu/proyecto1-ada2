import matplotlib.pyplot as plt
import timeit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from smart_terminal import brute_force_terminal, dynamic_programming_terminal, greedy_terminal

output_dir = "data_outputs"

def graph_all_cases():
  os.makedirs(output_dir, exist_ok=True)

  # Casos de prueba
  test_cases = [
    {
      "stringA": "francesa",
      "stringB": "ancestro",
      "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
    },
    {
      "stringA": "ingeniero",
      "stringB": "ingenioso",
      "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
    },
    {
      "stringA": "algorithm",
      "stringB": "altruistic",
      "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
    },
    {
      "stringA": "programming",
      "stringB": "programmer",
      "operations_dict": {"advance": 8,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
    },
    {
      "stringA": "computer",
      "stringB": "computation",
      "operations_dict": {"advance": 1,"delete": 21,"replace": 3,"insert": 6,"kill": 1},
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
    stringA = test_case["stringA"]
    stringB = test_case["stringB"]
    operations_dict = test_case["operations_dict"]

    print(f'Caso de prueba: stringA={stringA}, stringB={stringB}, operations_dict={operations_dict}')

    print('Fuerza bruta')
    time = timeit.timeit(lambda: brute_force_terminal.brute_force(stringA, stringB, operations_dict), number=1)
    results['brute_force'].append(time)
    print(f'Tiempo de ejecución: {time}s')

    print('Programación dinámica')
    time = timeit.timeit(lambda: dynamic_programming_terminal.dynamic_programming(stringA, stringB, operations_dict), number=1)
    results['dynamic_programming'].append(time)
    print(f'Tiempo de ejecución: {time}s')

    print('Algoritmo voraz')
    time = timeit.timeit(lambda: greedy_terminal.greedy(stringA, stringB, operations_dict), number=1)
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
  plt.title('Comparación de algoritmos de la terminal inteligente')
  plt.legend()
  plt.grid(True)
  # Guardar gráfico
  plt.savefig(os.path.join(output_dir, "smart_terminal_all_cases.png"))
  plt.close()

def graph_single_case():
  os.makedirs(output_dir, exist_ok=True)

  # Caso de prueba
  test_case = {
    "stringA": "programming",
    "stringB": "programmer",
    "operations_dict": {"advance": 8,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
  }

  # Resultados de los algoritmos
  results = {
    'brute_force': 0,
    'dynamic_programming': 0,
    'greedy': 0,
  }

  # Ejecución de los algoritmos
  stringA = test_case["stringA"]
  stringB = test_case["stringB"]
  operations_dict = test_case["operations_dict"]

  print(f'Caso de prueba: stringA={stringA}, stringB={stringB}, operations_dict={operations_dict}')

  print('Fuerza bruta')
  time = timeit.timeit(lambda: brute_force_terminal.brute_force(stringA, stringB, operations_dict), number=1)
  results['brute_force'] = time
  print(f'Tiempo de ejecución: {time}s')

  print('Programación dinámica')
  time = timeit.timeit(lambda: dynamic_programming_terminal.dynamic_programming(stringA, stringB, operations_dict), number=1)
  results['dynamic_programming'] = time
  print(f'Tiempo de ejecución: {time}s')

  print('Algoritmo voraz')
  time = timeit.timeit(lambda: greedy_terminal.greedy(stringA, stringB, operations_dict), number=1)
  results['greedy'] = time
  print(f'Tiempo de ejecución: {time}s')

  plt.figure(figsize=(10, 5))
  plt.bar(results.keys(), results.values(), color=['blue', 'orange', 'green'])
  
  for i, v in enumerate(results.values()):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

  plt.xlabel('Algoritmos')
  plt.ylabel('Tiempo de ejecución (s)')
  plt.title('Comparación de algoritmos de la terminal inteligente')
  plt.yscale('log')
  # Guardar gráfico
  plt.savefig(os.path.join(output_dir, "smart_terminal_single_case.png"))
  plt.close()

# Tiempo promedio con N ejecuciones
def average_graph(N=50):
  os.makedirs(output_dir, exist_ok=True)

  # Caso de prueba
  test_case = {
    "stringA": "francesa",
    "stringB": "ancestro",
    "operations_dict": {"advance": 8,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
  }

  # Resultados de los algoritmos
  results = {
    'brute_force': 0,
    'dynamic_programming': 0,
    'greedy': 0,
  }

  # Ejecución de los algoritmos
  for i in range(N):
    stringA = test_case["stringA"]
    stringB = test_case["stringB"]
    operations_dict = test_case["operations_dict"]

    print(f'Caso de prueba: stringA={stringA}, stringB={stringB}, operations_dict={operations_dict}')

    print('Fuerza bruta')
    time = timeit.timeit(lambda: brute_force_terminal.brute_force(stringA, stringB, operations_dict), number=1)
    results['brute_force'] += time
    print(f'Tiempo de ejecución: {time}s')

    print('Programación dinámica')
    time = timeit.timeit(lambda: dynamic_programming_terminal.dynamic_programming(stringA, stringB, operations_dict), number=1)
    results['dynamic_programming'] += time
    print(f'Tiempo de ejecución: {time}s')

    print('Algoritmo voraz')
    time = timeit.timeit(lambda: greedy_terminal.greedy(stringA, stringB, operations_dict), number=1)
    results['greedy'] += time
    print(f'Tiempo de ejecución: {time}s')
  
  for algorithm in results.keys():
    results[algorithm] /= N

  plt.figure(figsize=(10, 5))
  plt.bar(results.keys(), results.values(), color=['blue', 'orange', 'green'])
  
  for i, v in enumerate(results.values()):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

  plt.xlabel('Algoritmos')
  plt.ylabel('Tiempo de ejecución (s)')
  plt.title(f'Promedio de tiempo algoritmos de la terminal inteligente (N={N})')
  plt.yscale('log')
  # Guardar gráfico
  plt.savefig(os.path.join(output_dir, "smart_terminal_average.png"))
  plt.close()

if __name__ == '__main__':
  graph_all_cases()
  graph_single_case()
  average_graph()