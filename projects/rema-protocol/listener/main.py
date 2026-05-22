from router import execute_command


print("REMA Listener Started")

while True:
    text = input("VOICE > ")

    execute_command(text)