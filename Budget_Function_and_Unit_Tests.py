
from typing import Tuple

VALID_CATEGORIES = ["mortgage", "auto payment", "insurance", "credit card", "utility"]

def manage_household_finances(
    income: list[dict[str, float]], expenses: list[dict[str, Tuple[str, float]]]
) -> dict[str, dict[str, float]]:
    """
    Organizes and totals household expenses by categories and calculates the percentage
    of total income used by each expense category. Validates expense categories against
    a predefined list of valid categories.

    Args:
        income (list[dict[str, float]]): A list of dictionaries where each dictionary contains 'source' and 'amount' of income.
        expenses (list[dict[str, Tuple[str, float]]]): A list of dictionaries where each dictionary contains 'category' and ('description', 'amount') tuples for expenses.

    Returns:
        dict[str, dict[str, float]]: A dictionary with expense categories as keys and dictionaries as values. Each inner dictionary contains 'total' expense and 'percentage' of total income for the category.

    Raises:
        ValueError: If total income is 0, preventing division by zero in percentage calculation.
        ValueError: If an expense category is not recognized.
    """
    # Calculate total income
    total_income = sum(income_source["amount"] for income_source in income)
    if total_income == 0:
        raise ValueError("Total income cannot be zero.")

    # Initialize the dictionary to hold categorized expenses
    categorized_expenses = {}

    # Total expenses by category with category validation
    for expense in expenses:
        category, expense_detail = expense["category"], expense["expense"]
        expense_amount = expense_detail[1]
        if category not in VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")

        if category in categorized_expenses:
            categorized_expenses[category]["total"] += expense_amount
        else:
            categorized_expenses[category] = {"total": expense_amount, "percentage": 0}

    # Calculate the percentage of total income for each category
    for category, expense_info in categorized_expenses.items():
        expense_info["percentage"] = (expense_info["total"] / total_income) * 100

    return categorized_expenses

import unittest


class TestManageHouseholdFinances(unittest.TestCase):
    def setUp(self):
        self.income = [{"source": "Job 1", "amount": 3000},
                       {"source": "Job 2", "amount": 2000}]
        self.expenses = [
            {"category": "mortgage", "expense": ("Mortgage payment", 1500)},
            {"category": "utility", "expense": ("Electric bill", 500)},
            {"category": "insurance", "expense": ("Car insurance", 250)}
        ]

    def test_expense_categorization(self):
        result = manage_household_finances(self.income, self.expenses)
        self.assertIn("mortgage", result)
        self.assertIn("utility", result)
        self.assertIn("insurance", result)
        self.assertAlmostEqual(result["mortgage"]["percentage"], 30)
        self.assertAlmostEqual(result["utility"]["percentage"], 10)
        self.assertAlmostEqual(result["insurance"]["percentage"], 5)

    def test_total_income_zero(self):
        with self.assertRaises(ValueError):
            manage_household_finances([{"source": "Job", "amount": 0}], self.expenses)

    def test_invalid_expense_category(self):
        invalid_expenses = self.expenses + [{"category": "entertainment", "expense": ("Concert tickets", 100)}]
        with self.assertRaises(ValueError):
            manage_household_finances(self.income, invalid_expenses)

    def test_empty_expenses(self):
        result = manage_household_finances(self.income, [])
  

    def test_expense_with_valid_and_invalid_categories(self):
        mixed_expenses = self.expenses + [{"category": "invalid_category", "expense": ("Invalid expense", 500)}]
        with self.assertRaises(ValueError):
            manage_household_finances(self.income, mixed_expenses)

if __name__ == "__main__":
    unittest.main()
