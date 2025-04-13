"""
Main entry point for the Secret Santa assignment generator.

Reads employee and previous assignment data, generates new Secret Santa assignments,
and writes the results to a CSV file.
"""

import os
from src.services.assignment_service import AssignmentService
from src.services.csv_service import FileService
from src.utils.logger import setup_logger

logger = setup_logger("main")

def main():
    """Main function to read employee data, generate assignments, and write to xlsx."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logger.info("Starting Secret Santa assignment script.")

    # File paths
    employee_path = os.path.join(base_dir, "data", "employees.xlsx")
    previous_assignments_path = os.path.join(base_dir, "data", "last_year_assignments.xlsx")
    output_path = os.path.join(base_dir, "output", "secret_santa_assignments.csv")

    try:
        # Read input data
        employees = FileService.read_employees(employee_path)
        prev_assignments = FileService.read_previous_assignments(previous_assignments_path)

        # Generate new assignments
        assignments = AssignmentService.generate_assignments(employees, prev_assignments)

        # Write to output file
        FileService.write_assignments(assignments, output_path)
        logger.info("Assignments generated and written to output file successfully.")

    except FileNotFoundError as e:
        logger.error("❌ File not found: %s", e)
    except ValueError as e:
        logger.error("❌ Value error: %s", e)
    except (IOError, OSError) as e:
        logger.error("❌ File system error: %s", e)
    except Exception as e:
        logger.error("❌ Unexpected error: %s", e)
        raise

if __name__ == "__main__":
    main()
