
'''
Додаток, який буде працювати з книгою контактів та календарем

1) Зберігати ім'я та номер телефону
2) Знаходити номер телефону за ім'ям
3) Змінювати записаний номер телефону
4) Виводити в консоль всі записи, які збереглись

{"name": "John", "phone": "80977333967"}

'''

contacts = {}
contacts_file = "contacts.txt"

commands = """
1) add [name] [number] - to add a new contact
2) change [name] [new number] - to change old phone number
3) phone [name] - to print name 
4) all - will show all number from the contacts
5) exit - to exit the application
"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "User not found."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    save_contacts()
    return f"Contact {name} added"

def save_contacts():
    with open(contacts_file, 'w') as file:
        for name, phone in contacts.items():
            file.write(f'{name}: {phone}\n')

def read_contacts():
    contacts = {}
    try:
        with open(contacts_file, 'r') as file:
            for line in file:
                name, phone = line.strip().split(': ')
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

@input_error
def change_contact(args):
    name, phone = args
    contacts[name] = phone
    save_contacts()
    return f"Contact {name} update"

@input_error
def show_phone(args):
    name = args[0]
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return 'Contact list is empty.'
    return "\n".join(f'{name}: {phone}' for name, phone in contacts.items())



def main():
    global contacts
    contacts = read_contacts()
    print ("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print (show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()