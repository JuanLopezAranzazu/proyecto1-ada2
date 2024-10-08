import unittest
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from subasta_publica import brute_force_auction, dynamic_programming_auction, greedy_auction

class TestAuction(unittest.TestCase):
  def test_brute_force(self):
    A = 1000
    B = 100
    offers = [[450, 100, 400], [400, 100, 400], [500, 400, 550]]

    max_profit, assignments = brute_force_auction.brute_force(A, B, offers)
    expected_max_profit = 472500
    expected_assignments = [350, 100, 550, 0]

    self.assertEqual(expected_max_profit, max_profit)
    self.assertEqual(expected_assignments, assignments)

  def test_dynamic_programming(self):
    A = 1000
    B = 100
    offers =  [[450, 100, 400], [400, 100, 400], [500, 400, 600], [200, 50, 200]]

    max_profit, assignments = dynamic_programming_auction.dynamic_programming(A, B, offers)
    expected_max_profit = 480000
    expected_assignments = [400, 0, 600, 0, 0]

    self.assertEqual(expected_max_profit, max_profit)
    self.assertEqual(expected_assignments, assignments)

  def test_greedy(self):
    A = 1000
    B = 100
    offers = [[500, 100, 600], [450, 400, 800]]

    max_profit, assignments = greedy_auction.greedy(A, B, offers)
    expected_max_profit = 480000
    expected_assignments = [600, 400, 0]

    self.assertEqual(expected_max_profit, max_profit)
    self.assertEqual(expected_assignments, assignments)

if __name__ == '__main__':
  unittest.main()
  