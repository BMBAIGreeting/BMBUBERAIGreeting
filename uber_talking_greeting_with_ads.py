import tkinter as tk
import datetime
import pyttsx3  # Voice engine
import random  # For random ad picking

# Initialize voice engine
engine = pyttsx3.init()

# Ads list
ads = [
    "Today’s sponsor: CAR’isma Wash — professional car wash services with multiple locations across Houston. Open daily from 8 a.m. to 8 p.m. Visit carismawash.com for details."
    # Add more ads here as you grow!
]

# Function to generate and speak greeting and ad
def generate_message():
    customer_name = name_entry.get()

    # Build time-based greeting
    hour = datetime.datetime.now().hour
    if hour < 12:
        time_of_day = "Good Morning"
    elif hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"

    greeting = (
        f"{time_of_day} {customer_name}. Your driver name is Michael. "
        "He has been assigned to pick you up and take you to your destination quickly and safely as possible. "
        "The vehicle you entered is a Ford Fusion with personal advertising on both sides. "
        "License plate SRZ9670. Please fasten your seatbelt for your safety. "
        "You were trusted with today's ride for a reason. Thank you for choosing Uber. "
        "Thank you for riding with me, Michael B your Uber partner."
    )

    full_message = ""

    # Check if greeting is selected
    if greeting_var.get():
        full_message += greeting + " "

    # Check if ad is selected
    if ad_var.get():
        selected_ad = random.choice(ads)
        full_message += selected_ad

    # Display the message
    output_label.config(text=full_message)

    # Speak the message
    if full_message:
        engine.say(full_message)
        engine.runAndWait()

# Build the window
window = tk.Tk()
window.title("Uber Talking Greeting App - With Ads")

# Make the window bigger
window.geometry("700x500")

# Where you type the customer name
name_label = tk.Label(window, text="Enter Customer Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Checkboxes for Greeting and Ads
greeting_var = tk.BooleanVar()
ad_var = tk.BooleanVar()

greeting_checkbox = tk.Checkbutton(window, text="Play Greeting", variable=greeting_var)
greeting_checkbox.pack(pady=5)

ad_checkbox = tk.Checkbutton(window, text="Play Advertisement", variable=ad_var)
ad_checkbox.pack(pady=5)

# The button you press to create the greeting/ad
generate_button = tk.Button(window, text="Generate Message", command=generate_message)
generate_button.pack(pady=10)

# Where the message will show
output_label = tk.Label(window, text="", wraplength=650, justify="left")
output_label.pack(pady=20)

# Keep the window open
window.mainloop()
