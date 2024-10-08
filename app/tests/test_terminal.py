import unittest
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from terminal_inteligente import brute_force_terminal, dynamic_programming_terminal, greedy_terminal, uniform_cost_terminal

class TestTerminal(unittest.TestCase):
  def test_brute_force(self):
    stringA = "francesa"
    stringB = "ancestro"
    operations_dict = {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1}
    min_cost, operations = brute_force_terminal.brute_force(stringA, stringB, operations_dict)
    expected_min_cost = 16

    self.assertEqual(expected_min_cost, min_cost)

  def test_dynamic_programming(self):
    stringA = "terminal"
    stringB = "inteligente"
    operations_dict = {"advance": 1,"delete": 2,"replace": 4,"insert": 5,"kill": 3}
    min_cost, operations = dynamic_programming_terminal.dynamic_programming(stringA, stringB, operations_dict)
    expected_min_cost = 38

    self.assertEqual(expected_min_cost, min_cost)

  def test_greedy(self):
    stringA = "algorithm"
    stringB = "altruistic"
    operations_dict = {"advance": 1,"delete": 2,"replace": 3,"insert": 2,"kill": 1}
    min_cost, operations = greedy_terminal.greedy(stringA, stringB, operations_dict)
    expected_min_cost = 29

    self.assertEqual(expected_min_cost, min_cost)

if __name__ == '__main__':
  unittest.main()
