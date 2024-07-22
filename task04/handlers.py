from decorators import input_error

def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return "No such name in contacts."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]
    return f"{name}: {contacts[name]}"

def show_all(contacts: dict[str, str]) -> str:
    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def show_help():
    return """
        Available commands:\n
        hello - Display a greeting message.\n
        add username phone - Add a new contact with the specified phone number.\n
        change username phone - Change the phone number for an existing contact.\n
        phone username - Display the phone number for the specified contact.\n
        all - Display all saved contacts with their phone numbers.\n
        close, exit - Exit the bot with a goodbye message.\n
        help - Display this help message.
        """
