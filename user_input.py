#2. User Input Data Processor
# Objective: The aim of this assignment is to process 
# and format user input data.
# Task 1: Input Length Validator Write a script that 
# asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.
# Enter Github Link Here
# This question is manually scored. An instructor will submit 
# a score for your response after completion.

print("Welcome, please let us know who you are.")
first_name,last_name='',''

while len(first_name)<2:
    first_name=input("First Name:")
    if len(first_name)<2:
        print("Error! Must be at least two characters long!")

while len(last_name)<2:
    last_name=input("Last Name:")
    if len(last_name)<2:
        print("Error! Must be at least two characters long!")

print(f"Thank you for your input {first_name} {last_name}!")