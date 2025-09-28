from typing import Dict, List, Tuple


def greedy_algorithm(items: Dict[str, Dict[str, float]], budget: float) -> Tuple[List[Tuple[str, float, float]], float, float, float]:
    """
    Greedy algorithm to maximize calories within a given budget.
    Args:
        items (dict): A dictionary where keys are item names and values are
                      dictionaries with 'cost' and 'calories'.
        budget (float): The total budget available.
    Returns:
        tuple: A tuple containing the list of selected items, total cost,
               total calories, and leftover budget.
    """
    if budget <= 0:
        return [], 0, 0, budget

    sorted_items = sorted(
        items.items(), key=lambda i: i[1]['calories']/i[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0
    leftover = budget

    for item in sorted_items:
        if leftover == 0:
            break
        if leftover >= item[1]['cost']:
            total_cost += item[1]['cost']
            total_calories += item[1]['calories']
            leftover -= item[1]['cost']
            selected_items.append((item))

    return selected_items, total_cost, total_calories, leftover


def dynamic_programming(items: Dict[str, Dict[str, float]], budget: float) -> Tuple[List[Tuple[str, float, float]], float, float, float]:
    """
    Dynamic programming algorithm to maximize calories within a given budget.
    Args:
        items (dict): A dictionary where keys are item names and values are
                      dictionaries with 'cost' and 'calories'.
        budget (float): The total budget available.
    Returns:
        tuple: A tuple containing the list of selected items, total cost,
               total calories, and leftover budget.
    """
    if budget <= 0 or not items:
        return [], 0, 0, budget

    item_names = list(items.keys())
    items_costs = [items[name]['cost'] for name in item_names]
    items_calories = [items[name]['calories'] for name in item_names]
    items_count = len(item_names)
    table = [[0] * (budget + 1) for _ in range(items_count + 1)]

    # Build table
    for i in range(1, items_count + 1):
        item_cost = items_costs[i - 1]
        item_calory = items_calories[i - 1]
        for budget_value in range(budget + 1):
            best = table[i - 1][budget_value]
            if item_cost <= budget_value:
                candidate = table[i - 1][budget_value -
                                         item_cost] + item_calory
                if candidate > best:
                    best = candidate
            table[i][budget_value] = best

    selected: List[Tuple[str, float, float]] = []
    budget_value = budget
    for i in range(items_count, 0, -1):
        if table[i][budget_value] != table[i - 1][budget_value]:
            name = item_names[i - 1]
            selected.append(
                (name, items_costs[i - 1], items_calories[i - 1]))
            budget_value -= items_costs[i - 1]
    selected.reverse()
    total_cost = sum(cost for _, cost, _ in selected)
    total_calories = table[items_count][budget]
    leftover = budget - total_cost

    return selected, total_cost, total_calories, leftover


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

if __name__ == "__main__":
    budget = 70
    print("\n-Greedy-\n")
    bought_items, total_cost, total_calories, leftover = greedy_algorithm(
        items, budget)
    print("Items: ", bought_items)
    print("Sum:", total_cost)
    print("Calories:", total_calories)
    print("Leftover:", leftover)

    print("\n-Dinamic-\n")
    bought_items, total_cost, total_calories, leftover = dynamic_programming(
        items, budget)
    print("Items: ", bought_items)
    print("Sum:", total_cost)
    print("Calories:", total_calories)
    print("Leftover:", leftover)
