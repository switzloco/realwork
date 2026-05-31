import sys
sys.path.insert(0, '.')
from src.bright_data.client import BrightDataClient
client = BrightDataClient()
print(client.serp('"WEST VALLEY BOOSTERS" California'))
