import wikipedia
import random
import json
import os

# In-memory storage
COUNTRIES = []
CITIES = []

# File paths
COUNTRIES_FILE = "countries.json"
CITIES_FILE = "cities.json"

# =========================
# Utility functions
# =========================
def normalize(text):
    return text.strip().lower()

def load_data():
    global COUNTRIES, CITIES
    if os.path.exists(COUNTRIES_FILE):
        with open(COUNTRIES_FILE, "r", encoding="utf-8") as f:
            COUNTRIES = json.load(f)
    if os.path.exists(CITIES_FILE):
        with open(CITIES_FILE, "r", encoding="utf-8") as f:
            CITIES = json.load(f)

def save_data():
    with open(COUNTRIES_FILE, "w", encoding="utf-8") as f:
        json.dump(COUNTRIES, f, ensure_ascii=False, indent=4)
    with open(CITIES_FILE, "w", encoding="utf-8") as f:
        json.dump(CITIES, f, ensure_ascii=False, indent=4)

# =========================
# Wikipedia functions
# =========================
def fetch_country_from_wikipedia(name):
    try:
        return wikipedia.summary(name, sentences=2)
    except:
        return "No detailed information available."

def fetch_city_from_wikipedia(name):
    try:
        return wikipedia.summary(name, sentences=1)
    except:
        return "No detailed information available."

# =========================
# Core functions
# =========================
def country_exists(name):
    for c in COUNTRIES:
        if normalize(c["name"]) == normalize(name):
            return c
    return None

def get_next_country_id():
    return len(COUNTRIES) + 1

def add_country(name):
    existing = country_exists(name)
    if existing:
        return existing
    summary = fetch_country_from_wikipedia(name)
    country = {"id": get_next_country_id(), "name": name, "summary": summary}
    COUNTRIES.append(country)
    save_data()
    return country

def add_cities_for_country(country, city_names):
    existing_city_names = [c["name"].lower() for c in CITIES if c["country_id"] == country["id"]]
    for name in city_names:
        if name.lower() not in existing_city_names:
            city = {"name": name, "country_id": country["id"], "summary": fetch_city_from_wikipedia(name)}
            CITIES.append(city)
    save_data()

def get_cities_by_country(name):
    country = country_exists(name)
    if not country:
        return []
    return [c for c in CITIES if c["country_id"] == country["id"]]

def prompt_user_for_country():
    while True:
        user_input = input("Enter a country name (or 'exit'): ")
        if normalize(user_input) == "exit":
            return None
        country = country_exists(user_input) or add_country(user_input)
        if country:
            return country
        print("❌ Country not found. Try again.")

# =========================
# Player setup
# =========================
def welcome_message():
    print("=== Welcome to the Country & City Game ===")
    print("1. Enter a country name when prompted.")
    print("2. Wikipedia summaries will be shown.")
    print("3. Top 3 cities will be collected.")
    print("4. Type 'exit' to quit.\n")

def gather_players():
    while True:
        try:
            num = int(input("Enter number of players (1-3): "))
            if 1 <= num <= 3:
                break
            else:
                print("❌ Please enter a number between 1 and 3.")
        except ValueError:
            print("❌ Invalid input.")
    players = []
    for i in range(num):
        name = input(f"Enter Player {i+1} name: ").strip()
        players.append(name)
    print(f"✅ Players: {', '.join(players)}\n")
    return players

# =========================
# Main loop
# =========================
def main():
    load_data()
    welcome_message()
    players = gather_players()

    while True:
        country = prompt_user_for_country()
        if not country:
            print("Goodbye 👋")
            break

        print(f"\n📘 {country['name']} (Wikipedia Summary):")
        print(country["summary"])

        default_cities = wikipedia.search(country["name"] + " cities")[:3]
        add_cities_for_country(country, default_cities)

        cities = get_cities_by_country(country["name"])
        print("\n🏙 Cities collected:")
        for city in cities:
            print(f"- {city['name']}: {city['summary']}")

# =========================
# Run program
# =========================
if __name__ == "__main__":
    main()