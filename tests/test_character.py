import unittest

from main import create_character


class CharacterTests(unittest.TestCase):
    def test_creates_valid_character(self):
        self.assertEqual(
            create_character("Ren", 4, 2, 1),
            "Ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○",
        )

    def test_rejects_name_with_spaces(self):
        self.assertEqual(create_character("Red Mage", 4, 2, 1),
                         "The character name should not contain spaces.")

    def test_requires_seven_points(self):
        self.assertEqual(create_character("Ren", 3, 2, 1),
                         "The character should start with 7 points.")

    def test_rejects_out_of_range_stats(self):
        self.assertEqual(create_character("Ren", 5, 1, 1),
                         "All stats should be no more than 4.")


if __name__ == "__main__":
    unittest.main()
