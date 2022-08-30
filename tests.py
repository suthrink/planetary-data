import unittest
from main import *
class TestPlanet(unittest.TestCase):
    def test_count_moons_with_rings(self):
        planet_test_set = []
        planet_test_set.append(Planet("Earth", [], 10, True))
        planet_test_set.append(Planet("Mars", [], 2, False))
        expected_value = 10
        message = "Moon count should be 10!"
        self.assertEqual(count_of_moons_for_planet(planet_test_set, has_ring=True), expected_value, message)
  
    def test_count_moons_without_rings(self):
        planet_test_set = []
        planet_test_set.append(Planet("Earth", [], 10, True))
        planet_test_set.append(Planet("Mars", [], 2, False))
        expected_value = 2
        message = "Moon count should be 2!"
        self.assertEqual(count_of_moons_for_planet(planet_test_set, has_ring=False), expected_value, message)
  
    def test_most_common_gases(self):
        planet_test_set = []
        planet_test_set.append(Planet("Earth", ["Nitrogen", "Helium"], 1, True))
        planet_test_set.append(Planet("Mars", ["Nitrogen", "Hydrogen"], 0, False))
        expected_value = "Nitrogen"
        message = "Expected value should be Nitrogen"
        self.assertEqual(most_common_gases(planet_test_set), expected_value, message)

if __name__ == '__main__':
    unittest.main()