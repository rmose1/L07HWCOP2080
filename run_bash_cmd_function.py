# run_bash_cmd_function.py

import os

def run_bash_cmd(option):
    """
    Executes a Linux command based on the selected menu option.
    """

    commands = {
        1: "date",
        2: "uptime",
        3: "free -h"
    }

    command = commands.get(option)

    if command:
        os.system(command)
    else:
        print("Invalid option selected.")