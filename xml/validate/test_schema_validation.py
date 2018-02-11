import unittest
from xml_utils import validate_schema_from_files


class SchemaValidationTestCase(unittest.TestCase):

    def test_schema_valid(self):
        validate_schema_from_files('./example.xsd', './valid_example.xml')

    def test_schema_invalid(self):
        validate_schema_from_files('./example.xsd', './invalid_example.xml')


if __name__ == '__main__':
    unittest.main()
