# IS 3020 Final Project

## Student and Project Information

- Student name: Westby Slade
- GitHub username: WestbySlade
- Project title: EzBudget
- Application purpose: This application tracks your expenses and income to make for a lightweight budgeting app. It also tracks categories and goals you are saving for.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.
I am running Python 3.14 using PyCharm 2026.1.2. To start the application simply unpack the zip, locate the EzBudget.py file, and click run at the top.

## Major Features

List the major user-facing features implemented in the final application.
load_data(): Checks if finance_data.csv exists and reads existing transaction records into memory, or initializes a new file with header columns if absent.

save_data(): Writes all current transaction records in memory back to finance_data.csv using header fields.

input_budget(): Prompts the user to set or update their target dollar budget limit with input validation against negative numbers and non-numeric inputs.

add_transaction(): Gathers input for a new income or expense item, appends it to the global transaction list, and evaluates immediate budget impact.

view_summary(): Displays total income, total expense, net balance, target budget status, and budget progress.

view_transactions(): Prints every recorded transaction line by line or notifies the user if no records exist.

view_category(): Prompts for a specific category name and filters transactions to display matching records and their net total.

view_category_breakdown(): Groups all expenses by category, calculates each category's share of total spending, and displays a sorted visual distribution table.
    This feature was coded by AI as an additional feature that I wanted to throw on at the end.

main(): Runs the central application menu loop, handling navigation between options and managing startup data loading and shutdown saving.

## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

As this was coded in python, there are obviously alot of python concepts used.

File handling - open() and csv.DictReader/csv.DictWriter reads and write directly onto the data csv file.
Data Structures - Uses lists to maintain and organized file. 
Error - Uses several try, except, and ValueError clauses to reprompt the user.
Control Loops - while True, break, if, elif, and else are all used.
Formatting - .lower used to bypass possible case-sensitive matchings.

## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.
finance_data.csv holds the user input under the columbs: Date,Type,Amount,Category,and Description. 
It loads up automatically and saves at the end.


## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.
I went through and added a ton of inputs to have it summarize and test all of the options. 
Some errors include wrong variable type, like a string when a float is required in addition to other similar user-error inputs.

## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
AI was used to help explain when I got stuck coding part 1.
For part 2, AI was used to edit and add an additional feature.