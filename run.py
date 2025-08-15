from app.say_hello import say_hello_buggy, say_hello_fixed


def main():
    print("Running buggy version:")
    try:
        say_hello_buggy("Alice")
    except Exception as e:
        print("Buggy failed with:", repr(e))

    print("\nRunning fixed version:")
    say_hello_fixed("Alice")


if __name__ == "__main__":
    main()
