"""
Handles the core logic for generating Secret Santa assignments,
ensuring no duplicate or self-assignments.
"""

import random
from typing import List, Dict
from src.models.employee import Employee
from src.utils.logger import setup_logger

logger = setup_logger("main")

class AssignmentService:
    """Service for generating Secret Santa assignments."""
    @staticmethod
    def generate_assignments(
        employees: List[Employee],
        prev_assignments: Dict[str, str]
    ) -> Dict[Employee, Employee]:
        """
        Generates Secret Santa assignments ensuring no one is assigned to
        themselves or their previous assignment.
        """
        attempts = 100

        for _ in range(attempts):
            shuffled = employees.copy()
            random.shuffle(shuffled)

            assignments = []
            success = True

            for giver, receiver in zip(employees, shuffled):
                # Ensure giver is not assigned to themselves or their previous assignment
                giver_email = giver.get("email")
                receiver_email = receiver.get("email")
                prev_email = prev_assignments.get(giver_email)

                if giver == receiver or prev_email == receiver_email:
                    success = False
                    break
                assignments.append({
                    "Employee_Name": giver["name"],
                    "Employee_EmailID": giver["email"],
                    "Secret_Child_Name": receiver["name"],
                    "Secret_Child_EmailID": receiver["email"]
                })

            logger.info("Assignments generated successfully: %s", assignments)
            if success:
                return assignments

        logger.error("Failed to generate valid assignments after multiple attempts.")
        raise ValueError("Unable to generate valid assignments after multiple attempts.")
