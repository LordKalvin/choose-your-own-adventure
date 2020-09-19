from os import system

TITLE = "CHOOSE YOUR OWN ADVENTURE (IN PYTHON)"

def clear():
    system("clear")

def exit():
    system("exit")

def welcome_screen():
    print("\n" + TITLE)
    print("--" * 19)
    print("Welcome traveller. Your adventure should you accept is perilous\nand fraught with danger. Legend speaks of a brave traveller who\nwill be sent by the gods to help us in our time of need.\nAre you that brave traveller the legends speak of?")
    print("1. Yes\n2. No, thank you!")

def get_answer():
    answer = str(input("\nAnswer (1/2/3/4....) : "))
    return answer


welcome_screen()
answer = get_answer()

if answer == "1":
    pass
elif answer == "2":
    clear()
    print("Thats too bad. Goodbye!")
    print("1. Goodbye.\n2. No, wait. I am!")
    answer = get_answer()
    if answer == "1":
        exit()
    else:
        pass
