database = [
    {
        "country": "USA",
        "cities": ["New York", "Los Angeles", "Chicago"]
    },
    {
        "country": "India",
        "cities": ["Delhi", "Mumbai", "Bangalore"]
    },
    {
        "country": "Japan",
        "cities": ["Tokyo", "Osaka", "Kyoto"]
    }
]
# Simple list-based country → city database (easy & clear)
def get_cities(country_name):
    for record in database:
        if record["country"].lower() == country_name.lower():
            return record["cities"]
    return "Country not found"

print(get_cities("India"))


# Add new country or city
# Add a new country
def add_country(country, cities):
    database.append({
        "country": country,
        "cities": cities
    })

add_country("France", ["Paris", "Lyon", "Marseille"])


# Add a city to an existing country
def add_city(country, city):
    for record in database:
        if record["country"].lower() == country.lower():
            record["cities"].append(city)
            return
    print("Country not found")

add_city("USA", "San Francisco")

# Fully normalized list “database” (more realistic)
countries = [
    {"id": 1, "name": "USA"},
    {"id": 2, "name": "India"},
    {"id": 3, "name": "Japan"}
]

cities = [
    {"name": "New York", "country_id": 1},
    {"name": "Los Angeles", "country_id": 1},
    {"name": "Delhi", "country_id": 2},
    {"name": "Mumbai", "country_id": 2},
    {"name": "Tokyo", "country_id": 3}
]

# Get cities by country name

def get_cities_by_country(country_name):
    country_id = None
    for country in countries:
        if country["name"].lower() == country_name.lower():
            country_id = country["id"]
            break

    if country_id is None:
        return "Country not found"

    return [city["name"] for city in cities if city["country_id"] == country_id]

print(get_cities_by_country("USA"))

#################Final Recommended Structure (Simple & Practical)

database = [
    {"country": "USA", "cities": ["New York", "Los Angeles", "Chicago"]},
    {"country": "India", "cities": ["Delhi", "Mumbai", "Bangalore"]},
    {"country": "Japan", "cities": ["Tokyo", "Osaka", "Kyoto"]}
]