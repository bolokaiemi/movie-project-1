database = [
    {"country": "USA", "cities": ["New York", "Los Angeles", "Chicago"]},
    {"country": "India", "cities": ["Delhi", "Mumbai", "Bangalore"]},
    {"country": "Japan", "cities": ["Tokyo", "Osaka", "Kyoto"]}
]
######################Core Operations (for small projects & learning)############################
# Get cities
def get_cities(country):
    for record in database:
        if record["country"].lower() == country.lower():
            return record["cities"]
    return []




# Add country
def add_country(country):
    database.append({"country": country, "cities": []})


# Add city
    def add_city(country, city):
        for record in database:
            if record["country"].lower() == country.lower():
                record["cities"].append(city)
                return

# Remove city

def remove_city(country, city):
    for record in database:
        if record["country"].lower() == country.lower():
            if city in record["cities"]:
                record["cities"].remove(city)



print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

countries = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

cities = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Chicago", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Tokyo", "country_id": 3}
]





   # """
   #Suitable for:
    # Small projects
    # Learning data structures
    # Scripts & prototypes

 



countries = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

cities = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Chicago", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Tokyo", "country_id": 3}
]

def get_cities_by_country(country_name):
    for country in countries:   # ✅ correct variable name
        if country["name"].lower() == country_name.lower():
            country_id = country["id"]
            break
    else:
        return "Country not found"

    return [city["name"] for city in cities if city["country_id"] == country_id]


print(get_cities_by_country("USA"))



print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..................................")
import socket
import threading
import wikipedia
import random

# -----------------------------
# List-based "database"
# -----------------------------

countries = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

cities = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Chicago", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Tokyo", "country_id": 3}
]

# -----------------------------
# Function
# -----------------------------

def get_cities_by_country(country_name):
    country_id = None

    for country in countries:
        if country["name"].lower() == country_name.lower():
            country_id = country["id"]
            break

    if country_id is None:
        return "Country not found"

    return [city["name"] for city in cities if city["country_id"] == country_id]


# -----------------------------
# Main
# -----------------------------

def main():
    """
    Main function to start the online gaming service.
    """
    print("Starting online gaming service...")
    result = get_cities_by_country("USA")
    print("Cities in USA:", result)


if __name__ == "__main__":
    main()


print("::::::::::::::::::::::::::::::::")
import socket
import threading
import wikipedia
import random

# =====================================================
# In-memory list "database"
# Suitable for:
# ✅ Small projects
# ✅ Learning data structures
# ❌ Large datasets
# ❌ Multi-user applications
# =====================================================

COUNTRIES = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

CITIES = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Chicago", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Tokyo", "country_id": 3}
]

# =====================================================
# Core Logic
# =====================================================

def get_country_id(country_name):
    """Return country ID or None (O(n) search)."""
    for country in COUNTRIES:
        if country["name"].lower() == country_name.lower():
            return country["id"]
    return None


def get_cities_by_country(country_name):
    """
    Get all cities for a given country.
    ❌ Not optimized for large datasets
    ❌ Not thread-safe
    """
    if not country_name:
        return "Invalid country name"

    country_id = get_country_id(country_name)

    if country_id is None:
        return "Country not found"

    return [city["name"] for city in CITIES if city["country_id"] == country_id]


def get_random_city(country_name):
    """Return a random city from a country."""
    cities = get_cities_by_country(country_name)

    if isinstance(cities, str):
        return cities

    return random.choice(cities) if cities else "No cities available"


# =====================================================
# Main Application (Prototype)
# =====================================================

def main():
    print("Starting online gaming service (prototype)...")

    country = "USA"

    cities = get_cities_by_country(country)
    print(f"Cities in {country}: {cities}")

    random_city = get_random_city(country)
    print(f"Random city in {country}: {random_city}")


if __name__ == "__main__":
    main()

    print(":::::::::....................................................................................................")

import random

# =====================================================
# In-MEMORY DATA (List-Based Database)
# =====================================================

COUNTRIES = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

CITIES = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Chicago", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Bangalore", "country_id": 2},
    {"name": "Tokyo", "country_id": 3},
    {"name": "Osaka", "country_id": 3}
]

# =====================================================
# CORE LOGIC (Single Responsibility Functions)
# =====================================================

def normalize(text):
    """Normalize user input for reliable comparison."""
    return text.strip().lower()


def get_country_by_name(country_name):
    """Return country dict or None."""
    name = normalize(country_name)
    for country in COUNTRIES:
        if normalize(country["name"]) == name:
            return country
    return None


