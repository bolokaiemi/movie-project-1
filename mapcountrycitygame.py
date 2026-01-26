import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COUNTRIES = {
    "India": {
        "cities": ["Mumbai", "Bangalore", "Delhi"],
        "map": "maps/india.png"
    },
    "USA": {
        "cities": ["New York", "Chicago", "Boston"],
        "map": "maps/usa.png"
    },
    "Japan": {
        "cities": ["Tokyo", "Osaka", "Kyoto"],
        "map": "maps/japan.png"
    }
}


def show_map(country):
    """Display the map of the selected country."""
    global map_image

    path = os.path.join(BASE_DIR, COUNTRIES[country]["map"])

    try:
        img = Image.open(path)
        img = img.resize((250, 150))
        map_image = ImageTk.PhotoImage(img)
        map_label.config(image=map_image)
    except FileNotFoundError:
        map_label.config(text="❌ Map not found")


def check_city():
    country = country_var.get()
    city = city_entry.get().strip()

    if city in COUNTRIES[country]["cities"]:
        messagebox.showinfo(
            "Correct!",
            f"✅ Yes! {city} is in {country} 🎉"
        )
    else:
        correct = ", ".join(COUNTRIES[country]["cities"])
        messagebox.showerror(
            "Oops!",
            f"❌ {city} is NOT in {country}.\n\nCorrect cities:\n{correct}"
        )


def country_changed(*args):
    show_map(country_var.get())


# ---- GUI ----
root = tk.Tk()
root.title("Country & City Game")
root.geometry("450x450")

tk.Label(
    root,
    text="🌍 Country & City Game",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Choose a country:").pack()

country_var = tk.StringVar(value="India")
country_var.trace_add("write", country_changed)

country_menu = tk.OptionMenu(
    root,
    country_var,
    *COUNTRIES.keys()
)
country_menu.pack(pady=5)

map_label = tk.Label(root)
map_label.pack(pady=10)

tk.Label(root, text="Type a city:").pack()
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(
    root,
    text="Check Answer",
    command=check_city
).pack(pady=15)

show_map("India")

root.mainloop()

# to fix the above
#A map cannot appear unless ALL of these are true:

# The image file exists

#The filename matches exactly (lowercase/uppercase matters)

#The image is in the correct folder

#Tkinter is told the correct path

#The image object is kept in memory (classic Tkinter gotcha)

#Your error happened because #1 or #2 or #3 failed.
# do the following:
#_THE CORRECT & SAFE WAY TO SHOW MAPS (Tkinter only)
#'' STEP 1: Create this folder structure
u
#Inside your project:

#servicesProject/
#│
#├── mapcountrycitygame.py
#│
#└── maps/
    #├── india.png
#├── usa.png
    #└── japan.png

#⚠️ VERY IMPORTANT

#Filenames must be exactly:

#india.png

#usa.png

#japan.png

#All lowercase

#PNG format