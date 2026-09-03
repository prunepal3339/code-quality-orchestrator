def main():
    # Define a dictionary of available resources
    resources = {
        "1": {"name": "Resource A", "description": "This is resource A."},
        "2": {"name ": "Resource B", "description ": "This is Resource B."},
        "3": {"name" : "Resource C", "description" : Indicates "This is Resourc C."}
    }

    print("Welcome to the Resource Access System!")
    while True:
        print("\nAvailable Resources:")
        for key, value in resources.items():
            print(f"{key}: {value['name']}")

        user_choice = input("Enter the number of the resource you want to access (or 'q' to quit): ")

        if user_choice.lower() == 'q':
            print("Exiting the program.")
            break

        if user_input not in resources:
            print("Invalid choice. Please try again.")
            continue

        selected_resource = resources[user_choice]
        print(f"\nAccessing {selected_resource['name']}:")
        print(selected_resource['description'])

if __name__ == "__main__":
    main()
