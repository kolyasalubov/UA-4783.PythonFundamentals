import unittest
import functions
import functions_with_errors

class Test_for_All(unittest.TestCase):

    def setUp(self):
        self.modules = [functions, functions_with_errors]

    def test_greeting(self):
        for x in self.modules:
            self.assertEqual(x.greeting_by_name("Vasya"), "Hello Vasya!")
            self.assertEqual(x.greeting_by_name(55), "Hello 55!")
            self.assertEqual(x.greeting_by_name(""), "Hello !")
    
    def test_symbol_position(self):
        for x in self.modules:
            self.assertEqual(x.get_symbol_position("Vasya", "ty"), "Error! Symbol can be string with only one letter")
            self.assertEqual(x.get_symbol_position("Vasya", "a"), 2)
            self.assertEqual(x.get_symbol_position("Vasya", "o"), "Not found")
    
    def test_merge(self):
        dict1 = {1: "a", 2: "b"}
        dict2 = {"name": "Vasya", "age": 20}
        for x in self.modules:
            result = x.merge(dict1, dict2)
            self.assertIsNot(dict1, result)
            self.assertEqual(len(result), 4)

if __name__ == "__main__":
    unittest.main()
