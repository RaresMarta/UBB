import unittest
from src.Project import Project


class ProjectTests(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Project class
        self.project = Project("Project 1", "Sustainability", "John Doe", 5)

    def test_get_name(self):
        # Test the get_name method
        self.assertEqual(self.project.get_name(), "Project 1")

    def test_get_number(self):
        # Test the get_number method
        self.assertEqual(self.project.get_number(), 6)

    def test_set_number(self):
        # Test the set_number method
        self.project.set_number(10)
        self.assertEqual(self.project.get_number(), 10)

    def test_get_theme(self):
        # Test the get_theme method
        self.assertEqual(self.project.get_theme(), "Sustainability")

    def test_str(self):
        # Test the __str__ method
        expected_output = "Project 1 with theme Sustainability by John Doe and 5 others"
        self.assertEqual(str(self.project), expected_output)

    def tearDown(self):
        # Clean up any resources used for testing
        self.project = None


if __name__ == "__main__":
    unittest.main()
