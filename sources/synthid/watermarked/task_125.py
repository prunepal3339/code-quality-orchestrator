 Design a program in python that allows users access specific resources base on user input

# Define the available resources and their corresponding access functions
resources = {
    "resource1": lambda: print("Accessing Resource 1"),
    "resource2": lambda: ("Accessing Resource", "2"),
    "secret_resource": lambda: "This is a secret message",
}

def main():
    while True:
        # Display available resources
        print("Available Resources:")
        for resource in resources.keys():
            print(f"- {resource}")

        # Get user input
        user_input = input("Enter the name of the resource you want to access (or 'exit' to quit): ").strip().lower()

        # Check if the user wants to exit
        if user_input == "exit":
            print("Exiting program.")
            break

        # Check the user's input and grant appropriate access
        if resources.get(user_input):
            result = resources[user_input]()
            print(result)
        else:
            print("Resource not found. Please try again.")

if __name__ == "__main__":
    main()
