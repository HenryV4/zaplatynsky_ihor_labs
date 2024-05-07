import unittest
from src.penguins_city_gas import check_gas_delivery


class TestAggressiveCows(unittest.TestCase):
    def test_1(self):
        cities = ["Lviv", "Kyiv", "Rivne", "Dnipro", "Odesa"]
        storages = ["Storage_1", "Storage_2"]
        pipelines = [
            ["Storage_1", "Lviv"],
            ["Lviv", "Rivne"],
            ["Lviv", "Kyiv"],
            ["Lviv", "Odesa"],
        ]
        self.assertEqual(check_gas_delivery(cities, storages, pipelines), ["Dnipro"])

    def test_no_cities(self):
        cities = []
        storages = ["Storage_1", "Storage_2"]
        pipelines = [["Storage_1", "Storage_2"]]
        self.assertEqual(check_gas_delivery(cities, storages, pipelines), [])

    def test_2(self):
        cities = ["Lviv", "Kyiv", "Rivne", "Dnipro", "Odesa"]
        storages = ["Storage_1", "Storage_2"]
        pipelines = [
            ["Storage_1", "Storage_2"],
            ["Lviv", "Rivne"],
            ["Lviv", "Kyiv"],
            ["Lviv", "Odesa"],
        ]
        self.assertEqual(
            check_gas_delivery(cities, storages, pipelines),
            ["Lviv", "Kyiv", "Rivne", "Dnipro", "Odesa"],
        )


if __name__ == "__main__":
    unittest.main()
