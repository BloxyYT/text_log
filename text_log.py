import string
def log_input():
    while True:
        log_entry = input("Enter the log description: ")

        with open("log_file.txt", "a") as file:
            file.write(log_entry + "\n")

        print("Submitted!")

        choice = input("Enter 'L' for a new log input or 'E' to exit: ").upper()

        if choice == 'E':
            break
        elif choice != 'L':
            print("Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    log_input()
