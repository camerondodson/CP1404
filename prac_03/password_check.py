def main():

MINIMUM_LENGTH = 5


def get_password():
    global password
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Enter password: ")


get_password()


def print_asterisks():
    print('*' * len(password))


print_asterisks()

main()
