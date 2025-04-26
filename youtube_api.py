from googleapiclient.discovery import build

# API key
api_key = "AIzaSyApmPvynUnuIYB6L5QOearwY4ZYJD639eU"

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=api_key)

# Search for music videos
request = youtube.search().list(
    part="snippet",
    q="AI-generated music", 
    type="video",
    maxResults=5
)

response = request.execute()

# Print video titles and URLs
for item in response["items"]:
    print(f"Title: {item['snippet']['title']}")
    print(f"URL: https://www.youtube.com/watch?v={item['id']['videoId']}")
    print()
