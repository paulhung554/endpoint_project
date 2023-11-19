from typing import Union

from fastapi import FastAPI

from  random import randint


app = FastAPI()

#List of Employees 
employees = [{"id": 1, "name": "Ansel Mouse"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

print(randint(0, 99))

#print(random.randint(1, 100))  # Generates and displays a random integer between 0 and 99.
number =randint(0, 99)  # Stores the random number between 0 and 99 in the variable 'number'.
print(number)

@app.get("/random")
def get_random():
    number = randint(0, 99)
    return number

# HOMEWORK AFTER 2023-11-12

#1: Make a GET function that returns a random number between 0 and 99 
# HINT: Use google to search up how to gneerate random numbers between interval

#2 Make a Github account 

#3 Make a POST endpoint to save the id and name of an employee