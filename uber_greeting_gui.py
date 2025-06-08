import tkinter as tk
import datetime

# This is the function that builds your greeting
def generate_greeting():
    customer_name = name_entry.get()
    
    # Get current hour to decide greeting
    hour = datetime.datetime.now().hour
    if hour < 12:
        time_of_day = "Good Morning"
    elif hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"
    
    # Build the greeting
    greeting = (
        f"{time_of_day} {customer_name}. Your driver name is Michael. "
        "He has been assigned to pick you up and take you to your destination quickly and safely as possible. "
        "The vehicle you entered is a Ford Fusion with personal advertising on both sides. "
        "License plate SRZ9670. Please fasten your seatbelt for your safety. "
        "You were trusted with today's ride for a reason. Thank you for choosing Uber. "
        "Thank you for riding with me, Michael B your Uber partner."
    )
    
    # Show the greeting
    output_label.config(text=greeting)

# Build the window
window = tk.Tk()
window.title("Uber Greeting App")

# Where you type the customer name
name_label = tk.Label(window, text="Enter Customer Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

# The button you press to create the greeting
generate_button = tk.Button(window, text="Generate Greeting", command=generate_greeting)
generate_button.pack()

# Where the greeting will show
output_label = tk.Label(window, text="", wraplength=400, justify="left")
output_label.pack()

# Keep the window open
window.mainloop()
