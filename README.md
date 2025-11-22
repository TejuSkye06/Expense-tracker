# Expense-tracker
A basic console-driven daily expense tracker. Users can add entries with expense amount, category, and description. The application saves entries, displays totals, highlights the biggest expense, and shows summaries by category apply simple programming techniques.

Problem Statement:
People usually spend small amounts of cash each day without realizing where they spend it. This creates overspending and a lack of awareness regarding money matters. A quick and simple tool aimed at tracking those expenses can help reveal the bigger picture regarding day to day spending.

Objectives:
1) Record individual expenses
2) Categorize each entry
3) Display all individual expenses
4) Calculate total spending
5) Display cumulative spending by category
6) Identify the single highest expense
7) Display in a clean, menu-driven interface.

Key Features:
1) Add an expense with amount, category, and description
2) View all expenses in categorical, tabular format
3) Calculate total spending
4) Summarize spending by category
5) Determine highest expense
6) Modify entry with easy-to-read menus
7) File structure is Modular for easy readability and function

Programming Concepts/Objects Used:
1) Lists
2) Dictionaries
3) functions
4) Loops
5) Conditionals
6) Basic modular design
7) Input/Output handling

Algorithm Summary:-

Add Expense:
- Prompt the user for the amount
- Prompt the user for a category
- Prompt the user for a description
- Save all in a dictionary
- Append the dictionary to a list

Total Spending:
- Loop through all expenses
- Sum the amounts
- Display the total

Category Summary:
- Create an empty dictionary
- Loop through expenses
- Add amounts for categories

Highest Expense:
- Get the maximum amount
- Display details

Project Structure:-

-ExpenseTracker/
- expense_tracker.py
- README.md
- screenshots/
- (Images showing program output)
- recordings
- Display the results

How to Run:-
- Install Python (3.x recommended).
- Open a terminal/command prompt.
- Navigate to the project folder.
- Run:
    python expense_tracker.py

Summary

This project utilizes basic programming concepts to develop a simple, yet effective tool for tracking daily expenditures. Crucially, it illustrates the entire development process, from identifying a real-world problem, to design, application, and testing of the working program
