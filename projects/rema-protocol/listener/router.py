import subprocess


def execute_command(command):
    command = command.lower()

    if "ema despierta" in command:
        subprocess.run(
            ["rema", "ema", "start"]
        )

        print("EMA START SIGNAL")

    elif "ema duerme" in command:
        subprocess.run(
            ["rema", "ema", "stop"]
        )

        print("EMA STOP SIGNAL")

    else:
        print("UNKNOWN COMMAND")