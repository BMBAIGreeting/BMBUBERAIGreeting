import tkinter as tk
import datetime
import pyttsx3
import random

# Initialize voice engine
engine = pyttsx3.init()

# Full Business Ad Inventory by Profile
ad_inventory = {
    "Truck Driver": [
        "Today's sponsor: Charity Ray Dispatch — reliable truck dispatch service for owner operators, hotshots, reefers, flatbeds, and over-the-road drivers. Get the loads you need, wherever you are. Call today to grow your trucking business."
    ],
    "Nurse": [
        "Today's sponsor: Lisa's Scrubs — professional scrubs and medical uniforms. Visit lisasscrubs.com for specials."
    ],
    "Tourist / Visitor": [
        "Today's sponsor: Taste Houston BBQ — real Texas barbecue. Visit tastehoustonbbq.com to find a location near you.",
        "Today's sponsor: Houston Galleria Mall — top shopping destination in Texas."
    ],
    "Business Traveler": [
        "Today's sponsor: Priority Conference Center — host your next meeting with professional accommodations. Visit priorityconference.com.",
        "Today's sponsor: Executive Rentals Houston — luxury vehicles and lodging for your business trip."
    ],
    "Local Rider": [
        "Today's sponsor: CAR’isma Wash — professional car wash services with multiple locations across Houston. Open daily from 8 a.m. to 8 p.m. Visit carismawash.com for details.",
        "Today's sponsor: Priority Roofing of Houston — storm restoration specialist Damian Hunter. Contact 631-827-1782 or visit priorityroofs.com.",
        "Today's sponsor: Sal's Auto Glass — expert automotive glass replacement. Call 713-259-6415 for fast service.",
        "Today's sponsor: Ant's Auto Care — honest, reliable, professional auto care. Call 713-382-1998.",
        "Today's sponsor: T.H. Remodeling — specializing in remodeling, electrical, plumbing, windows, and more. Call 832-526-4550 or 832-403-8386.",
        "Today's sponsor: A and I Flooring — flooring experts in Houston and Jersey City. Call 713-485-9169 or visit houstonfloorexpert.com for free estimates."
    ],
    "Houston Visitor": [
        "Today's Houston Guide: Try The Pit Room for BBQ, visit the Galleria Mall for shopping, check out Discovery Green Park, and don’t miss the Houston Rodeo if in season!"
    ]
}

# Motivational message
motivation = "Keep pushing. Every step forward builds your future. Stay focused. Keep building."

# Function to generate and speak message
def generate_message():
    customer_name = name_entry.get()
    profile = profile_var.get()

    # Time-based greeting
    hour = datetime.datetime.now().hour
    if hour < 12:
        time_of_day = "Good Morning"
    elif hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"

    greeting = (
        f"{time_of_day} {customer_name}. Your driver name is Michael. "
        "Vehicle: Ford Fusion. License plate SRZ9670. "
        "Please fasten your seatbelt. Your safety is our number one priority."
    )

    closing = (
        "Thank you for choosing Uber. Thank you for riding with me. Michael B, your Uber partner."
    )

    full_message = ""

    if greeting_var.get():
        full_message += greeting + " "

    full_message += motivation + " "

    if ad_var.get() and profile in ad_inventory:
        selected_ad = random.choice(ad_inventory[profile])
        full_message += selected_ad + " "

    full_message += closing

    output_label.config(text=full_message)

    if full_message:
        engine.say(full_message)
        engine.runAndWait()

# Build the app window
window = tk.Tk()
window.title("Uber Talking Greeting App - BMB AI Engine 3.0 City Guide")
window.geometry("850x700")

# Customer Name Input
name_label = tk.Label(window, text="Enter Customer Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Profile Selector (AI Logic Starter)
profile_label = tk.Label(window, text="Select Customer Profile:")
profile_label.pack(pady=5)

profile_var = tk.StringVar(window)
profile_var.set("Local Rider")  # Default value

profile_options = ["Truck Driver", "Nurse", "Tourist / Visitor", "Business Traveler", "Local Rider", "Houston Visitor"]
profile_menu = tk.OptionMenu(window, profile_var, *profile_options)
profile_menu.pack(pady=5)

# Checkboxes for Greeting & Ads
greeting_var = tk.BooleanVar()
ad_var = tk.BooleanVar()

greeting_checkbox = tk.Checkbutton(window, text="Play Greeting", variable=greeting_var)
greeting_checkbox.pack(pady=5)

ad_checkbox = tk.Checkbutton(window, text="Play Advertisement", variable=ad_var)
ad_checkbox.pack(pady=5)

# Generate Message Button
generate_button = tk.Button(window, text="Generate Message", command=generate_message)
generate_button.pack(pady=10)

# Output Display
output_label = tk.Label(window, text="", wraplength=800, justify="left")
output_label.pack(pady=20)

# Keep window open
window.mainloop()
