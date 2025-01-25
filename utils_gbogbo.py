"""
Module: utils_gbogbo

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytic company Gbogbo Analytics. 
When we work hard to write useful code, we want it to be reusable and that is what Gbogbo Analytics does best.
A good byline ensure the great quality work that is done here at Gbogbo Analytics to maintain customer satisfaction.

Author: Elom Gbogbo

"""
#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_international_clients: bool = True
is_privately_held: bool = False

# declare an integer variable 
years_in_operation: int = 10
number_of_employees: int = 6

# declare a floating point variable
average_client_satisfaction: float = 4.7
average_employee_satisfaction: float = 4.1

# declare a list of strings
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
tools_used: list = ["SQL", "GitHub", "Python"]

# declare a list of numbers so we can illustrate statistics skills
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
employee_satisfication_scores: list = [4.0, 4.0, 3.3, 4.2, 5.0, 3.9]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_score_employee: float = min(employee_satisfication_scores)  
max_score_employee: float = max(employee_satisfication_scores)  
mean_score_employee: float = statistics.mean(employee_satisfication_scores)  
stdev_score_employee: float = statistics.stdev(employee_satisfication_scores)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Gbogbo Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:    {has_international_clients}
Is Privately Held:            {is_privately_held}
Years in Operation:           {years_in_operation}
Number of Employees:          {number_of_employees}
Skills Offered:               {skills_offered}
Tools Used:                   {tools_used}
Client Satisfaction Scores:   {client_satisfaction_scores}
Employee Satisfaction Scores: {employee_satisfication_scores}
Minimum Satisfaction Score:   {min_score}
Maximum Satisfaction Score:   {max_score}
Minimum Satisfaction Score for Employees: {min_score_employee}
Maximum Satisfaction Score for Employees: {max_score_employee}
Mean Satisfaction Score:       {mean_score:.2f}
Mean Satisfaction Score for Employees: {mean_score_employee}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
Standard Deviation of Employee Satisfaction Scores: {stdev_score_employee}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()


