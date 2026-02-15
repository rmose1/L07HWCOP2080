# main.py

from menu import Menu


def main():
    """
    Public interface for the Linux Utilities Menu application.
    """

    menu = Menu()

    # Add Linux utility options
    menu.addOption("Show Current Date")
    menu.addOption("Show System Uptime")
    menu.addOption("Show Memory Usage")

    # Start menu interaction
    menu.getInput()


if __name__ == "__main__":
    main()