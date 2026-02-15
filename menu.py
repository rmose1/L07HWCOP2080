# menu.py

from run_bash_cmd_function import run_bash_cmd


class Menu:
    """
    Menu class that displays Linux utility options
    and processes user input.
    """

    def __init__(self):
        """
        Constructor initializes empty list of options.
        """
        self._options = []

    def addOption(self, option):
        """
        Adds a menu option to the options list.
        """
        self._options.append(option)

    def displayMenu(self):
        """
        Displays the menu options.
        """
        print("\n===== Linux Utilities Menu =====")

        for index, option in enumerate(self._options, start=1):
            print(f"{index}. {option}")

        print("4. Quit (or Q)")

    def getInput(self):
        """
        Collects and validates user input.
        """

        while True:
            self.displayMenu()
            user_input = input("Enter choice (1-4): ")

            if user_input.lower() == 'q' or user_input == '4':
                print("Exiting program...")
                break

            try:
                choice = int(user_input)

                if 1 <= choice <= len(self._options):
                    run_bash_cmd(choice)
                else:
                    print("Invalid selection. Please enter 1-4.")

            except ValueError:
                print("Invalid input. Please enter a number 1-4 or Q to quit.")