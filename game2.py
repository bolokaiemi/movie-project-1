import wikipedia
import random
import json
import os
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

# =========================
# Configuration
# =========================
COUNTRIES_FILE = "countries.json"
CITIES_FILE = "cities.json"

ALLOWED_COUNTRIES = [
    "Germany",
    "France",
    "Japan",
    "India",
    "United States"
]

# =========================
# In-memory storage
# =========================
COUNTRIES = []
CITIES = []

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
        json.dump(COUNTRIES, f, indent=4)
    with open(CITIES_FILE, "w", encoding="utf-8") as f:
        json.dump(CITIES, f, indent=4)

# =========================
# Wikipedia helpers
# =========================
def fetch_summary(name, sentences=2):
    try:
        return wikipedia.summary(name, sentences=sentences)
    except:
        return "No information available."

# =========================
# Data logic
# =========================
def country_exists(name):
    for c in COUNTRIES:
        if normalize(c["name"]) == normalize(name):
            return c
    return None

def add_country(name):
    existing = country_exists(name)
    if existing:
        return existing

    country = {
        "id": len(COUNTRIES) + 1,
        "name": name,
        "summary": fetch_summary(name)
    }
    COUNTRIES.append(country)
    save_data()
    return country

def add_cities(country):
    city_names = wikipedia.search(country["name"] + " cities")[:3]
    for name in city_names:
        if not any(c["name"] == name for c in CITIES):
            CITIES.append({
                "name": name,
                "country_id": country["id"],
                "summary": fetch_summary(name, 1)
            })
    save_data()

def get_cities(country):
    return [c for c in CITIES if c["country_id"] == country["id"]]

# =========================
# Game UI
# =========================
def welcome_message():
    print("\n🎮 Country & City Quiz Game 🎮")
    print("Rules:")
    print("• Answer questions in free text")
    print("• Correct answer = +1 point")
    print("• Wikipedia is the source of truth\n")

def gather_players():
    while True:
        try:
            n = int(input("Number of players (1–3): "))
            if 1 <= n <= 3:
                break
        except ValueError:
            pass
        print("Invalid number.")

    players = []
    for i in range(n):
        players.append({
            "name": input(f"Player {i+1} name: "),
            "score": 0
        })
    return players

# =========================
# Question Engine
# =========================
def ask_capital_question(player, country):
    print(f"\n🎯 {player['name']}'s turn")
    answer = input(f"What is the capital of {country['name']}? ")

    try:
        page = wikipedia.page(country["name"])
        capital = page.infobox.get("capital")
    except:
        capital = None

    if capital and normalize(answer) in normalize(capital):
        print("✅ Correct!")
        player["score"] += 1
    else:
        print(f"❌ Correct answer: {capital}")

def ask_population_question(player, city1, city2):
    print(f"\n🎯 {player['name']}'s turn")
    answer = input(f"Which has a larger population: {city1} or {city2}? ")

    try:
        p1 = int(wikipedia.page(city1).infobox.get("population_total"))
        p2 = int(wikipedia.page(city2).infobox.get("population_total"))
    except:
        print("Population data unavailable.")
        return

    correct = city1 if p1 > p2 else city2
    if normalize(answer) == normalize(correct):
        print("✅ Correct!")
        player["score"] += 1
    else:
        print(f"❌ Correct answer: {correct}")

# =========================
# Main loop
# =========================
def main():
    load_data()
    welcome_message()
    players = gather_players()

    print("\nAvailable countries:", ", ".join(ALLOWED_COUNTRIES))
    country_name = input("Choose a country: ")

    if country_name not in ALLOWED_COUNTRIES:
        print("Invalid country.")
        return

    country = add_country(country_name)
    add_cities(country)
    cities = get_cities(country)

    for i, player in enumerate(players):
        ask_capital_question(player, country)
        if len(cities) >= 2:
            ask_population_question(player, cities[0]["name"], cities[1]["name"])

    print("\n🏆 Final Scores:")
    for p in players:
        print(f"{p['name']}: {p['score']} points")

if __name__ == "__main__":
    main()