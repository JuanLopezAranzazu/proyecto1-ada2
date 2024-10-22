import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from public_auction import brute_force_auction, dynamic_programming_auction, greedy_auction

class TestAuction(unittest.TestCase):
  def test_brute_force(self):
    test_cases = [
      {
        "A": 1000,
        "B": 100,
        "offers": [[450, 100, 400], [400, 100, 400], [500, 400, 550]],
        "expected_max_profit": 472500,
        "expected_assignments": [350, 100, 550, 0]
      },
      {
        "A": 2000,
        "B": 100,
        "offers": [],
        "expected_max_profit": 200000,
        "expected_assignments": [2000]
      }
    ]
    
    for test_case in test_cases:
      A = test_case["A"]
      B = test_case["B"]
      offers = test_case["offers"]
      expected_max_profit = test_case["expected_max_profit"]
      expected_assignments = test_case["expected_assignments"]

      max_profit, assignments = brute_force_auction.brute_force(A, B, offers)

      self.assertEqual(expected_max_profit, max_profit)
      self.assertEqual(expected_assignments, assignments)

  def test_dynamic_programming(self):
    test_cases = [
      {
        "A": 1000,
        "B": 100,
        "offers": [[450, 100, 400], [400, 100, 400], [500, 400, 600], [200, 50, 200]],
        "expected_max_profit": 480000,
        "expected_assignments": [400, 0, 600, 0, 0]
      },
      {
        "A": 2000,
        "B": 100,
        "offers": [],
        "expected_max_profit": 200000,
        "expected_assignments": [2000]
      }
    ]
    
    for test_case in test_cases:
      A = test_case["A"]
      B = test_case["B"]
      offers = test_case["offers"]
      expected_max_profit = test_case["expected_max_profit"]
      expected_assignments = test_case["expected_assignments"]

      max_profit, assignments = dynamic_programming_auction.dynamic_programming(A, B, offers)

      self.assertEqual(expected_max_profit, max_profit)
      self.assertEqual(expected_assignments, assignments)

  def test_greedy(self):
    test_cases = [
      {
        "A": 1000,
        "B": 100,
        "offers": [[500, 100, 600], [450, 400, 800]],
        "expected_max_profit": 480000,
        "expected_assignments": [600, 400, 0]
      },
      {
        "A": 2000,
        "B": 100,
        "offers": [],
        "expected_max_profit": 200000,
        "expected_assignments": [2000]
      }
    ]
    
    for test_case in test_cases:
      A = test_case["A"]
      B = test_case["B"]
      offers = test_case["offers"]
      expected_max_profit = test_case["expected_max_profit"]
      expected_assignments = test_case["expected_assignments"]

      max_profit, assignments = greedy_auction.greedy(A, B, offers)

      self.assertEqual(expected_max_profit, max_profit)
      self.assertEqual(expected_assignments, assignments)

if __name__ == '__main__':
  unittest.main()
