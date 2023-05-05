"""
algorithm:
get name
display"(H)ello,(G)oodbye,(Q)uit"
get choice
while choice !="Q"
    if choice == "H"
        display "Hello {name}"
    elif choice == "G"
        display "Goodbye {name}
    else:
        display"invalid choice"
     display"(H)ello,(G)oodbye,(Q)uit"
    get choice
display "finished"
"""
name= input("what is your name:")
print("(H)ello\n(G)oodbye\n(Q)uit\n")
choice=str(input(">>>")).title()
while choice !="Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    choice = str(input(">>>")).title()
print("finished")