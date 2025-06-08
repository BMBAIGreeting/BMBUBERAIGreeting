import tkinter as tk
import datetime
import pyttsx3
import random

# Initialize voice engine
engine = pyttsx3.init()

# Full Business Ad Inventory
ads = [
    "Today's sponsor: CAR’isma Wash — professional car wash services with multiple locations across Houston. Open daily from 8 a.m. to 8 p.m. Visit carismawash.com for details.",
    "Today's sponsor: Priority Roofing of Houston — storm restoration specialist Damian Hunter. Contact 631-827-1782 or visit priorityroofs.com.",
    "Today's sponsor: Sal's Auto Glass — expert automotive glass replacement. Call 713-259-6415 for fast service.",
    "Today's sponsor: Ant's Auto Care — honest, reliable, professional auto care. Call 713-382-1998.",
    "Today's sponsor: T.H. Remodeling — specializing in remodeling, electrical, plumbing, windows, and more. Call 832-526-4550 or 832-403-8386.",
    "Today's sponsor: A and I Flooring — flooring experts in Houston and Jersey City. Call 713-485-9169 or visit houstonfloorexpert.com for free estimates.",
    "Today's sponsor: Charity Ray Dispatch — reliable truck dispatch service for owner operators, hotshots, reefers, flatbeds, and over-the-road drivers. Get the loads you need, wherever you are. Call today to grow your trucking business."
]

# Motivational message
motivation = "Keep pushing. Every step forward builds your future. Stay focused. Keep building."

# Function to generate and speak message
def generate_message():
    customer_name = name_entry.get()

    # Time-based greeting
    hour = datetime.datetime.now().hour
    if hour < 12:
        time_of_day = "Good Morning"
    elif hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"

    # Build greeting
    greeting = (
        f"{time_of_day} {customer_name}. Your driver name is Michael. "
        "Vehicle: Ford Fusion. License plate SRZ9670. "
        "Please fasten your seatbelt. Your safety is our number one priority."
    )

    # Thank you message
    closing = (
        "Thank you for choosing Uber. Thank you for riding with me. Michael B, your Uber partner."
    )

    full_message = ""

    if greeting_var.get():
        full_message += greeting + " "

    # Add motivational message every time
    full_message += motivation + " "

    if ad_var.get():
        selected_ad = random.choice(ads)
        full_message += selected_ad

    full_message += " " + closing

    output_label.config(text=full_message)

    if full_message:
        engine.say(full_message)
        engine.runAndWait()

# Build the app window
window = tk.Tk()
window.title("Uber Talking Greeting App - BMB Business Engine 1.0")
window.geometry("750x600")

# Input fields
name_label = tk.Label(window, text="Enter Customer Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Customer controls
greeting_var = tk.BooleanVar()
ad_var = tk.BooleanVar()

greeting_checkbox = tk.Checkbutton(window, text="Play Greeting", variable=greeting_var)
greeting_checkbox.pack(pady=5)

ad_checkbox = tk.Checkbutton(window, text="Play Advertisement", variable=ad_var)
ad_checkbox.pack(pady=5)

# Generate button
generate_button = tk.Button(window, text="Generate Message", command=generate_message)
generate_button.pack(pady=10)

# Output text area
output_label = tk.Label(window, text="", wraplength=700, justify="left")
output_label.pack(pady=20)

# Keep app running
window.mainloop()
