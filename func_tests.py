# Ben
import unittest
import func

class TestCases(unittest.TestCase):
    def test_user_input_1(self):
        input1 = "Do you like food?"
        input2 = [3, 2]
        expected = 3
        result = func.user_input(input1, input2)
        # This test will work assuming that the user inputs "3", "1", or some acceptable
        #   analogue of those choices
        self.assertEqual(expected, result)
    def test_user_input_2(self):
        input1 = "Which fruit is the best among this list?"
        input2 = ["apple" , "banana", "pomegranate", "kiwi", "orange", "strawberry", "mango"]
        expected = "Strawberry"
        result = func.user_input(input1, input2)
        # This test will work assuming that the user inputs "Strawberry", "6", or some
        #   acceptable analogue of those choices
        self.assertEqual(expected, result)
    def test_user_input_3(self):
        input1 = "Are you sure you like food?"
        input2 = ["yes", "no"]
        input3 = True
        expected = True
        result = func.user_input(input1, input2, input3)
        # This test will work assuming that the user inputs "Yes", "1", or some
        #   acceptable analogue of those choices
        self.assertEqual(expected, result)
    def test_user_input_4(self):
        input1 = "You're sure you like food then?"
        input2 = ["absolutely", "sure", "100% sure, yes sir"]
        expected = "100% sure, yes sir"
        result = func.user_input(input1, input2)
        # This test will work assuming that the user inputs "100% sure, yes sir",
        #   "3", or some acceptable analogue of these choices
        self.assertEqual(expected, result)

    def test_choices_1(self):
        input1 = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        expected = None
        result = func.choices(input1)
        self.assertEqual(expected, result)
        # The print statement should look like:
        # [1] Option 1
        # [2] Option 2
        # [3] Option 3
        # [4] Option 4
        # [5] Option 5
    def test_choices_2(self):
        input1 = [-1, 0, 5, "-6", "-7"]
        expected = None
        result = func.choices(input1)
        self.assertEqual(expected, result)
        # The print statement should look like:
        # [1] -1
        # [2] 0
        # [3] 5
        # [4] -6
        # [5] -7

    def test_confirm_1(self):
        input1 = "Strawberry"
        input2 = "Are you sure your favorite among the list is {}?"
        input3 = "Which fruit is the best among this list?"
        input4 = ["apple", "banana", "pomegranate", "kiwi", "orange", "strawberry", "mango"]
        expected = "Mango"
        result = func.confirm(input1, input2, input3, input4)
        # This test will work assuming that the user:
        #   First inputs "No", "2", or some acceptable analogue
        #   Then inputs "Mango", "7", or some acceptable analogue
        #   And finally selects "Yes", "1", or some acceptable analogue
        # Note that the exact process of choice selection does not matter
        #   as long as the user chooses and confirms their selection as
        #   "Mango" in the end
        self.assertEqual(expected, result)
    def test_confirm_2(self):
        input1 = "Broadsword"
        input2 = "Are you sure you want to choose the {}?"
        input3 = "Which item do you wish to keep?"
        input4 = ["broadsword", "rapier", "The Royal Fish"]
        input5 = {"Broadsword": {"Name": "Broadsword",
                            "Description": "A classic choice of weapon. A sword "
                                           "characterized for its wide blade \n"
                                           "designed for slashing your foes "
                                           "into pieces",
                            "Strength": "+15", "Dexterity": -5, "Agility": -5},
                  "Rapier": {"Name": "Rapier",
                             "Description": "A light, lengthy sword designed for "
                                            "cutting and thrusting your foes. "
                                            "Although it may not do much damage, \n"
                                            "this weapon allows you to stay agile "
                                            "and more easily attack vital areas"
                                            " of your enemies",
                             "Strength": "+5", "Dexterity": 15, "Agility": 3},
                  "The Royal Fish": {"Name": "The Royal Fish",
                            "Description": "This is no ordinary fish. It was taken straight "
                                           "from the shores of Okhotsk and prepared by \n"
                                           "the Royal chefs themselves. Infused with a "
                                           "blackened spice rub and cooked so that its \n"
                                           "center is white and flakey, yet impossibly "
                                           "still juicy, many find it impossible to stop \n"
                                           "eating once they start. This dish is a specialty "
                                           "in the region and one that many claim to have healed \n"
                                           "them after a long and arduous journey. It- \nWhat? You "
                                           "wanted a weapon? I thought you were hungry! "
                                           "Why didn't you say something?",
                            "Health": "+50", "Dexterity": -10, "Agility": -10}}
        expected = "The Royal Fish"
        result = func.confirm(input1, input2, input3, input4, input5)
        # This test will work assuming that the user:
        #   First inputs "No", "2", or some acceptable analogue
        #   Then inputs "The Royal Fish", "3", or some acceptable analogue
        #   And finally selects "Yes", "1", or some acceptable analogue
        # Note that the exact process of choice selection does not matter
        #   as long as the user chooses and confirms their selection as
        #   "The Royal Fish" in the end
        self.assertEqual(expected, result)

    def test_str_to_float_1(self):
        input1 = '12.32'
        expected = 12.32
        result = func.str_to_float(input1)
        self.assertEqual(expected, result)
    def test_str_to_float_2(self):
        input1 = '12.32a'
        expected = None
        result = func.str_to_float(input1)
        self.assertEqual(expected, result)

    def test_separator_1(self):
        input1 = "1234567891234567891234567890"
        expected = None
        result = func.separator(input1)
        self.assertEqual(expected, result)
        # A line of hyphens should be printed that is the same
        # length as the input, so the message printed should be:
        # "----------------------------", which is the same length as:
        # "1234567891234567891234567890"
    def test_separator_2(self):
        input1 = "  2    12345678 91 234567 8912 34567890"
        expected = None
        result = func.separator(input1)
        self.assertEqual(expected, result)
        # A line of hyphens should be printed that is the same
        # length as the input, so the message printed should be:
        # "---------------------------------------", which is the same length as:
        # "  2    12345678 91 234567 8912 34567890"
    def test_separator_3(self):
        input1 = "   "
        expected = None
        result = func.separator(input1)
        self.assertEqual(expected, result)
        # A line of hyphens should be printed that is the same
        # length as the input, so the message printed should be:
        # "---", which is the same length as:
        # "   "

    def test_print_stats_1(self):
        input1 = "Broadsword"
        input2 = {"Broadsword": {
                            "Description": "A classic choice of weapon. A sword "
                                           "characterized for its wide blade \n"
                                           "designed for slashing your foes "
                                           "into pieces",
                            "Name": "Broadsword",
                            "Strength": "+15", "Dexterity": -5, "Agility": -5}}
        expected = None
        result = func.print_stats(input1, input2)
        self.assertEqual(expected, result)
        # The print statement should look like:
        # You have chosen:
        # Name: Broadsword
        #
        # Description:
        # A classic choice of weapon. A sword characterized for its wide blade
        # designed for slashing your foes into pieces
        #
        # Strength: +15, Dexterity: -5, Agility: -5
    def test_print_stats_2(self):
        input1 = "Broadsword"
        input2 = {"Broadsword": {"Name": "Broadsword",
                                 "Strength": "+15", "Dexterity": -5, "Agility": -5,}}
        expected = None
        result = func.print_stats(input1, input2)
        self.assertEqual(expected, result)
        # The print statement should look like:
        # You have chosen:
        # Name: Broadsword
        # Strength: +15, Dexterity: -5, Agility: -5

if __name__ == '__main__':
    unittest.main()
