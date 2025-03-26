# DiceRoller

DiceRoller is a Python library designed for rolling dice in tabletop role-playing games like Dungeons & Dragons (D&D). It offers a simple, flexible way to simulate dice rolls, calculate ability score modifiers, and generate character stats.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with DiceRoller, you’ll need Python 3.6 or later. Follow these steps to install it:

### Using pip
Install DiceRoller directly from PyPI:

```bash
pip install dice-roller
```

### Manual Installation
Alternatively, clone the repository and install it manually:

```bash
git clone https://github.com/your-username/dice-roller.git
cd dice-roller
python setup.py install
```

## Usage

DiceRoller includes two primary classes: `DiceRoller` for rolling dice and `StatCalculators` for handling D&D-specific calculations. Below are examples of how to use them.

### DiceRoller

The `DiceRoller` class lets you roll a specified number of dice with a given number of sides. You can sort the results or request detailed output (e.g., for d100 rolls).

#### Example: Rolling 4d6 with Sorted Results
This simulates rolling four six-sided dice (4d6) and sorts the results in descending order:

```python
from dice_roller import DiceRoller

roll_results = DiceRoller.rollDice(4, 6, sort=True)
DiceRoller.printRolltoConsole(roll_results)
```

**Sample Output:**
```
Result of 4 d6:
• Roll 1: 6
• Roll 2: 5
• Roll 3: 4
• Roll 4: 2
---------------
Total: 17
Average: 4.25
```

#### Example: Rolling a d100 with Detailed Output
This rolls a percentile die (d100) and shows the individual d10 components:

```python
roll_results = DiceRoller.rollDice(1, 100, detailed=True)
DiceRoller.printRolltoConsole(roll_results)
```

**Sample Output:**
```
Result of 1 d100:
• Roll 1: 42 (40, 2)
---------------
Total: 42
Average: 42.0
```

### StatCalculators

The `StatCalculators` class helps with D&D-specific tasks, like calculating ability score modifiers or generating stats.

#### Example: Calculating an Ability Score Modifier
This calculates the modifier for an ability score of 16:

```python
from dice_roller import StatCalculators

modifier = StatCalculators.getModifier(16)
print(modifier)  # Output: 3
```

#### Example: Generating a Character Stat
This rolls 4d6, drops the lowest roll, and returns the total for a character stat:

```python
from dice_roller import DiceRoller, StatCalculators

roll_results = DiceRoller.rollDice(4, 6, sort=True)
stat = StatCalculators.rollForStats(roll_results)
print(stat)  # Output: e.g., 15
```

## Features

- Roll any number of dice with any number of sides.
- Option to sort dice rolls in descending order.
- Detailed output for d100 rolls (showing tens and ones).
- Calculate D&D ability score modifiers based on scores.
- Generate character stats using the "4d6 drop lowest" method.
- Formatted console output for easy reading.

## Contributing

We welcome contributions to DiceRoller! To contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on GitHub.
2. **Create a Branch**: Make a new branch for your feature or bugfix (`git checkout -b feature-name`).
3. **Write Tests**: Add tests to verify your changes.
4. **Submit a Pull Request**: Push your branch and create a pull request on GitHub.

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing Guidelines](CONTRIBUTING.md).

## License

DiceRoller is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

---

### How to Customize This README for Your Project
- **Project Title and Description**: Replace "DiceRoller" with your project’s name and update the description to reflect its purpose.
- **Installation**: Add any specific dependencies or setup steps your project requires.
- **Usage**: Include examples that showcase your project’s functionality—add more if you have additional features.
- **Features**: List the key features of your project to highlight what makes it unique.
- **Contributing and License**: Update links to point to your actual files (e.g., `CONTRIBUTING.md`), and choose a license that suits your needs.

This README provides a clear, professional structure that’s easy to adapt. It’s designed to help users understand your project, install it, and contribute if they’d like. Let me know if you’d like to tweak it further!