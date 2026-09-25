from commands import greet,status,greet_user, help_command , show_time , show_date,echo,goodbye,system_info
from constants import GREETING_COMMANDS, STATUS_COMMANDS, EXIT_COMMANDS
from constants import GOODBYE_COMMANDS
COMMAND_ALIASES = {
    "hi": "hello",
    "hey": "hello",
    "greetings": "hello",
}
COMMAND_HANDLERS = {
    "hello": greet,
    "echo": echo,
    "status": status,
    "help": help_command,
    "commands": help_command,
    "time": show_time,
    "date": show_date,
    "system": system_info,
    "goodbye": goodbye,
    "see you later": goodbye,
    "farewell": goodbye,
}
def handle_command(user_command):
    parts = user_command.split()
    
    if len(parts) == 0:
        return False
    
    command = parts[0]
    argument = " ".join(parts[1:])
    if user_command in COMMAND_HANDLERS:
        handler = COMMAND_HANDLERS[user_command]
        handler()
        return False
    if command == "hello" and len(parts) > 1:
        name = " ".join(parts[1:])
        greet_user(name)
        return False
    if command == "help" or command == "commands":
        help_command(COMMAND_HANDLERS.keys())
        return False
    
    handler = COMMAND_HANDLERS.get(command)
    if handler:
        if argument:
            handler(argument)
        else:
            handler()
        return False
    
    
    elif command == "exit":
        print("ULTRON: Shutting down")
        return True
    
    else:
        print("I don't understand that command")
        return False
while True:
    user_command = input("You:").strip().lower()
    parts = user_command.split()
    should_exit = handle_command(user_command)
    if should_exit:
        break