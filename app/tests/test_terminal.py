import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from smart_terminal import brute_force_terminal, dynamic_programming_terminal, greedy_terminal, uniform_cost_terminal

class TestTerminal(unittest.TestCase):
  def test_brute_force(self):
    test_cases = [
      {
        "stringA": "francesa",
        "stringB": "ancestro",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 16
      },
      {
        "stringA": "francesa",
        "stringB": "",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 1
      },
      {
        "stringA": "",
        "stringB": "ancestro",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 16
      },
      {
        "stringA": "ingeniero",
        "stringB": "ingenieso",
        "operations_dict": {"advance": 11,"delete": 7,"replace": 4,"insert": 5,"kill": 3},
        "expected_min_cost": 40
      }
    ]

    for test_case in test_cases:
      stringA = test_case["stringA"]
      stringB = test_case["stringB"]
      operations_dict = test_case["operations_dict"]
      expected_min_cost = test_case["expected_min_cost"]

      min_cost, _ = brute_force_terminal.brute_force(stringA, stringB, operations_dict)

      self.assertEqual(expected_min_cost, min_cost)

  def test_dynamic_programming(self):
    test_cases = [
      {
        "stringA": "terminal",
        "stringB": "inteligente",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 4,"insert": 5,"kill": 3},
        "expected_min_cost": 38
      },
      {
        "stringA": "terminal",
        "stringB": "",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 4,"insert": 5,"kill": 3},
        "expected_min_cost": 3
      },
      {
        "stringA": "",
        "stringB": "inteligente",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 4,"insert": 5,"kill": 3},
        "expected_min_cost": 55
      },
      {
        "stringA": "ingeniero",
        "stringB": "ingenieso",
        "operations_dict": {"advance": 11,"delete": 7,"replace": 4,"insert": 5,"kill": 3},
        "expected_min_cost": 40
      }
    ]
    
    for test_case in test_cases:
      stringA = test_case["stringA"]
      stringB = test_case["stringB"]
      operations_dict = test_case["operations_dict"]
      expected_min_cost = test_case["expected_min_cost"]

      min_cost, _ = dynamic_programming_terminal.dynamic_programming(stringA, stringB, operations_dict)

      self.assertEqual(expected_min_cost, min_cost)

  def test_greedy(self):
    test_cases = [
      {
        "stringA": "algorithm",
        "stringB": "altruistic",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 21
      },
      {
        "stringA": "algorithm",
        "stringB": "",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 1
      },
      {
        "stringA": "",
        "stringB": "altruistic",
        "operations_dict": {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1},
        "expected_min_cost": 20
      }
    ]
    
    for test_case in test_cases:
      stringA = test_case["stringA"]
      stringB = test_case["stringB"]
      operations_dict = test_case["operations_dict"]
      expected_min_cost = test_case["expected_min_cost"]

      min_cost, _ = greedy_terminal.greedy(stringA, stringB, operations_dict)

      self.assertEqual(expected_min_cost, min_cost)

if __name__ == '__main__':
  unittest.main()
