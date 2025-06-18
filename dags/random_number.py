"""
## Random Number Generator DAG

This DAG demonstrates the use of Airflow's TaskFlow API to:
1. Generate a random number
2. Check if the number is even or odd
3. Print the results

The DAG uses the TaskFlow API's automatic XCom feature to pass data between tasks.
"""

from airflow.decorators import dag, task
from pendulum import datetime
import random

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["random_number"],
    description="A simple DAG that generates and checks a random number"
)
def random_number_dag():
    
    @task
    def generate_random_number() -> int:
        """
        Generates a random number between 1 and 100
        """
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number
    
    @task
    def check_number(number: int) -> None:
        """
        Checks if the number is even or odd and prints the result
        """
        if number % 2 == 0:
            print(f"The number {number} is even!")
        else:
            print(f"The number {number} is odd!")

    # Define the task dependencies
    number = generate_random_number()
    check_number(number)

# Instantiate the DAG
random_number_dag()
