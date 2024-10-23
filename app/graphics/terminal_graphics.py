import matplotlib.pyplot as plt
import timeit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from smart_terminal import brute_force_terminal, dynamic_programming_terminal, greedy_terminal

def plot_time_complexity():
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

  results = {
    'brute_force': [],
    'dynamic_programming': [],
    'greedy': [],
  }

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
  plt.show()

def plot_single_case():
  test_case = {
    "stringA": "programming",
    "stringB": "programmer",
    "operations_dict": {"advance": 8,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
  }

  results = {
    'brute_force': 0,
    'dynamic_programming': 0,
    'greedy': 0,
  }

  print(f'Caso de prueba: stringA={test_case["stringA"]}, stringB={test_case["stringB"]}, operations_dict={test_case["operations_dict"]}')

  stringA = test_case["stringA"]
  stringB = test_case["stringB"]
  operations_dict = test_case["operations_dict"]

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
  plt.show()

if __name__ == '__main__':
  plot_time_complexity()
  plot_single_case()
