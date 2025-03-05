# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main Routine goes here
make_statement("Instructions", "❗")

# Functions go here


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enters the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "❕")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket
sales information and write the data tom a text file.

It will also choose one lucky ticket holder who wins the
 draw (their ticket is free).
 
    ''')

# Main routine goes here
# payment_ans = ['cash', 'credit']


while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()


# pay_method = string_check("Payment method: ", payment_ans, 2)
# print(f"You chose {pay_method}")
