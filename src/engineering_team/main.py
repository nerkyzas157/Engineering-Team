#!/usr/bin/env python
import sys
import warnings
import os
from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

os.makedirs("output", exist_ok=True)

# Demo
project_name = "Trading Simulation Platform"
user_requirements = """
Users can sign up, get virtual money, and practice trading stocks or crypto.
Shows portfolio balance, trade history, and current prices.
Works on mobile and desktop.
Leaderboard and learning tips.
Secure, easy to use, no real money involved.
"""

########################## Uncomment to enable user input ##########################
# project_name = input("Enter the name of the project:\n")
# requirements = input("Enter the requirements for the project:\n")
# if ".py" not in module_name:
#     module_name += ".py"


def run():
    """
    Run the research crew.
    """
    inputs = {
        "project_name": project_name,
        "user_requirements": user_requirements,
        "module_name": f"{project_name.replace(" ", "_").lower()}.py",
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
