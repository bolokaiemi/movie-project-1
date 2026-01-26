# Write a Python script

import wikipedia

# Search
print(wikipedia.search("Python programming"))

# Get a summary
summary = wikipedia.summary("Python (programming language)", sentences=3)
print(summary)

# Get a full page
page = wikipedia.page("Python (programming language)")
print(page.title)
print(page.url)