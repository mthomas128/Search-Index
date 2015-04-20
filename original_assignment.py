# Sample dictionary of websites
ListOfWebsites = {
  "http://www.google.com": "Google",
  "http://www.apple.com": "Apple",
  "http://www.youtube.com": "YouTube",
  "http://www.forbes.com": "Forbes",
  "http://www.yahoo.com": "Yahoo",
  "http://www.gmail.com": "Gmail"
}

result = {}

# Basic search function accepting dictionaries
def search(Websites, query):
  for i in Websites:
    for j in range(len(i)):
      if i[j:j + len(query)] == query:
	result.update({i: Websites[i]})
  return result

# Runs function; looks nice in OS's command prompt
search(ListOfWebsites, raw_input("Enter query:\n> "))

# Writes to file to make large results more managable
with open("output.txt", "r+") as output:
  # OVERWRITES OUTPUT FILE ON EACH RUN
  output.truncate()
  for i in result:
    output.write(result[i] + " - " + i + "\n")