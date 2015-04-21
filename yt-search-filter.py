"""This program is designed to facilitate rapidly
finding a video and its link on YouTube. Instructions for use:
Install elementtree and gdata 2.0 APIs.
Run program through command prompt of choice and enter a query
to be searched on YouTube. Specific queries work best.
Then enter a second query to filter the results through.
This is because YouTube delivers results with the query not
necessarily in the title. One word queries on this part work best.
If an output.txt file is in the same directory as the program,
the results satisfying the paramaters will be added to the file."""

import elementtree, httplib, urllib, gdata.youtube, gdata.youtube.service

SortedYTFeed = {}
result = {}

# Functions take YouTube query and process them into a dictionary
# ----------------------------------------------------------------
def UpdateSortedFeed(entry):
  SortedYTFeed.update({entry.media.title.text: entry.GetSwfUrl()})
		
def LoopThroughEntries(feed):
  for entry in feed.entry:
    UpdateSortedFeed(entry)

def YouTubeSearch(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'relevance'
  query.max_results = 50
  feed = yt_service.YouTubeQuery(query)
  LoopThroughEntries(feed)
# ----------------------------------------------------------------

# Basic search function accepting dictionaries
def search(Websites, query):
  for i in Websites:
    for j in range(len(i)):
      if i[j:j + len(query)].lower() == query.lower():
	result.update({i: Websites[i]})
  return result
  
YouTubeSearch(raw_input("Enter query for YouTube search:\n> "))

SortedYTFeed = {key: value for key, value in SortedYTFeed.items() if key != "https://youtube.com/devicesupport"}

search(SortedYTFeed, raw_input("Enter query for search refinement:\n> "))

# Writes to file to make large results more managable
with open("output.txt", "r+") as output:
  # OVERWRITES OUTPUT FILE ON EACH RUN
  output.truncate()
  for i in result:
    output.write(i + " - " + result[i] + "\n\n")
