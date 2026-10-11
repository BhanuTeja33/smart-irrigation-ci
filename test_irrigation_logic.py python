import csv
import os
import unittest

from irrigation_logic import decide_irrigation


class TestIrrigationLogic(unittest.TestCase):

    def test_irrigate_case(self):
        self.assertEqual(decide_irrigation(20, 28), "IRRIGATE")

    def test_skip_due_to_moisture(self):
        self.assertEqual(decide_irrigation(45, 30), "SKIP")

    def test_skip_due_to_cold(self):
        self.assertEqual(decide_irrigation(25, 15), "SKIP")

    def test_boundary_values(self):
        self.assertEqual(decide_irrigation(29, 20), "IRRIGATE")
        self.assertEqual(decide_irrigation(30, 25), "SKIP")

    def test_dataset_rows(self):
        path = os.path.join(os.path.dirname(__file__), "field_readings.csv")
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                with self.subTest(field=row["field_id"]):
                    result = decide_irrigation(
                        float(row["soil_moisture"]), float(row["temperature"])
                    )
                    self.assertEqual(result, row["expected"])


if __name__ == "__main__":
    unittest.main()
