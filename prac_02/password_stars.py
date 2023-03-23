PASSWORD= "duck"
code= input("what is your password:")
while code != PASSWORD:
    print("invalid")
    code = input("what is your password:")
print("Welcome back duck")