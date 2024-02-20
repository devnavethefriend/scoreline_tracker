import json
import os

# Constants
DATA_FILE = "scorelines.json"
MAX_SCORES = 5

def save_data(data):
    """
    Save data to a JSON file.

    Args:
        data (list): The list of scorelines to save.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def load_data():
    """
    Load data from the JSON file.

    Returns:
        list: The list of scorelines loaded from the file, or an empty list if the file doesn't exist.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def calculate_mean(data):
    """
    Calculate the mean value of the scorelines.

    Args:
        data (list): The list of scorelines.

    Returns:
        float: The mean value of the scorelines.
    """
    if data:
        return sum(data) / len(data)
    else:
        return 0

def enter_scorelines(data):
    """
    Prompt the user to enter scorelines and add them to the data.

    Args:
        data (list): The list of scorelines.
    """
    if len(data) < MAX_SCORES:
        scores = input("Enter Scorelines (two space-separated values): ")
        try:
            line1, line2 = map(float, scores.split())
            data.append(line1 + line2)
            print("Done! Scorelines added.")
            print(str(len(data)) + " Added...")
            return enter_scorelines(data)
        except ValueError:
            print("Invalid input. Please enter two numeric values separated by space.")
    else:
        print("Maximum number of scorelines reached.")

def display_results(data):
    """
    Display the list of scorelines and their mean value.

    Args:
        data (list): The list of scorelines.
    """
    if data:
        print("Result List:", data)
        print("Mean Value:", calculate_mean(data))
    else:
        print("Result List is empty.")

def reset_data():
    """
    Reset the data by clearing the list of scorelines.

    Returns:
        list or None: The empty list if data reset is confirmed, or None if reset is canceled.
    """
    confirmation = input("Are you sure you want to reset the result list? (yes/no): ")
    if confirmation.lower() == "yes":
        return []
    else:
        print("Reset canceled.")
        return None

def main():
    """
    Main function to run the program.
    """
    data = load_data()
    while True:
        print("\nMenu:")
        print("1. Enter Scorelines")
        print("2. Display Results")
        print("3. Reset Data")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            enter_scorelines(data)
        elif choice == "2":
            display_results(data)
        elif choice == "3":
            data = reset_data()
            if data is not None:
                save_data(data)
        elif choice == "4":
            save_data(data)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
