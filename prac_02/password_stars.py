def main():
    PASSWORD = "duck"
    code = get_password()
    while code != PASSWORD:
        print("invalid")
        code = get_password()
    print("Welcome back sir duck")


def get_password():
    code = input("what is your password:")
    return code


main()
