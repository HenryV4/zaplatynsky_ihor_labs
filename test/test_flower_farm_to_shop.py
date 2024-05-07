import unittest
from src.flower_farm_to_shop import calculate_max_flow


class TestMaxFlow(unittest.TestCase):
    def test_max_flow_1(self):
        expected_max_flow = 51
        actual_max_flow = calculate_max_flow(
            "C:/projects/zaplatynsky_ihor_labs/resources/roads.csv"
        )
        self.assertEqual(actual_max_flow, expected_max_flow)

    def test_max_flow_2(self):
        expected_max_flow = 0
        actual_max_flow = calculate_max_flow(
            "C:/projects/zaplatynsky_ihor_labs/resources/roads_no_way.csv"
        )
        self.assertEqual(actual_max_flow, expected_max_flow)


if __name__ == "__main__":
    unittest.main()
