import webbrowser
import json
from urllib.request import  urlopen

print("Let's find an old website.")
site = input('Type a website URL: ')
era = input("Type a year, month, and day, like YYYYMMDD : ")
url = f'http://archive.org/wayback/available?url={site}&timestamp={era}'

response = urlopen(url)
contents = response.read()
text = contents.decode("UTF-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print(f'Found this copy : {old_site}')
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print(f"Sorry, no luck finding {site}")

