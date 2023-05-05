EMAILS = {}


def main():
    email = validate_email()
    user_name = name_processing(email)
    while email != "":
        choice = input(f'Is your name {user_name}? (Y/n)').upper()
        if choice == "Y":
            EMAILS[email] = user_name
        else:
            modified_name = input("Name: ")
            EMAILS[email] = modified_name
        email = validate_email()
        user_name = name_processing(email)

    for email in EMAILS:
        print(f"{EMAILS[email]} ({email})")


def name_processing(email):
    "this will process the user email to identify their username"
    name = email.split('@')[0]
    name_parts = name.split('.')
    name_parts = [part.title() for part in name_parts]
    name = ' '.join(name_parts)
    return name


def validate_email():
    "this will check if the email is valid or not"
    email = input("Email:")
    if email == "":
        return email
    while '@' not in email:
        print("This is not a valid email,please try again")
        email = input("Email:")
    return email


main()
