#!/usr/bin/env python3

import random

class DiceRoller:
	@staticmethod
	def rollDice(qty: int, sides: int, sort: bool = False, detailed: bool = False) -> tuple[str, list, int, float]:
		if qty < 1 or sides < 1:
			raise ValueError("You must have at least one (1) die with at least one (1) side.")
		result = []
		if sides == 100:
			for _ in range(qty):
				die1 = random.randint(0, 9) * 10
				die2 = random.randint(0, 9)
				dieTotal = 100 if die1 == 0 and die2 == 0 else die1 + die2
				if detailed:
					result.append([dieTotal, [die1, die2]])
				else:
					result.append(dieTotal)
		else:
			result = [random.randint(1, sides) for _ in range(qty)]
		if sort and not detailed:
			result.sort(reverse=True)
		total = sum(roll if isinstance(roll, int) else roll[0] for roll in result)
		avg = total / qty if qty > 0 else 0
		return f"d{sides}", result, total, avg
	
	@staticmethod
	def rollD4(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 4, sort)
	
	@staticmethod
	def rollD6(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 6, sort)
	
	@staticmethod
	def rollD8(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 8, sort)
	
	@staticmethod
	def rollD10(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 10, sort)
	
	@staticmethod
	def rollD12(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 12, sort)
	
	@staticmethod
	def rollD20(qty: int, sort: bool = False) -> tuple[str, list[int], int, float]:
		return DiceRoller.rollDice(qty, 20, sort)
	
	@staticmethod
	def printRolltoConsole(rollResults):
		if isinstance(rollResults, str):
			print(rollResults)
			return
		die_type, result, total, avg = rollResults
		print(f"Result of {len(result)} {die_type}:")
		for each, roll in enumerate(result, 1):
			if isinstance(roll, list):  # Detailed d100 rolls
				print(f"• Roll {each}: {roll[0]} ({roll[1][0]}, {roll[1][1]})")
			else:
				print(f"• Roll {each}: {roll}")
		print("---------------")
		print(f"Total: {total}")
		print(f"Average: {avg}\n")
	
class StatCalculators:

	@staticmethod
	def getModifier(score: int):
		return (score - 10) // 2
	
	@staticmethod
	def rollForStats(rollResults, printToConsole: bool = True):
		die_type, result, total, avg = rollResults
		if len(result) != 4:
			raise ValueError("Expected 4 roll values for stat calculation.")
		sorted_result = sorted(result, reverse=True)
		score = sum(sorted_result[:3])
		if printToConsole:
			print(f"Base Result: {result[0]}, {result[1]}, {result[2]}, {result[3]}")
			print(f"Sorted Result: {sorted_result[0]}, {sorted_result[1]}, {sorted_result[2]}, {sorted_result[3]}")
			print(f"Dropped Value: {sorted_result[3]}")
			print(f"Score Result: {score}")
		return score