def get_cities_for_country_id(country_id):
    """Return list of city names for a country_id."""
    return [city["name"] for city in CITIES if city["country_id"] == country_id]


def get_cities_by_country_name(country_name):
    """High-level API used by the application."""
    country = get_country_by_name(country_name)

    if not country:
        return None

    return get_cities_for_country_id(country["id"])


def get_random_city(country_name):
    """Return one random city or None."""
    cities = get_cities_by_country_name(country_name)
    if not cities:
        return None
    return random.choice(cities)

# =====================================================
# USER INTERACTION (CLI Prototype)
# =====================================================

def prompt_user_for_country():
    """Ask user until a valid country is entered."""
    while True:
        user_input = input("\nEnter a country name (or 'exit'): ")

        if normalize(user_input) == "exit":
            return None

        country = get_country_by_name(user_input)
        if country:
            return country["name"]

        print("❌ Country not found. Try again.")


def main():
    print("=== Country & City Lookup Service ===")
    print("Type a country name to see its cities.")

    while True:
        country_name = prompt_user_for_country()

        if country_name is None:
            print("Goodbye 👋")
            break

        cities = get_cities_by_country_name(country_name)

        print(f"\nCities in {country_name}:")
        for city in cities:
            print(" •", city)

        random_city = get_random_city(country_name)
        print(f"\n🎲 Random city suggestion: {random_city}")


if __name__ == "__main__":
    main()

print("::::::::::::::::::::advance::::::::::::::::::::::::::::::::::::::.........")
import wikipedia
import random

# =====================================================
# In-Memory List-Based Storage (LLD Friendly)
# =====================================================

COUNTRIES = []  # [{id, name, summary}]
CITIES = []  # [{name, country_id, summary}]

# =====================================================
# Utility Functions
# =====================================================


def normalize(text):
    return text.strip().lower()


def country_exists(country_name):
    for country in COUNTRIES:
        if normalize(country["name"]) == normalize(country_name):
            return country
    return None

#added:::::::::::::::::::::::::

def ask_capital_question(player, country):
    ...

def get_next_country_id():
    return len(COUNTRIES) + 1

    # =====================================================
    # Wikipedia Integration
    # =====================================================


def fetch_country_from_wikipedia(country_name):
    """
    Fetch country summary from Wikipedia.
    """
    try:
        summary = wikipedia.summary(country_name, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return None


def fetch_city_from_wikipedia(city_name):
    """
    Fetch city summary from Wikipedia.
    """
    try:
        return wikipedia.summary(city_name, sentences=1)
    except:
        return "No detailed information available."

    # =====================================================
    # Core Logic
    # =====================================================


def add_country(country_name):
    """
    Add country to list-based DB if not already present.
    """
    existing = country_exists(country_name)
    if existing:
        return existing

    summary = fetch_country_from_wikipedia(country_name)
    if not summary:
        return None

    country = {
        "id": get_next_country_id(),
        "name": country_name,
        "summary": summary
    }

    COUNTRIES.append(country)
    return country


def add_cities_for_country(country, city_names):
    """
    Add cities related to a country.
    """
    for name in city_names:
        city = {
            "name": name,
            "country_id": country["id"],
            "summary": fetch_city_from_wikipedia(name)
        }
        CITIES.append(city)


def get_cities_by_country(country_name):
    country = country_exists(country_name)
    if not country:
        return []

    return [city for city in CITIES if city["country_id"] == country["id"]]

    # =====================================================
    # User Interaction (CLI Prototype)
    # =====================================================


def main():
    print("=== Wikipedia-Based Country & City Collector ===")
    print("Type 'exit' to quit.")

    while True:
        country_name = input("\nEnter a country name: ")

        if normalize(country_name) == "exit":
            print("Goodbye 👋")
            break

        country = add_country(country_name)
        if not country:
            print("❌ Could not fetch country data.")
            continue

        print(f"\n📘 {country['name']} (Wikipedia Summary)")
        print(country["summary"])

        # Example city list (LLD simplification)
        default_cities = wikipedia.search(country_name + " cities")[:3]

        add_cities_for_country(country, default_cities)

        cities = get_cities_by_country(country_name)

        print("\n🏙 Cities collected:")
        for city in cities:
            print(f"- {city['name']}: {city['summary']}")


if __name__ == "__main__":
    main()
 # in the above , how do i do the following:
#Extendable

#You can update and replace:
# make it to become a game connected to the map

#Lists → JSON / DB

#Wikipedia → API

#CLI → Socket / Web