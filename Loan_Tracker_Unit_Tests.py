# Here is the prompt to use with this function and the unit tests:
# "I'm using this function to track my personal loan balance and the total interest paid on it.
# It updates the balances after each monthly payment and raises a 'ValueError'
# if either the monthly payment or loan balance values are negative."


def modify_loan_balance(loan_details: dict) -> None:
    """

    Update the car loan balance and the running total of interest paid.



    Args:

        loan_details (dict): A dictionary containing 'loan_balance', 'monthly_payment',

                             'interest_rate', and 'total_interest_paid' keys.



    Returns:

        None: The function updates the dictionary in place.



    Raises:

        ValueError: If loan balance or monthly payment is negative.

    """

    # Extract loan details

    loan_balance = loan_details.get("loan_balance")

    monthly_payment = loan_details.get("monthly_payment")

    interest_rate = (
        loan_details.get("interest_rate") / 100
    )  # Convert percentage to decimal

    total_interest_paid = loan_details.get("total_interest_paid", 0)

    # Validate inputs

    if loan_balance < 0 or monthly_payment < 0:
        raise ValueError("Loan balance and monthly payment must be non-negative.")

    # Calculate interest for the current month

    monthly_interest = loan_balance * interest_rate / 12

    # Update the total interest paid

    loan_details["total_interest_paid"] = total_interest_paid + monthly_interest

    # Update the loan balance

    principal_payment = monthly_payment - monthly_interest

    loan_details["loan_balance"] = loan_balance - principal_payment


import unittest


class TestModifyLoanBalance(unittest.TestCase):
    def test_normal_payment(self):
        loan_details = {
            "loan_balance": 20000,
            "monthly_payment": 1000,
            "interest_rate": 5,
            "total_interest_paid": 0,
        }

        monthly_interest = (
            loan_details["loan_balance"] * (loan_details["interest_rate"] / 100) / 12
        )

        modify_loan_balance(loan_details)

        principal_payment = 1000 - monthly_interest

        expected_balance = 20000 - principal_payment

        self.assertAlmostEqual(loan_details["loan_balance"], expected_balance, places=2)

        self.assertAlmostEqual(
            loan_details["total_interest_paid"], monthly_interest, places=2
        )

    def test_full_payment(self):
        loan_details = {
            "loan_balance": 1000,
            "monthly_payment": 1000,
            "interest_rate": 5,
            "total_interest_paid": 0,
        }

        monthly_interest = (
            loan_details["loan_balance"] * (loan_details["interest_rate"] / 100) / 12
        )

        modify_loan_balance(loan_details)

        principal_payment = 500 - monthly_interest

        expected_balance = 500 - principal_payment

        self.assertAlmostEqual(loan_details["loan_balance"], expected_balance, places=2)

        self.assertAlmostEqual(
            loan_details["total_interest_paid"], monthly_interest, places=2
        )

    def test_negative_loan_balance(self):
        loan_details = {
            "loan_balance": -2000,
            "monthly_payment": 1000,
            "interest_rate": 5,
            "total_interest_paid": 0,
        }

        with self.assertRaises(ValueError):
            modify_loan_balance(loan_details)

    def test_negative_payment(self):
        loan_details = {
            "loan_balance": 10000,
            "monthly_payment": -1000,
            "interest_rate": 5,
            "total_interest_paid": 0,
        }

        with self.assertRaises(ValueError):
            modify_loan_balance(loan_details)


if __name__ == "__main__":
    unittest.main()
