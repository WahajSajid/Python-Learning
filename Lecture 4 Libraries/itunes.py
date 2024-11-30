import requests
import sys
import json
if len(sys.argv)!=2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
data = response.json()
print(json.dumps(data,indent=2))
for result in data["results"]:
    print(result["trackName"])