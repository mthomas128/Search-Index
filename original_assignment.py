# Sample dictionary of websites
ListOfWebsites = {
  "Google": "http://www.google.com",
  "Apple": "http://www.apple.com",
  "YouTube": "http://www.youtube.com",
  "Forbes": "http://www.forbes.com",
  "Yahoo!": "http://www.yahoo.com",
  "Gmail": "http://www.gmail.com"
}

result = {}

# Basic search function accepting dictionaries
def search(Websites, query):
  for i in Websites:
    for j in range(len(i)):
      if i[j:j + len(query)].lower() == query.lower():
	result.update({i: Websites[i]})
  return result

# Runs function; looks nice in OS's command prompt
search(ListOfWebsites, raw_input("Enter query:\n> "))

# Writes to file to make large results more managable
with open("output.txt", "r+") as output:
  # OVERWRITES OUTPUT FILE ON EACH RUN
  output.truncate()
  for i in result:
    output.write(i + " - " + result[i] + "\n")
