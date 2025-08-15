"""Demo module with an intentional bug and a fixed function.

Contains:
- say_hello_buggy(name): intentionally broken to demonstrate a bug
- say_hello_fixed(name): corrected version using colorama for colored output
"""

# Intentional minimal dependency on colorama

def say_hello_buggy(name):
    """Intentional bug: missing the 'name' argument in format() call.

    Also demonstrates a poor use of colorama by not calling init(), but
    the primary bug is the format call without the required value.
    """
    from colorama import Fore
    # Bug: forgetting to supply `name` to format()
    print(Fore.GREEN + "Hello, {}!".format() + Fore.RESET)


def say_hello_fixed(name):
    """Fixed version: correctly formats the string and initializes colorama.
    """
    from colorama import init, Fore, Style
    init(autoreset=True)
    print(Fore.GREEN + f"Hello, {name}!" + Style.RESET_ALL)
