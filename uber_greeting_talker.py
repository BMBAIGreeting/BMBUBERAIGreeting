import pyttsx3
import random
import datetime

# List of motivational quotes
motivational_quotes = [
    "Every journey begins with a decision to move forward.",
    "You were trusted with today’s ride for a reason.",
    "Stay focused. Stay positive. Stay safe.",
    "Each day brings new opportunities to grow and shine.",
    "Your steps today are building your future tomorrow."
]

# Function to automatically detect time of day
def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 18:
        return "Afternoon"
    else:
        return "Evening"

# Function to read customer list from file
def load_customers():
    try:
        with open("customers.txt", "r") as file:
            customers = [line.strip() for line in file.readlines()]
        return customers
    except FileNotFoundError:
        print("Customer file not found.")
        return []

# Function to generate the greeting message
def generate_greeting(customer_name):
    time_of_day = get_time_of_day()
    quote = random.choice(motivational_quotes)
    greeting = (f"Good {time_of_day} {customer_name}. Your driver name is Michael. "
                "He has been assigned to pick you up and take you to your destination quickly and safely as possible. "
                "The vehicle you entered is a Ford Fusion with personal advertising on both sides. "
                "License plate SRZ9670. Please fasten your seatbelt for your safety. "
                f"{quote} "
                "Thank you for choosing Uber. Thank you for riding with me, Michael B your Uber partner.")
    return greeting

# Function to speak the greeting message
def speak_greeting(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Main function to run everything
def main():
    customers = load_customers()
    if not customers:
        print("No customers loaded. Exiting program.")
        return

    print("Today's Customer List:")
    for i, customer in enumerate(customers, 1):
        print(f"{i}. {customer}")

    try:
        choice = int(input("Select customer by number: "))
        if 1 <= choice <= len(customers):
            selected_customer = customers[choice - 1]
            greeting = generate_greeting(selected_customer)
            print("\nGenerated Greeting:\n")
            print(greeting)
            speak_greeting(greeting)
        else:
            print("Invalid selection. Please choose a valid customer number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
