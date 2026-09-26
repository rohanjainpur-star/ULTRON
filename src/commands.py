from datetime import datetime
import platform
import ast
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
def help_command(commands):
    print("ULTRON: Available commands :")
    for cmd in commands:
        print(f"- {cmd}")       
def greet_user(name):
    print(f"ULTRON: Hello, {name.title()} Sir.")
def echo(argument):
     print(argument)
def calculate(argument):
    try:
        tree = ast.parse(argument, mode="eval")
        if isinstance(tree.body, ast.BinOp):
            operator = tree.body.op
            allowed_operators = (ast.Add, ast.Sub, ast.Mult, ast.Div)

            if isinstance(operator, allowed_operators):
                left = tree.body.left
                right = tree.body.right
                left_value = left.value
                right_value = right.value

                if isinstance(operator, ast.Add):
                    result = left_value + right_value
                elif isinstance(operator, ast.Sub):
                    result = left_value - right_value
                elif isinstance(operator, ast.Mult):
                    result = left_value * right_value
                elif isinstance(operator, ast.Div):
                    result = left_value / right_value

                print(f"ULTRON: {result}")
        else:
            print("ULTRON: Please enter valid calculation.")
    except ZeroDivisionError:
        print("ULTRON: Cannot divide by zero.")
def goodbye():
    print("ULTRON: Goodbye, Sir.")
def system_info():
    operating_system = platform.system()
    print(f"ULTRON: Operating System: {operating_system}")
    python_version = platform.python_version()
    print(f"ULTRON: Python Version: {python_version}")
    processor = platform.processor()
    print(f"ULTRON: Processor: {processor}")