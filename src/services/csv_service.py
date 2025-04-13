"""
Responsible for reading employee and assignment data from Excel files,
and writing final assignments to a CSV file.
"""

import csv
from typing import List

import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger("main")

class FileService:
    """A service to handle file operations for employee assignments."""
    @staticmethod
    def read_employees(file_path):
        """Reads employee data from a file."""
        df = pd.read_excel(file_path)  # for .xlsx

        logger.info("Reading employee data from file.")
        return [
            {
                "name": row["Employee_Name"],
                "email": row["Employee_EmailID"]
            }
            for _, row in df.iterrows()
        ]

    @staticmethod
    def read_previous_assignments(file_path):
        """Reads previous assignments from a file."""
        df = pd.read_excel(file_path)  # for .xlsx

        logger.info("Starting to read previous assignments.")
        return {
            row["Employee_EmailID"]: row["Secret_Child_EmailID"]
            for _, row in df.iterrows()
        }

    @staticmethod
    def write_assignments(assignments: List[dict], output_path: str):
        """Writes the final assignments to a CSV file."""
        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            logger.info("Starting to write assignments to CSV file.")
            writer = csv.DictWriter(file, fieldnames=[
                "Employee_Name", "Employee_EmailID",
                "Secret_Child_Name", "Secret_Child_EmailID"
            ])
            writer.writeheader()
            writer.writerows(assignments)
