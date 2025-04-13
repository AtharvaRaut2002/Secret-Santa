"""
Test cases for the AssignmentService and FileService classes.
"""
import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from src.services.assignment_service import AssignmentService
from src.services.csv_service import FileService


class TestAssignmentService(unittest.TestCase):
    """Test cases for the AssignmentService class."""
    def setUp(self):
        """Set up test data."""
        self.employees = [
            {"name":"Alice", "email":"alice@example.com"},
            {"name":"Bob", "email":"bob@example.com"},
            {"name":"Charlie", "email":"charlie@example.com"}
        ]
        self.prev_assignments = {
            "alice@example.com": "charlie@example.com",
            "bob@example.com": "alice@example.com",
            "charlie@example.com": "bob@example.com"
        }

    def test_generate_assignments(self):
        """Test generating assignments."""
        assignments = AssignmentService.generate_assignments(self.employees, self.prev_assignments)
        self.assertEqual(len(assignments), len(self.employees))

        receivers = set()
        for assignment in assignments:
            giver = assignment["Employee_EmailID"]
            receiver = assignment["Secret_Child_EmailID"]

            self.assertNotEqual(giver, receiver)
            self.assertNotEqual(receiver, self.prev_assignments.get(giver))
            self.assertNotIn(receiver, receivers)
            receivers.add(receiver)


class TestFileService(unittest.TestCase):
    """Test cases for the FileService class."""
    @patch("pandas.read_excel")
    def test_read_employees(self, mock_read_excel):
        """Test reading employees from an Excel file."""
        mock_read_excel.return_value = pd.DataFrame([
            {"Employee_Name": "Hamish Murray", "Employee_EmailID": "hamish.murray@acme.com"}
        ])

        employees = FileService.read_employees("dummy_path.xlsx")
        self.assertEqual(len(employees), 1)
        print("employee  -------------------------------,", employees[0])
        self.assertEqual(employees[0],{"name":"Hamish Murray", "email":"hamish.murray@acme.com"})

    @patch("pandas.read_excel")
    def test_read_previous_assignments(self, mock_read_excel):
        """Test reading previous assignments from an Excel file."""
        mock_read_excel.return_value = pd.DataFrame([
            {"Employee_EmailID": "alice@example.com", "Secret_Child_EmailID": "bob@example.com"}
        ])

        assignments = FileService.read_previous_assignments("dummy_path.xlsx")
        self.assertEqual(assignments, {"alice@example.com": "bob@example.com"})

if __name__ == "__main__":
    unittest.main()
