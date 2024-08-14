import unittest

from examples import json_object1
from validate_json import validate_json


class Validate_JSON(unittest.TestCase):
    def test_less_than_max_depth(self):
        result = validate_json(json_object1, 10)
        self.assertEqual(result, True)

    def test_more_than_max_depth(self):
        result = validate_json(json_object1, 2)
        self.assertEqual(result, False)

    def test_equal_max_depth(self):
        result = validate_json(json_object1, 4)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
