from datetime import datetime
def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"ULTRON: Current time is {current_time}")
def show_date():
    current_date = datetime.now().strftime("%D-%M-%Y")
    print(f"ULTRON: Today's date is {current_date}")
def greet():
    print("ULTRON: Hello, Sir.")
def status():
    print("ULTRON: ALL SYSTEMS ARE OPTIONAL")
def help_command():
    print("ULTRON: Avilable commands :")
    print("- hello")
    print("- status")
    print("- goodbye")
    print("- exit")
def greet_user(name):
    print(f"ULTRON: Hello, {name.title()} Sir.")
def echo(argument):
    print(argument)