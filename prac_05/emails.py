"""
This program will get a user input email,
ask if the name before the @ is the correct name
if not the user will input the correct name and it will be stored.
"""


def main():
    email_and_name_dict = {}
    # Get user input email
    email = input("Enter your email: ")

    while email != "":
        name = get_name_from_email(email)
        # Check if the name before the @ is correct
        check_name = input("Is this your name: {}? (Y/n) ".format(name))
        if check_name.upper() != "Y" and check_name != "":
            # If name is incorrect get the user to input the correct name
            name = input("Enter you name: ")
        email_and_name_dict[email] = name
        email = input("Enter your email: ")
    # Print the name followed by email for each email stored
    for email, name in email_and_name_dict.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    # Function to get the name from the email string
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
