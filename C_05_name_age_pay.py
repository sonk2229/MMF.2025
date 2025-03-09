# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - Please enter an number more than zero."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


# main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")