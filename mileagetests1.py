def update_mileage(mileage_record: dict, miles: float, trip_type: str) -> None:
    """
    Update the mileage record for a company car, categorizing miles as either business or personal.

    Args:
        mileage_record (dict): A dictionary containing 'business_miles' and 'personal_miles'.
        miles (float): The number of miles driven in the trip.
        trip_type (str): The type of trip, either 'business' or 'personal'.

    Raises:
        ValueError: If miles is negative or trip_type is not 'business' or 'personal'.
    """
    if miles < 0:
        raise ValueError("Miles cannot be negative.")
    
    if trip_type not in ['business', 'personal']:
        raise ValueError("Trip type must be 'business' or 'personal'.")

    if trip_type == 'business':
        mileage_record['business_miles'] += miles
    else:
        mileage_record['personal_miles'] += miles

# Example usage
mileage_record = {'business_miles': 0.0, 'personal_miles': 0.0}

# Record a business trip of 15.5 miles
update_mileage(mileage_record, 15.5, 'business')

# Record a personal trip of 7.3 miles
update_mileage(mileage_record, 7.3, 'personal')

print(mileage_record)  # Output will show updated mileage for business and personal trips

import unittest



class TestUpdateMileage(unittest.TestCase):
    def setUp(self) -> None:
        self.mileage_record = {'business_miles': 0.0, 'personal_miles': 0.0}

    def test_business_trip(self) -> None:
        update_mileage(self.mileage_record, 20.0, 'business')
        self.assertEqual(self.mileage_record['business_miles'], 20.0)

    def test_personal_trip(self) -> None:
        update_mileage(self.mileage_record, 15.0, 'personal')
        self.assertEqual(self.mileage_record['personal_miles'], 15.0)

    def test_combined_mileage(self) -> None:
        update_mileage(self.mileage_record, 10.0, 'business')
        update_mileage(self.mileage_record, 5.0, 'personal')
        self.assertEqual(self.mileage_record['business_miles'], 10.0)
        self.assertEqual(self.mileage_record['personal_miles'], 5.0)

    def test_negative_miles(self) -> None:
        with self.assertRaises(ValueError):
            update_mileage(self.mileage_record, -5.0, 'business')

    def test_invalid_trip_type(self) -> None:
        with self.assertRaises(ValueError):
            update_mileage(self.mileage_record, 10.0, 'party')

if __name__ == "__main__":
    unittest.main()
