from typing import Dict

import numpy as np


def evaluate_dice_roll(roll_count: int = 10_000) -> Dict[int, float]:
    """
    Simulate rolling two six-sided dice multiple times and evaluate the probability
    of each possible sum (from 2 to 12).
    Args:
        roll_count (int, optional): Number of dice rolls to simulate. Defaults to 10000.
    Returns:
        dict: A dictionary where keys are possible sums (2-12) and values are their probabilities.
    """
    experiments: Dict[int, int] = {}

    for _ in range(roll_count):
        roll = np.random.randint(1, 7, 2)
        roll_value = sum(dice_value for dice_value in roll)
        experiments[int(roll_value)] = experiments.get(roll_value, 0) + 1

    return {dice_sum: experiments[dice_sum]/roll_count for dice_sum in sorted(experiments)}


if __name__ == '__main__':
    print("Сума | Імовірність")
    experiments_count = 100_000
    results = evaluate_dice_roll(100_000)
    for dice_value, probability in results.items():
        print(f"{dice_value:4d} | {probability*100:.2f}%")
