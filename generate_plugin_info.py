import requests
import json
from bs4 import BeautifulSoup

# Fetch the simple index page
url = "https://pypi.org/simple/"
response = requests.get(url)
response.raise_for_status()

# Extract packages starting with "cmem-plugin"
soup = BeautifulSoup(response.text, 'html.parser')
plugins = [a.text for a in soup.find_all('a') if a.text.startswith("cmem-plugin")]

# Function to fetch plugin details from PyPI
def fetch_plugin_info(plugin_name):
    """Fetch plugin details from PyPI."""
    try:
        url = f"https://pypi.org/pypi/{plugin_name}/json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        info = data['info']
        return {
            "id": plugin_name,
            "name": info['name'],
            "description": info['description'] or "No description available",
            "latest_version": info['version']
        }
    except requests.RequestException as e:
        print(f"Error fetching data for {plugin_name}: {e}")
        return None

# Fetch plugin details and store them
plugin_info_list = []
for plugin in plugins:
    plugin_info = fetch_plugin_info(plugin)
    if plugin_info:
        plugin_info_list.append(plugin_info)

# Save the plugin information to a JSON file
with open("plugins_info.json", "w") as file:
    json.dump(plugin_info_list, file, indent=4)

print(f"Found {len(plugin_info_list)} cmem-plugin packages.")

