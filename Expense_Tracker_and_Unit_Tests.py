def track_expenses(expense_record: dict, new_expense: dict) -> None:
    """
    Updates the expense record with a new expense entry.

    Args:
        expense_record (dict): The current record of expenses, keyed by date with lists of expenses as values.
        new_expense (dict): Details of the new expense to add, including 'amount', 'date', and 'category'.

    Raises:
        ValueError: If 'amount' is negative, 'date' is not in YYYY-MM-DD format, or 'category' is not recognized.
    """
    # Validate new_expense data
    if new_expense['amount'] <= 0:
        raise ValueError("Expense amount must be positive.")
    if 'date' not in new_expense or 'category' not in new_expense:
        raise ValueError("Each expense must have a date and category.")

    # Update the record
    date = new_expense['date']
    if date in expense_record:
        expense_record[date].append(new_expense)
    else:
        expense_record[date] = [new_expense]

import unittest


class TestTrackExpenses(unittest.TestCase):
    def setUp(self):
        self.expense_record = {}

    def test_add_new_expense(self):
        new_expense = {'amount': 100, 'date': '2023-03-01', 'category': 'supplies'}
        track_expenses(self.expense_record, new_expense)
        self.assertIn('2023-03-01', self.expense_record)
        self.assertIn(new_expense, self.expense_record['2023-03-01'])

    def test_add_invalid_amount(self):
        new_expense = {'amount': -50, 'date': '2023-03-02', 'category': 'travel'}
        with self.assertRaises(ValueError):
            track_expenses(self.expense_record, new_expense)

    def test_missing_category(self):
        new_expense = {'amount': 50, 'date': '2023-03-03'}
        with self.assertRaises(ValueError):
            track_expenses(self.expense_record, new_expense)

    def test_multiple_expenses_same_date(self):
        expenses = [{'amount': 55, 'date': '2023-03-04', 'category': 'meals'},
                    {'amount': 95, 'date': '2023-03-04', 'category': 'travel'}]
        for exp in expenses:
            track_expenses(self.expense_record, exp)
        self.assertEqual(len(self.expense_record['2023-03-04']), 2)

if __name__ == "__main__":
    unittest.main()
