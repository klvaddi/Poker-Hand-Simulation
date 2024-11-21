# Poker-Hand-Simulation
Find the experimental probability of poker hands at showdown (taking the best 5 cards out of the 7 available cards). The occurence and percentage of each hand type will be displayed.  
## To Run
Using your command line, navigate to the project directory and run:
```bash
python3 poker_main.py
```
Enter how many trials you want to run.
## Unit Testing
Install pytest (if not already installed):
```bash
pip3 install pytest
```
Navigate to the project directory and run:
```bash
python3 -m pytest
```
25 tests (2-3 for each function in poker_functions.py) will be run using multiple predefined hands of 7 cards. If a function's output matches the expected result, that test will pass.
## What I Learned
- Enhanced skills in writing modular and reusable code in Python
- Learned how to write unit tests using pytest to ensure code reliability
- Explored more efficient solutions to reduce runtime of large simulations
