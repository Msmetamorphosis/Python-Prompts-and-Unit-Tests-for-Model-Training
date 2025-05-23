# 🧪 Python Prompts & Unit Tests for Model Training

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Use Case](https://img.shields.io/badge/use--case-LLM%20Training-blueviolet)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![Test Coverage](https://img.shields.io/badge/test--coverage-100%25-success)
![Created By](https://img.shields.io/badge/created%20by-Advanced%20AI%20Data%20Trainer-lightgrey)

This repository showcases Python prompts and unit tests I developed while working as an **Advanced AI Data Trainer and Prompt Engineer** on the programming & data science team for contracted projects for Google, Meta, Anthropic and OpenAI. The scripts here were used to help fine-tune and evaluate LLMs in understanding logic, writing functions, and generating accurate unit tests.

---

## 🧠 Project Purpose

These files were crafted to simulate real-world developer tasks and test cases, helping improve LLM capabilities in:
- Python reasoning and code synthesis
- Function creation and logic structuring
- Unit test generation and validation
- Contextual understanding of finance, utilities, and tracking domains

All examples are original and engineered for high-value prompt-response learning and error handling.

---

## 📁 File Highlights

| Filename                            | Functionality Description                                                                 |
|------------------------------------|-------------------------------------------------------------------------------------------|
| `Budget_Function_and_Unit_Tests.py` | Categorizes and calculates household budget allocations with category validation logic   |
| `Depreciation_tests_for_LLM.py`     | Calculates asset depreciation using the straight-line method with full unit test coverage |
| `Expense_Tracker_and_Unit_Tests.py` | Tracks monthly expenses and evaluates budget thresholds                                   |
| `Loan_Tracker_Unit_Tests.py`        | Updates loan balances with interest and validates negative payment edge cases             |
| `mileagetests1.py`                  | Records business vs personal mileage and updates totals with validation checks            |

---

## 💬 Prompt & Response Examples

| 🧾 Prompt (User) | 💡 Assistant Response (LLM) |
|------------------|----------------------------|
| “How do I calculate the depreciation of a $10,000 asset over 5 years?” | `calculate_depreciation(10000, 5)` → `2000.0` |
| “Track a $1,000 loan with $100 monthly payments and 5% interest.” | Updates balance, calculates cumulative interest, validates inputs |
| “Log 15.5 miles as a business trip and 7.3 as personal.” | Adds miles to `business_miles` and `personal_miles` keys in a dictionary |
| “What if my total income is $0 when calculating budget allocation?” | Raises `ValueError`: “Total income cannot be zero.” |
| “How can I test that my function raises an error when the asset value is negative?” | Uses `unittest.TestCase.assertRaises` with negative input |

---

## 🛠 Applications

These prompt + unit test pairs were used in:
- LLM **code reasoning evaluations**
- **Helpfulness/harmfulness** filtering rounds
- **Unit test generation training**
- **Prompt tuning** for AI developer copilots

The goal was to build LLM behaviors that mimic experienced Python developers’ logical structures and test coverage standards.

---

## 💼 Skills Demonstrated

- Python 3.x (typed functions, edge case validation)
- `unittest` testing framework
- Prompt engineering for LLM training
- Functional decomposition and test-driven development (TDD)
- Finance, productivity, and tracking use cases

---

## 🤝 Let’s Connect

If you're building coding copilots, educational AI tools, or want to integrate unit test generation into your LLM workflows, I’d love to collaborate or customize datasets like these further.

> All files are my original work used in professional LLM training contexts. Feel free to fork, use, or adapt them as needed.
