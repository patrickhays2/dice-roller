#!/usr/bin/env python3

import unittest
import io
from contextlib import redirect_stdout
from dice_roller import DiceRoller, StatCalculators  # Replace with actual module name

class TestDiceRoller(unittest.TestCase):
	
	def test_rollDice_basic(self):
		"""Test rolling a single die."""
		die_type, rolls, total, avg = DiceRoller.rollDice(1, 6)
		self.assertEqual(die_type, "d6")
		self.assertEqual(len(rolls), 1)
		self.assertTrue(1 <= rolls[0] <= 6)
		self.assertEqual(total, rolls[0])
		self.assertEqual(avg, rolls[0])
		
	def test_rollDice_multiple(self):
		"""Test rolling multiple dice."""
		die_type, rolls, total, avg = DiceRoller.rollDice(3, 6)
		self.assertEqual(die_type, "d6")
		self.assertEqual(len(rolls), 3)
		self.assertTrue(all(1 <= roll <= 6 for roll in rolls))
		self.assertEqual(total, sum(rolls))
		self.assertAlmostEqual(avg, total / 3)
		
	def test_rollDice_sort(self):
		"""Test rolling dice with sorting enabled."""
		die_type, rolls, total, avg = DiceRoller.rollDice(4, 6, sort=True)
		self.assertEqual(die_type, "d6")
		self.assertEqual(len(rolls), 4)
		self.assertEqual(rolls, sorted(rolls, reverse=True))
		self.assertTrue(all(1 <= roll <= 6 for roll in rolls))
		
	def test_rollDice_d100_detailed(self):
		"""Test rolling d100 with detailed output."""
		die_type, rolls, total, avg = DiceRoller.rollDice(1, 100, detailed=True)
		self.assertEqual(die_type, "d100")
		self.assertEqual(len(rolls), 1)
		self.assertIsInstance(rolls[0], list)
		self.assertEqual(len(rolls[0]), 2)  # [total, [die1, die2]]
		self.assertTrue(0 <= rolls[0][1][0] <= 90 and 0 <= rolls[0][1][1] <= 9)
		expected_total = 100 if rolls[0][1] == [0, 0] else rolls[0][1][0] + rolls[0][1][1]
		self.assertEqual(rolls[0][0], expected_total)
		self.assertEqual(total, rolls[0][0])
		
	def test_rollDice_d100_not_detailed(self):
		"""Test rolling d100 without detailed output."""
		die_type, rolls, total, avg = DiceRoller.rollDice(2, 100)
		self.assertEqual(die_type, "d100")
		self.assertEqual(len(rolls), 2)
		self.assertTrue(all(isinstance(roll, int) and 0 <= roll <= 100 for roll in rolls))
		self.assertEqual(total, sum(rolls))
		
	def test_rollDice_invalid_input(self):
		"""Test rolling dice with invalid inputs."""
		with self.assertRaises(ValueError):
			DiceRoller.rollDice(0, 6)
		with self.assertRaises(ValueError):
			DiceRoller.rollDice(1, 0)
			
	def test_specific_die_methods(self):
		"""Test specific die methods like rollD4, rollD6, etc."""
		die_type, rolls, total, avg = DiceRoller.rollD4(2)
		self.assertEqual(die_type, "d4")
		self.assertEqual(len(rolls), 2)
		self.assertTrue(all(1 <= roll <= 4 for roll in rolls))
		
		die_type, rolls, total, avg = DiceRoller.rollD20(1)
		self.assertEqual(die_type, "d20")
		self.assertEqual(len(rolls), 1)
		self.assertTrue(1 <= rolls[0] <= 20)
		
	def test_printRolltoConsole_standard(self):
		"""Test printing standard dice rolls to console."""
		roll_results = DiceRoller.rollDice(2, 6)
		with redirect_stdout(io.StringIO()) as f:
			DiceRoller.printRolltoConsole(roll_results)
		output = f.getvalue().strip()
		self.assertIn("Result of 2 d6:", output)
		self.assertIn("Total:", output)
		self.assertIn("Average:", output)
		self.assertTrue(any(f"Roll {i}: {roll}" in output for i, roll in enumerate(roll_results[1], 1)))
		
	def test_printRolltoConsole_d100_detailed(self):
		"""Test printing detailed d100 rolls to console."""
		roll_results = DiceRoller.rollDice(1, 100, detailed=True)
		with redirect_stdout(io.StringIO()) as f:
			DiceRoller.printRolltoConsole(roll_results)
		output = f.getvalue().strip()
		self.assertIn("Result of 1 d100:", output)
		roll = roll_results[1][0]
		expected_roll_str = f"Roll 1: {roll[0]} ({roll[1][0]}, {roll[1][1]})"
		self.assertIn(expected_roll_str, output)
		self.assertIn(f"Total: {roll[0]}", output)
		
	def test_printRolltoConsole_error_message(self):
		"""Test printing an error message to console."""
		with redirect_stdout(io.StringIO()) as f:
			DiceRoller.printRolltoConsole("Invalid input")
		output = f.getvalue().strip()
		self.assertEqual(output, "Invalid input")
		
class TestStatCalculators(unittest.TestCase):
	
	def test_getModifier(self):
		"""Test ability score modifier calculation."""
		test_cases = [
			(2, -4), (3, -4), (4, -3), (5, -3),
			(6, -2), (7, -2), (8, -1), (9, -1), (10, 0),
			(11, 0), (12, 1), (13, 1), (14, 2), (15, 2),
			(16, 3), (17, 3), (18, 4)
		]
		for score, expected in test_cases:
			with self.subTest(score=score):
				self.assertEqual(StatCalculators.getModifier(score), expected)
				
	def test_rollForStats_valid(self):
		"""Test rolling for stats with valid input."""
		roll_results = DiceRoller.rollDice(4, 6, sort=True)
		stat = StatCalculators.rollForStats(roll_results, printToConsole=False)
		sorted_rolls = sorted(roll_results[1], reverse=True)
		expected_stat = sum(sorted_rolls[:3])
		self.assertEqual(stat, expected_stat)
		self.assertTrue(3 <= stat <= 18)
		
	def test_rollForStats_invalid(self):
		"""Test rolling for stats with invalid input."""
		roll_results = DiceRoller.rollDice(3, 6)  # Only 3 rolls instead of 4
		with self.assertRaises(ValueError):
			StatCalculators.rollForStats(roll_results, printToConsole=False)
			
	def test_rollForStats_print(self):
		"""Test rolling for stats with console output."""
		roll_results = DiceRoller.rollDice(4, 6, sort=True)
		with redirect_stdout(io.StringIO()) as f:
			stat = StatCalculators.rollForStats(roll_results, printToConsole=True)
		output = f.getvalue().strip()
		rolls = roll_results[1]
		sorted_rolls = sorted(rolls, reverse=True)
		self.assertIn(f"Base Result: {rolls[0]}, {rolls[1]}, {rolls[2]}, {rolls[3]}", output)
		self.assertIn(f"Sorted Result: {sorted_rolls[0]}, {sorted_rolls[1]}, {sorted_rolls[2]}, {sorted_rolls[3]}", output)
		self.assertIn(f"Dropped Value: {sorted_rolls[3]}", output)
		self.assertIn(f"Score Result: {stat}", output)
		
if __name__ == "__main__":
	unittest.main()