"""
This module defines the Employee class, which represents an employee with a name and email.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Employee:
    """Represents an employee with a name and email."""
    name: str
    email: str
