def calculate_depreciation(asset_value: float, lifespan: int) -> float:
    """
    Calculate the annual depreciation of an asset using the straight-line method.

    Args:
        asset_value (float): The initial value of the asset.
        lifespan (int): The expected useful life of the asset in years.

    Returns:
        float: The annual depreciation value of the asset.

    Raises:
        ValueError: If asset_value is less than or equal to 0 or if lifespan is less than 1.
    """
    if asset_value <= 0 or lifespan < 1:
        raise ValueError("Asset value must be greater than 0 and lifespan must be at least 1 year.")
    annual_depreciation = asset_value / lifespan
    return annual_depreciation

import unittest

class TestCalculateDepreciation(unittest.TestCase):
    def test_calculate_depreciation(self):
        self.assertAlmostEqual(calculate_depreciation(10000, 5), 2000)

    def test_zero_lifespan(self):
        with self.assertRaises(ValueError):
            calculate_depreciation(6000, 0)

    def test_negative_asset_value(self):
        with self.assertRaises(ValueError):
            calculate_depreciation(-6000, 5)

    def test_large_asset_value(self):
        self.assertAlmostEqual(calculate_depreciation(80000, 10), 8000)

    def test_one_year_lifespan(self):
        self.assertAlmostEqual(calculate_depreciation(5000, 1), 5000)

if __name__ == "__main__":
    unittest.main()
