from commands import greet,status,greet_user, help_command , show_time , show_date
from constants import GREETING_COMMANDS, STATUS_COMMANDS, EXIT_COMMANDS
from constants import GOODBYE_COMMANDS
COMMAND_HANDLERS = {
    "hello": greet,
    "hey": greet,
    "hi": greet,
    "status": status,
    "help": help_command,
    "commands": help_command,
    "time": show_time,
    "date": show_date,
}
def handle_command(user_command):
    if user_command.startswith("hello "):
        name = user_command[6:]
        greet_user(name)
        return False
    handler = COMMAND_HANDLERS.get(user_command)
    if handler:
        handler()
        return False
    
    
    elif user_command == EXIT_COMMANDS:
        print("ULTRON: Shutting down")
        return True
    elif user_command in GOODBYE_COMMANDS:
        print("ULTRON: Goodbye, Sir.")
        
    else:
        print("I don't understand that command")
        return False
while True:
    user_command = input("You:").strip().lower()
    parts = user_command.split()
    should_exit = handle_command(user_command)
    if should_exit:
        break