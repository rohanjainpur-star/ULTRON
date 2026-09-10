count =1 
while count<= 10:
    print("ULTRON")
    count += 1
def add(a,b):
    return a + b
result=add(10,20)
print(result)
my_dictionary ={"hello": "hello sir",
                "status": "All sysyems are operational",
                "help": "Avilable commands"
    }
command = input("Command: ").strip().lower()

response = my_dictionary.get(command, "I don't understand that command")

print(response)