import unittest
from src.Project import Project
from repo.ProjectRepo import ProjectRepo


class ProjectRepoTests(unittest.TestCase):
    def setUp(self):
        # Create an instance of the ProjectRepo class
        self.repo = ProjectRepo()

        # Create some sample projects
        self.project1 = Project("AKd", "Teaching", "Hercule Poirot", 3)
        self.project2 = Project("Help", "Sustainability", "Cosmin", 0)
        self.project3 = Project("Developed+", "Development", "Mario64", 2)

    def test_add_project(self):
        # Test adding a project to the repository
        self.repo.add_project(self.project1)
        self.assertEqual(len(self.repo._ProjectRepo__projects), 1)

    def test_add_duplicate_project(self):
        # Test adding a duplicate project to the repository
        self.repo.add_project(self.project1)
        with self.assertRaises(ValueError):
            self.repo.add_project(self.project1)

    def test_add_project_with_existing_name(self):
        # Test adding a project with an existing name to the repository
        self.repo.add_project(self.project1)
        with self.assertRaises(ValueError):
            self.project1.set_number(2)
            self.repo.add_project(self.project1)

    def test_limit_number_by_theme(self):
        # Test limiting the number of projects by theme
        self.repo.add_project(self.project1)
        self.repo.add_project(self.project2)
        self.repo.limit_number_by_theme(2, "Development")
        self.assertEqual(self.project1.get_number(), 4)
        self.assertEqual(self.project2.get_number(), 1)

    def test_limit_number_by_theme_invalid_number(self):
        # Test limiting the number of projects by theme with an invalid number
        self.repo.add_project(self.project1)
        with self.assertRaises(ValueError):
            self.repo.limit_number_by_theme(0, "Teaching")

    def test_delete_by_name(self):
        # Test deleting a project by name
        self.repo.add_project(self.project1)
        self.repo.add_project(self.project2)
        self.repo.delete_by_name("AKd")
        self.assertEqual(len(self.repo._ProjectRepo__projects), 1)

    def test_delete_nonexistent_project(self):
        # Test deleting a nonexistent project by name
        self.repo.add_project(self.project1)
        with self.assertRaises(ValueError):
            self.repo.delete_by_name("Help")

    def test_str(self):
        # Test the string representation of the ProjectRepo object
        self.repo.add_project(self.project1)
        self.repo.add_project(self.project2)
        expected_output = "AKd with theme Teaching by Hercule Poirot and 3 others\nHelp with theme Sustainability by Cosmin and 0 others"
        self.assertEqual(str(self.repo), expected_output)

    def tearDown(self):
        # Clean up any resources used for testing
        self.repo = None


if __name__ == "__main__":
    unittest.main()
